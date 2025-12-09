# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Translation"]


class Translation(BaseModel):
    """Translation result model.

    Attributes:
        request_id (UUID): Unique ID for this request.
        text: translated text.
        due_date: used when model is `human`. the date you can expect the translation to be delivered
    """

    request_id: str

    text: str

    due_date: Optional[datetime] = None
