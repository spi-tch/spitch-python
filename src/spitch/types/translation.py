# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Translation"]


class Translation(BaseModel):
    request_id: str

    text: str

    due_date: Optional[datetime] = None
