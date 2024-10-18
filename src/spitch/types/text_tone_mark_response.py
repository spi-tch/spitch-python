# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TextToneMarkResponse"]


class TextToneMarkResponse(BaseModel):
    request_id: str

    text: Optional[str] = None
