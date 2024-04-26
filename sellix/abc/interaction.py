from .modals import Shop

import msgspec
import typing as t

class ShopInteraction(msgspec.Struct): 
    """Base class for all Sellix API responses."""
    
    # Attributes
    status: int
    """HTTP status code of the response."""
    
    data: t.Optional[Shop]
    
    error: t.Optional[str]
    """Error message, if any."""
    
    message: t.Optional[str]
    """General message, if any."""
    
    env: t.Optional[str]
    """Environment in which the request was made."""




    
