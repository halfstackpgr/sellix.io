from ..enums.caller import (
    ShopType,
    Currency,
    DashboardFeature,
    SortCustomTheme,
    DefaultSort,
    OrderOrigin,
    OrderSubtype,
    OrderType,
)
from ..enums.checkables import (
    DisplayTaxOnStorefront,
    DisplayTaxCustomFields,
    ValidationOnlyForCompanies,
    ValidateVatNumber,
    PricesTaxInclusive,
    NotifySubscriptionRenewalFailure,
    NotifyTrialEnding,
    NotifyUpcomingRenewal,
    OrderEmails,
    PayPalCreditCard,
    ForcePaypalEmailDelivery,
    NonCustodialWallet,
    DarkMode,
    SearchEnabled,
    SortEnabled,
    CartEnabled,
    HideOutOfStock,
    HideProductsSold,
    HideStockCounter,
    ServiceDateFrom,
    CenterProductTitles,
    CenterGroupTitles,
    CustomTheme,
    CustomEmbed,
    DescriptionYouTubeOnly,
    OnHold,
    Verified,
    DescriptionImage,
    DescriptionSkipDefaultImage,
    SetupWizard,
    SetupCryptocurrencies,
    MarketplaceVerified,
)
from .subtype import ProductVariant

import msgspec
import typing as t


class Shop(msgspec.Struct):
    """
    A class that represents a Sellix `Shop` or `GET self` method on the API.

    
    Reference: [sellix.get_self](https://docs.sellix.io/apireference/information/getself)
    """

    id: t.Optional[int]
    """The ID of the shop"""

    user_id: t.Optional[int]
    """The ID of the user who requested the shop info"""

    shop_type: t.Optional[ShopType] = msgspec.field(name="type")
    """The type of the shop"""

    name: t.Optional[str]
    """The name of the shop"""

    avatar: t.Optional[str]
    """The [hash](https://www.geeksforgeeks.org/whatishashing) for the avatar"""

    currency: t.Optional[Currency]
    """Available currency."""

    default_currency: t.Optional[Currency]
    """Available currency."""

    vat_percentage: t.Optional[str]
    """The VAT percentage setup for the store"""

    tax_configuration: t.Optional[str]
    """The tax configuration for the shop"""

    dashboard_feature: t.Optional[DashboardFeature]
    """The organization mode set for the dashboard"""

    display_tax_on_storefront: t.Optional[DisplayTaxOnStorefront]
    """The tax percentage will be shown on the product cards of your storefront, and not on the checkout page and invoice PDF only."""

    display_tax_custom_fields: t.Optional[DisplayTaxCustomFields]
    """Whether the tax is displayed in custom fields"""

    validation_only_for_companies: t.Optional[ValidationOnlyForCompanies]
    """Wheter or not VAT validation is only done for companies"""

    validate_vat_number: t.Optional[ValidateVatNumber]
    """If enabled, we will validate the Company VAT number to be sure it's correct."""

    prices_tax_inclusive: t.Optional[PricesTaxInclusive]
    """Whether or not product pricing incldues the VAT"""

    notify_trial_ending: t.Optional[NotifyTrialEnding]
    """Send an email to your customers when the trial period is ending."""

    notify_upcoming_renewal: t.Optional[NotifyUpcomingRenewal]
    """Send an email to your customers days before an upcoming renewal."""

    notify_subscription_renewal_failure: t.Optional[NotifySubscriptionRenewalFailure]
    """Send an email to your customers when a subscription renewal fails."""

    order_emails: t.Optional[OrderEmails]
    """Whether or not order emails are enabled"""

    subscription_grace_period: t.Optional[int]
    """In days, how much time should we wait before cancelling a subscription if no payment is completed."""

    paypal_credit_card: t.Optional[PayPalCreditCard]
    """Whether or not the shop accepts credit cards via PayPal"""

    force_paypal_email_delivery: t.Optional[ForcePaypalEmailDelivery]
    """Whether or not the shop accepts credit cards via PayPal"""

    paypal_merchant_id: t.Optional[str]
    """The PayPal merchant ID of the PayPal account linked to the shop"""

    binance_id: t.Optional[str]
    """The Binance ID of the Binance account linked to the shop"""

    walletconnect_id: t.Optional[str]
    """The WalletConnect ID of the WalletConnect account linked to the shop"""

    non_custodial_wallet: t.Optional[NonCustodialWallet]
    """Whether or not the shop uses the Sellix noncustodial crypto wallet"""

    dark_mode: t.Optional[DarkMode]
    """Whether or not the shop is in dark mode"""

    discord_link: t.Optional[str]
    """The Discord link of the shop"""

    twitter_link: t.Optional[str]
    """The link to the shop's Twitter account"""

    instagram_link: t.Optional[str]
    """The link to the shop's Instagram account"""

    facebook_link: t.Optional[str]
    """The link to the shop's Facebook account"""

    telegram_link: t.Optional[str]
    """The invite link to the shop's Telegram community"""

    youtube_link: t.Optional[str]
    """The invite link to the shop's Youtube channel"""

    reddit_link: t.Optional[str]
    """The link to the shop's SubReddit"""

    tiktok_link: t.Optional[str]
    """The link to the shop's TikTok account"""

    search_enabled: t.Optional[SearchEnabled]
    """Whether or not the shop has dark mode enabled"""

    sort_enabled: t.Optional[SortEnabled]
    """Whether or not the shop has product sorting enabled"""

    cart_enabled: t.Optional[CartEnabled]
    """Whether or not the shop has the cart system enabled"""

    cart_maximum_checkout: t.Optional[str]
    """Set the maximum amount, in your currency, for an order made through the Shopping Cart."""

    hide_out_of_stock: t.Optional[HideOutOfStock]
    """Automatically hide your products when out of stock."""

    google_analytics_tracking_id: t.Optional[str]
    """The google analyticd tracking id the shop uses for analytics"""

    crisp_website_id: t.Optional[str]
    """The crisp website id the shop uses for analytics"""

    center_product_titles: t.Optional[CenterProductTitles]
    """Whether or not the shop's theme centers product titles"""

    center_group_titles: t.Optional[CenterGroupTitles]
    """Whether or not the shop's theme centers group titles"""

    popup_message: t.Optional[str]
    """This message will be shown to anyone who visits your site. Do not include your Terms of Service here."""

    verified: t.Optional[Verified]
    """Whether or not the shop is verified by Sellix"""

    on_hold: t.Optional[OnHold]
    """Whether or not the shop is on hold"""

    terms_of_service: t.Optional[str]
    """The terms of service for the shop in MDX"""

    primary_color_custom_theme: t.Optional[str]
    """The primary color of the shop's custom theme. Value is null if no custom theme is used."""

    secondary_color_custom_theme: t.Optional[str]
    """The secondary color of the shop's custom theme. Value is null if no custom theme is used."""

    primary_font_color_custom_theme: t.Optional[str]
    """The primary font color of the shop's custom theme. Value is null if no custom theme is used."""

    secondary_font_color_custom_theme: t.Optional[str]
    """The secondary font color of the shop's custom theme. Value is null if no custom theme is used."""

    custom_embed: t.Optional[CustomEmbed]
    """Whether or not the shop uses a custom embed theme. Value is null if no custom theme is used."""

    custom_theme: t.Optional[CustomTheme]
    """Whether or not the shop uses a custom storefront theme. Value is null if no custom theme is used."""

    font_custom_theme: t.Optional[str]
    """The font of the shop's custom storefront theme. Value is null if no custom theme is used."""

    style_custom_theme: t.Optional[str]
    """The style of the shop's custom storefront theme. Value is null if no custom theme is used."""

    embed_style_custom_theme: t.Optional[str]
    """The style of the shop's custom embed theme. Value is null if no custom theme is used."""

    index_custom_theme: t.Optional[str]
    """The index of the shop's active custom storefront theme. Value is null if no custom theme is used."""

    product_card_custom_theme: t.Optional[str]
    """The product_card of the shop's active custom storefront theme. Value is null if no custom theme is used."""

    banner_custom_theme: t.Optional[object]
    """The storefront banner of the shop's custom theme. Value is null if no custom theme is used."""

    footer_custom_theme: t.Optional[object]
    """The storefront footer of the shop's custom theme. Value is null if no custom theme is used."""

    background_image_custom_theme: t.Optional[object]
    """The storefront background image of the shop's custom theme. Value is null if no custom theme is used."""

    logo_custom_theme: t.Optional[object]
    """The storefront logo of the shop's custom theme. Value is null if no custom theme is used."""

    header_custom_theme: t.Optional[object]
    """The storefront header of the shop's custom theme. Value is null if no custom theme is used."""

    cards_in_row_custom_theme: t.Optional[int]
    """The amount of cards to display in a row on the storefront"""

    cards_align_custom_theme: t.Optional[object]
    """Value is null if no custom theme is used."""

    group_card_custom_theme: t.Optional[object]
    """Value is null if no custom theme is used."""

    card_animation_custom_theme: t.Optional[object]
    """Value is null if no custom theme is used."""

    light_font_color_custom_theme: t.Optional[str]
    """The light mode font color of the shop's custom theme. Value is null if no custom theme is used."""

    dark_font_color_custom_theme: t.Optional[str]
    """The dark mode font color of the shop's custom theme. Value is null if no custom theme is used."""

    light_color_custom_theme: t.Optional[str]
    """light_color_custom_theme"""

    dark_color_custom_theme: t.Optional[str]
    """The dark mode accent color of the shop's custom theme. Value is null if no custom theme is used."""

    border_color_custom_theme: t.Optional[str]
    """The border color of the shop's custom theme. Value is null if no custom theme is used."""

    button_color_custom_theme: t.Optional[str]
    """The button color of the shop's custom theme. Value is null if no custom theme is used."""

    thin_color_custom_theme: t.Optional[str]
    """The thin font color of the shop's custom theme. Value is null if no custom theme is used."""

    sort_custom_theme: t.Optional[SortCustomTheme]
    """The default sorting method for the storefront's custom theme"""

    helpspace_client_id: t.Optional[str]
    """The helpspace client id of the helpspace account linked to the shop"""

    helpspace_token: t.Optional[str]
    """The helpspace token of the helpspace account linked to the shop"""

    description_youtube_only: t.Optional[DescriptionYouTubeOnly]
    """Show only youtube video for invoice/product description."""

    description_skip_default_image: t.Optional[DescriptionSkipDefaultImage]
    """Skip Default Image for Product Description."""

    hide_stock_counter: t.Optional[HideStockCounter]
    """If enabled, the number of how many products are in stock will be removed, we will only show 'In Stock' or 'Out of Stock'."""

    image_width: t.Optional[int]
    """The width of the storefront image"""

    image_height: t.Optional[int]
    """The height of the storefront image"""

    default_sort: t.Optional[DefaultSort]
    """The default sorting method for the storefront"""

    description_image: t.Optional[DescriptionImage]
    """Whether or not the shop has a description image."""

    hide_products_sold: t.Optional[HideProductsSold]
    """Hide the products sold counter on your storefront, only your average feedback will be displayed."""

    service_date_from: t.Optional[ServiceDateFrom]
    """Choose whether to display your business starting date from the day of your first sale or the day you have signed up to Sellix."""

    cards_type: t.Optional[str]
    """`DEPRECATED`: The name of the product image with the file type"""

    setup_wizard: t.Optional[SetupWizard]
    """Whether or not the shop has completed the setup wizzard"""

    setup_cryptocurrencies: t.Optional[SetupCryptocurrencies]
    """Whether or not the shop has setup cryptocurrencies"""

    notices_banner: t.Optional[str]
    """The notices for the shop"""

    affiliate_revenue_percent: t.Optional[int]
    """The percentage of each payment given to affiliates"""

    created_at: t.Optional[int]
    """Timestamp for the creation of the subscription."""

    image_name: t.Optional[str]
    """`DEPRECATED`: The name of the product image with the file type"""

    image_storage: t.Optional[str]
    """Where the image is stored in Sellix's selfhosted CDN."""

    cloudflare_image_id: t.Optional[str]
    """
    #### New field containing the cloudflare image ID of this product.
    Replaces `image_attachment` and `image_name`.
    Format
    URL: `https://imagedelivery.net/95QNzrEeP7RU5l5WdbyrKw/<cloudflare_image_id>/<variant_name>`
    Where `variant_name` can be `shopItem`, `avatar`, `icon`, `imageAvatarFeedback`, `public`, `productImageCart`.
    """

    marketplace_verified: t.Optional[MarketplaceVerified]
    """Whether or not the shop is a verified marketplace"""

    available_currency: t.Optional[Currency] = None
    """Available currency."""

class Order(msgspec.Struct):
    """
    A class that represents a Sellix `Order`

    ---
    Reference: [sellix.get_self](https://docs.sellix.io/apireference/information/getself)
    """
    id: t.Optional[int]
    """ID of the resource."""
    uniqid: t.Optional[str]
    """Unique ID of the resource, used as reference across the API."""

    recurring_billing_id: str
    payout_configuration: str
    type: OrderType
    subtype: OrderSubtype
    origin: OrderOrigin
    total: int
    total_display: int
    product_variants: t.List[ProductVariant]
    exchange_rate: int
    crypto_exchange_rate: int
    currency: str
    shop_id: int
    shop_image_name: str
    shop_image_storage: str
    cloudflare_image_id: str
    name: str
    customer_email: str
    customer_id: str
    affliate_revenue_customer_id: str
    paypal_email_delivery: bool
    product_id: str
    product_title: str
    product_type: str
    subscription_id: int
    subscription_time: int
    gateway: str
    blockchain: str
    paypal_apm: str
    stripe_apm: str
    paypal_email: str
    paypal_order_id: str
    paypal_payer_email: str
    paypal_fee: int
    paypal_subscription_id: int
    paypal_subscription_link: int
    lex_order_id: str
    lex_payment_method: str
    paydash_payment_id: str
    virtual_payments_id: str
    stripe_client_secret: str
    stripe_price_id: str
    skrill_email: str
    skrill_sid: str
    skrill_link: str
    perfectmoney_id: UUID
    binance_invoice_id: str
    binance_qrcode: str
    binance_checkout_url: str
    crypto_address: str
    crypto_amount: float
    crypto_received: float
    crypto_uri: str
    crypto_confirmations_needed: int
    crypto_scheduled_payout: bool
    crypto_payout: bool
    fee_billed: bool
    bill_info: BillInfo
    cashapp_qrcode: str
    cashapp_note: UUID
    cashapp_cashtag: str
    country: str
    location: str
    ip: str
    is_vpn_or_proxy: bool
    user_agent: str
    quantity: int
    coupon_id: UUID
    custom_fields: CustomFields
    developer_invoice: bool
    developer_title: str
    developer_webhook: str
    developer_return_url: str
    status: str
    status_details: str
    void_details: str
    discount: int
    fee_percentage: int
    fee_breakdown: FeeBreakdown
    discount_breakdown: BillInfo
    day_value: int
    day: str
    month: str
    year: int
    product_addons: List[Addon]
    bundle_config: List[BundleConfig]
    created_at: int
    updated_at: int
    updated_by: int
    approved_address: ApprovedAddress
    service_text: str
    ip_info: IPInfo
    webhooks: List[Webhook]
    rewards_data: List[RewardsDatum]
    paypal_dispute: PaypalDispute
    product_downloads: List[ProductDownload]
    payment_link_id: str
    cashapp_email_configured: bool
    license: bool
    status_history: List[StatusHistory]
    aml_wallets: List[AmlWallet]
    crypto_transactions: List[CryptoTransaction]
    product: Product
    total_conversions: str
    theme: str
    dark_mode: int
    crypto_mode: str
    gateways_available: List[str]
    country_regulations: str
    available_stripe_apm: AvailableStripeApm
    serials: List[str]
    shop_payment_gateways_fees: List[PaymentGatewaysFee]
    shop_paypal_credit_card: bool
    shop_force_paypal_email_delivery: bool
    shop_walletconnect_id: str
    original_developer_return_url: str
    rates_snapshot: RatesSnapshot
    void_times: List[VoidTime]