from enum import (
    Enum,
)


class MerchantTier(Enum):
    """
    A class representing all the given tiers according to Sellix.

    To upgrade to a higher tier, please reach out to us at [sales@sellix.io](mailto:sales@sellix.io) or through our [Discord community](https://sellix.io/discord).

    ---
    Reference: [sellix.tier](https://docs.sellix.io/api-reference/errors#general-endpoints)
    """

    STANDARD = 5
    """
    Standard sellix tier allows general rate-limit of 5 requests, per 10s.
    - `STANDARD`: Represents the standard tier with a value of 5.
    """

    TIER_1 = (75,)
    """
    Represents Tier 1 with a rate-limit of 75 requests per 10s.
    - `TIER_1`: Represents Tier 1 with a rate-limit of 75.
    """

    TIER_2 = (100,)

    """
    Represents Tier 2 with a rate-limit of 100 requests per 10s.
    - `TIER_2`: Represents Tier 2 with a rate-limit of 100.
    """

    TIER_3 = 500
    """
    Represents Tier 3 with a rate-limit of 500 requests per 10s.
    - `TIER_3`: Represents Tier 3 with a rate-limit of 500.
    """


class WebHookEvents(Enum):
    """
    A class representing all the `webhook` events.

    ---
    Reference: [sellix.webhooks](https://docs.sellix.io/api-reference/webhooks#events)
    """

    ORDER_CREATED = (
        "order:created",
        "The order has been created.",
    )
    """Event triggered when an order is created."""

    ORDER_UPDATED = (
        "order:updated",
        "The order status has changed.",
    )
    """Event triggered when the order status is updated."""

    ORDER_PARTIAL = (
        "order:partial",
        "The order status is now partial, indicating a cryptocurrency payment that has been sent but not covering the whole amount.",
    )
    """Event triggered when the order status becomes partial."""

    ORDER_PAID = (
        "order:paid",
        "The order has been flagged as paid, this is the final state.",
    )
    """Event triggered when the order is marked as paid."""

    ORDER_CANCELLED = (
        "order:cancelled",
        "The order has been cancelled either by the fraud shield, the merchant, or due to not receiving a payment within the time window.",
    )
    """Event triggered when the order is cancelled."""

    ORDER_DISPUTED = (
        "order:disputed",
        "A Stripe/PayPal dispute has been opened against one of your stores.",
    )
    """Event triggered when a dispute is opened against an order."""

    PRODUCT_CREATED = (
        "product:created",
        "A product has been created.",
    )
    """Event triggered when a product is created."""

    PRODUCT_STOCK = (
        "product:stock",
        "A product’s stock has fallen below the warning range.",
    )
    """Event triggered when a product's stock falls below the warning range."""

    PRODUCT_EDITED = (
        "product:edited",
        "A product has been edited.",
    )
    """Event triggered when a product is edited."""

    PRODUCT_DYNAMIC = (
        "product:dynamic",
        "This event is issued only for dynamic products.",
    )
    """Event issued only for dynamic products."""

    QUERY_CREATED = (
        "query:created",
        "A query has been created for one of your shops.",
    )
    """Event triggered when a query is created."""

    QUERY_REPLIED = (
        "query:replied",
        "A reply has been received for one of your queries.",
    )
    """Event triggered when a reply is received for a query."""

    FEEDBACK_RECEIVED = (
        "feedback:received",
        "One of your customers left a feedback for you.",
    )
    """Event triggered when a feedback is received."""

    SUBSCRIPTION_TRIAL_STARTED = (
        "subscription:trial:started",
        "A trial has been started for one of your subscriptions.",
    )
    """Event triggered when a trial is started for a subscription."""

    SUBSCRIPTION_TRIAL_ENDED = (
        "subscription:trial:ended",
        "A trial has ended for one of your subscriptions, this is usually followed by an order:created event.",
    )
    """Event triggered when a trial ends for a subscription."""

    SUBSCRIPTION_CREATED = (
        "subscription:created",
        "A subscription has been created.",
    )
    """Event triggered when a subscription is created."""

    SUBSCRIPTION_UPDATED = (
        "subscription:updated",
        "A subscription has been updated.",
    )
    """Event triggered when a subscription is updated."""

    SUBSCRIPTION_RENEWED = (
        "subscription:renewed",
        "A subscription has been renewed, after receiving a new payment.",
    )
    """Event triggered when a subscription is renewed."""

    SUBSCRIPTION_CANCELLED = (
        "subscription:cancelled",
        "A subscription has been canceled, either due to not receiving a payment or by a manual action of the customer.",
    )
    """Event triggered when a subscription is cancelled."""

    SUBSCRIPTION_UPCOMING = (
        "subscription:upcoming",
        "A customer will have to pay for one of your subscriptions in the next 72 hours.",
    )
    """Event triggered when a subscription payment is upcoming."""

    ORDER_PAID_PRODUCT = (
        "order:paid:product",
        "This event is the same as order:paid, however the :product segment indicates that it originates from a webhook URL configured within a product, which is now deprecated.",
    )
    """Event triggered when an order is paid through a product webhook URL."""

    ORDER_PARTIAL_PRODUCT = (
        "order:partial:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order status is partial through a product webhook URL."""

    ORDER_CREATED_PRODUCT = (
        "order:created:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order is created through a product webhook URL."""

    ORDER_DISPUTED_PRODUCT = (
        "order:disputed:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order is disputed through a product webhook URL."""

    ORDER_CANCELLED_PRODUCT = (
        "order:cancelled:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order is cancelled through a product webhook URL."""

    ORDER_UPDATED_PRODUCT = (
        "order:updated:product",
        "Similar to order:paid, this event is the same as its parent.",
    )
    """Event triggered when an order status is updated through a product webhook URL."""


class LinkStep(Enum):
    """
    A class representing the available step number to be configured on links.

    ---
    Reference: [sellix.prefilledlinks](https://docs.sellix.io/api-reference/prefilled-links#available-querystring-parameters)
    """

    DEFAULT_CHECKOUT = 0
    """The default checkout step (product details)"""
    GATEWAY_CHOICE = 1
    """The gateway choice step"""
    EMAIL_AND_PAY_BUTTON = 3
    """The email and pay button step"""


class APIEndpoints(Enum):
    """
    A class representing the available API endpoints.

    ---
    Reference: [sellix.api.reference](https://docs.sellix.io/api-reference/)
    """

    GET_SHOP = "/v1/self"
    """
    `GET` Shop affiliated to the API key.
    """

    GET_ORDER = "/v1/orders/{uniqid}"
    """
    `GET` Specifc order using `uniqid`.
    """

    GET_ORDER_LIST = "/v1/orders"
    """
    `GET` List of orders.
    """

    GET_CONSTUMERS = "/v1/customers/{id}"
    """
    `GET` Specific customer using `id`.
    """

    GET_CONSTUMERS_LIST = "/v1/customers"
    """
    `GET` List of customers.
    """

    GET_SUBSCRIPTION = "/v1/subscriptions/{id}"
    """
    `GET` Specific subscription using `id`.
    """

    GET_SUBSCRIPTION_LIST = "/v1/subscriptions"
    """
    `GET` List of subscriptions.
    """

    GET_BLACKLIST = "/v1/blacklists/{uniqid}"
    """
    `GET` Specific blacklisted entry using `uniqid`.
    """

    GET_BLACKLIST_LIST = "/v1/blacklists"
    """
    `GET` List of blacklisted entries.
    """

    GET_WHITELIST = "/v1/whitelists/{uniqid}"
    """
    `GET` Specific whitelisted entry using `uniqid`.
    """

    GET_WHITELIST_LIST = "/v1/whitelists"
    """
    `GET` List of whitelisted entries.
    """

    GET_PRODUCT = "/v1/products/{uniqid}"
    """
    `GET` Specific product using `uniqid`.
    """

    GET_PRODUCT_LIST = "/v1/products"
    """
    `GET` List of products.
    """

    GET_CATEGORY = "/v1/categories/{uniqid}"
    """
    `GET` Specific category using `uniqid`.
    """

    GET_CATEGORY_LIST = "/v1/categories"
    """
    `GET` List of categories.
    """

    GET_GROUP = "/v1/groups/{uniqid}"
    """
    `GET` Specific group using `uniqid`.
    """

    GET_GROUP_LIST = "/v1/groups"
    """
    `GET` List of groups.
    """

    GET_COUPON = "/v1/coupons/{uniqid}"
    """
    `GET` Specific coupon using `uniqid`.
    """

    GET_COUPON_LIST = "/v1/coupons"
    """
    `GET` List of coupons.
    """

    GET_FEEDBACK = "/v1/feedback/{uniqid}"
    """
    `GET` Specific feedback using `uniqid`.
    """

    GET_FEEDBACK_LIST = "/v1/feedback"
    """
    `GET` List of feedbacks.
    """

    GET_QUERY = "/v1/queries/{uniqid}"
    """
    `GET` Specific query using `uniqid`.
    """

    GET_QUERY_LIST = "/v1/queries"
    """
    `GET` List of queries.
    """
