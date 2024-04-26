from sellix.client import SellixClientX

import datetime

s = SellixClientX(
    auth_key="KKCGz5LVmvbXJBbYdBVvfbwncQXCzEna9SaZFckuMttrqRpX8DRsKxEOLMnNFbCw"
)


import asyncio
from enum import Enum


async def main():
    client = SellixClientX(
        auth_key="KKCGz5LVmvbXJBbYdBVvfbwncQXCzEna9SaZFckuMttrqRpX8DRsKxEOLMnNFbCw"
    )
    shop = await client.get_shop()
    if shop:
        print(shop.avatar)

asyncio.run(main())
