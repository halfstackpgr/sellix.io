from enum import (
    Enum,
)


class DisplayTaxOnStorefront(Enum):
    DISABLED = 0
    """Tax percentage will not be shown on the product cards of your storefront."""

    ENABLED = 1
    """Tax percentage will be shown on the product cards of your storefront."""


class DisplayTaxCustomFields(Enum):
    DISABLED = 0
    """Tax is not displayed in custom fields."""

    ENABLED = 1
    """Tax is displayed in custom fields."""


class ValidationOnlyForCompanies(Enum):
    DISABLED = 0
    """VAT validation is not done only for companies."""

    ENABLED = 1
    """VAT validation is only done for companies."""


class ValidateVatNumber(Enum):
    DISABLED = 0
    """VAT number validation is disabled."""

    ENABLED = 1
    """VAT number validation is enabled."""


class PricesTaxInclusive(Enum):
    DISABLED = 0
    """Product pricing does not include the VAT."""

    ENABLED = 1
    """Product pricing includes the VAT."""


class NotifyTrialEnding(Enum):
    DISABLED = 0
    """No email is sent to customers when the trial period is ending."""

    ENABLED = 1
    """An email is sent to customers when the trial period is ending."""


class NotifyUpcomingRenewal(Enum):
    DISABLED = 0
    """No email is sent to customers before an upcoming renewal."""

    ENABLED = 1
    """An email is sent to customers before an upcoming renewal."""


class NotifySubscriptionRenewalFailure(Enum):
    DISABLED = 0
    """No email is sent to customers if a subscription renewal fails."""

    ENABLED = 1
    """An email is sent to customers if a subscription renewal fails."""


class OrderEmails(Enum):
    DISABLED = 0
    """Shop owner does not receive emails for orders."""

    ENABLED = 1
    """Shop owner receives emails for orders."""


class PayPalCreditCard(Enum):
    DISABLED = 0
    """Shop does not accept credit cards via PayPal."""

    ENABLED = 1
    """Shop accepts credit cards via PayPal."""


class ForcePaypalEmailDelivery(Enum):
    DISABLED = 0
    """Shop does not deliver products to the PayPal email when the gateway is PAYPAL."""

    ENABLED = 1
    """Shop delivers products to the PayPal email when the gateway is PAYPAL."""


class NonCustodialWallet(Enum):
    DISABLED = 0
    """The shop does not use the Sellix non-custodial crypto wallet."""

    ENABLED = 1
    """The shop uses the Sellix non-custodial crypto wallet."""


class DarkMode(Enum):
    DISABLED = 0
    """Dark mode is not enabled for the shop."""

    ENABLED = 1
    """Dark mode is enabled for the shop."""


class SearchEnabled(Enum):
    DISABLED = 0
    """Search functionality is disabled for the shop."""

    ENABLED = 1
    """Search functionality is enabled for the shop."""


class SortEnabled(Enum):
    DISABLED = 0
    """Product sorting is disabled for the shop."""

    ENABLED = 1
    """Product sorting is enabled for the shop."""


class CartEnabled(Enum):
    DISABLED = 0
    """The cart system is disabled for the shop."""

    ENABLED = 1
    """The cart system is enabled for the shop."""


class HideOutOfStock(Enum):
    DISABLED = 0
    """Products are not automatically hidden when out of stock."""

    ENABLED = 1
    """Products are automatically hidden when out of stock."""


class CenterProductTitles(Enum):
    DISABLED = 0
    """The shop's theme does not center product titles."""

    ENABLED = 1
    """The shop's theme centers product titles."""


class CenterGroupTitles(Enum):
    DISABLED = 0
    """The shop's theme does not center group titles."""

    ENABLED = 1
    """The shop's theme centers group titles."""


class Verified(Enum):
    NOT_VERIFIED = 0
    """The shop is not verified by Sellix."""

    VERIFIED = 1
    """The shop is verified by Sellix."""


class OnHold(Enum):
    NOT_ON_HOLD = 0
    """The shop is not on hold."""

    ON_HOLD = 1
    """The shop is on hold."""


class CustomEmbed(Enum):
    NOT_USED = 0
    """The shop does not use a custom embed theme."""

    ENABLED = 1
    """The shop uses a custom embed theme."""


class CustomTheme(Enum):
    NOT_USED = 0
    """The shop does not use a custom storefront theme."""

    ENABLED = 1
    """The shop uses a custom storefront theme."""


class DescriptionYouTubeOnly(Enum):
    DISABLED = 0
    """Both YouTube videos and other types of content are shown for invoice/product description."""

    ENABLED = 1
    """Only YouTube videos are shown for invoice/product description."""


class DescriptionSkipDefaultImage(Enum):
    DISABLED = 0
    """Default images are not skipped for product description."""

    ENABLED = 1
    """Default images are skipped for product description."""


class HideStockCounter(Enum):
    DISABLED = 0
    """The number of products in stock is displayed."""

    ENABLED = 1
    """Only 'In Stock' or 'Out of Stock' messages are displayed, without showing the exact number of products in stock."""


class DescriptionImage(Enum):
    NO_DESCRIPTION_IMAGE = 0
    """The shop does not have a description image."""

    HAS_DESCRIPTION_IMAGE = 1
    """The shop has a description image."""


class HideProductsSold(Enum):
    NO_HIDE_PRODUCTS_SOLD = 0
    """The products sold counter is not hidden on the storefront."""

    HIDE_PRODUCTS_SOLD = 1
    """The products sold counter is hidden on the storefront."""


class ServiceDateFrom(Enum):
    REGISTRATION_DATE = "REGISTRATION_DATE"
    """The business starting date is displayed from the day of signing up to Sellix."""

    FIRST_SALE = "FIRST_SALE"
    """The business starting date is displayed from the day of the first sale."""


class SetupWizard(Enum):
    NOT_COMPLETED = 0
    """The shop has not completed the setup wizard."""

    COMPLETED = 1
    """The shop has completed the setup wizard."""


class SetupCryptocurrencies(Enum):
    NOT_SETUP = 0
    """Cryptocurrencies have not been set up for the shop."""

    SETUP = 1
    """Cryptocurrencies have been set up for the shop."""


class MarketplaceVerified(Enum):
    NOT_VERIFIED = 0
    """The shop is not a verified marketplace."""

    VERIFIED = 1
    """The shop is a verified marketplace."""
