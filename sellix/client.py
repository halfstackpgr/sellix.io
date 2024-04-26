import asyncio
from datetime import datetime, timedelta
from urllib.parse import urljoin, urlparse
from .enums.genric import MerchantTier, APIEndpoints
from .abc.interaction import ShopInteraction
from .abc.modals import Shop
import msgspec
import aiohttp
import typing as t


class SellixClientX:
    def __init__(
        self,
        auth_key: str,
        merchant_id: t.Optional[str] = None,
        default_blacklist: t.Optional[int] = None,
        merchant_tier: t.Optional[MerchantTier] = MerchantTier.STANDARD,
        enable_auto_rate_limit_handler: t.Optional[bool] = False,
        custom_rate_limit_time: t.Optional[int] = None,
        restrict_methods: t.Optional[t.Literal["GET", "POST", "PUT", "DEL"]] = None,
        logging: t.Optional[bool] = False,
        ratelimits_by_tasks: t.Optional[bool] = True,
    ) -> None:
        self.base_url = "https://dev.sellix.io/v1"

        if auth_key is None:
            raise ValueError("auth_key cannot be None")

        self.headers: t.Dict[str, str] = {
            "Authorization": f"Bearer {auth_key}",
        }

        if merchant_id:
            self.headers["X-Sellix-Merchant"] = f"{merchant_id}"

        self.__session = aiohttp.ClientSession(headers=self.headers)
        self.merchant_tier = merchant_tier
        self.rate_limit_task_queue = asyncio.Queue() if ratelimits_by_tasks else None
        self.enable_auto_rate_limit_handler = enable_auto_rate_limit_handler
        self.custom_rate_limit_time = custom_rate_limit_time or 10
        self.restrict_methods = restrict_methods
        self.ratelimits_by_tasks = ratelimits_by_tasks
        self.semaphore = asyncio.Semaphore(self.merchant_tier.value)  #type: ignore
        self.blacklist = default_blacklist
        if self.enable_auto_rate_limit_handler:
            asyncio.create_task(self._rate_limit_handler())


    async def _rate_limit_handler(self):
        while True:
            await asyncio.sleep(self.custom_rate_limit_time)

            current_time = datetime.now()
            await self._handle_rate_limit(current_time)

    async def _handle_rate_limit(self, current_time: datetime):
        if self.merchant_tier is None:
            return

        limit = int(self.merchant_tier.value)  # type: ignore
        rate_limit_window_start = current_time - timedelta(
            seconds=self.custom_rate_limit_time
        )

        tasks_executed_within_window = 0
        for task_time, _ in self.rate_limit_task_queue._queue:  # type: ignore
            if task_time >= rate_limit_window_start:
                tasks_executed_within_window += 1

        if tasks_executed_within_window >= limit:
            delay = (
                rate_limit_window_start + timedelta(seconds=self.custom_rate_limit_time)
            ) - current_time
            print(
                f"Rate limit exceeded for {self.merchant_tier.name} tier. Waiting for {delay.total_seconds()} seconds."
            )
            await asyncio.sleep(delay.total_seconds())

        print(f"Rate limit check completed for {self.merchant_tier.name} tier.")

        if self.rate_limit_task_queue:
            await self.rate_limit_task_queue.put(
                (current_time, await self._execute_tasks())
            )

    async def _execute_tasks(self):
        if self.rate_limit_task_queue:
            while not self.rate_limit_task_queue.empty():
                # Acquire the semaphore before executing a task
                async with self.semaphore:
                    time, task = await self.rate_limit_task_queue.get()
                    if datetime.now() - time <= timedelta(
                        seconds=self.custom_rate_limit_time
                    ):
                        await task

    async def _make_request(
        self, method: t.Literal["GET", "POST", "PUT", "DEL"], api_method: APIEndpoints
    ) -> bytes:
        """
        Generic method to make an API request.

        Args:
            method (Literal["GET", "POST", "PUT", "DEL"]): The HTTP method to use.
            api_method (APIEndpoints): The API endpoint to send the request to.

        Returns:
            bytes: The response body.
        """
        if method == "GET":
            url = urljoin(self.base_url, api_method.value)
            print(self.base_url)
            print(url)
            async with self.__session.get(
                url=url
            ) as response:
                
                return await response.read()
        elif method == "POST":
            async with self.__session.post(
                urljoin(self.base_url, api_method.value)
            ) as response:
                print(await response.json())
                return await response.read()
        elif method == "PUT":
            async with self.__session.put(
                urljoin(self.base_url, api_method.value)
            ) as response:
                print(await response.json())
                return await response.read()
        elif method == "DEL":
            async with self.__session.delete(
                urljoin(self.base_url, api_method.value)
            ) as response:
                print(await response.json())
                return await response.read()
            

    async def get_shop(self) -> t.Optional[Shop]:
        get_shop = await self._make_request("GET", APIEndpoints.GET_SHOP)
        base = msgspec.json.decode(
            get_shop, 
            strict=False,
            type=ShopInteraction
        )
        return base.data
    
    async def close(self):
        await self.__session.close()
