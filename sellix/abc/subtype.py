import msgspec

class ProductVariant(msgspec.Struct):
    price: int
    title: str
    description: str
    price_conversions: object