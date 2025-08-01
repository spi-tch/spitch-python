# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TextTranslateResponse"]


class TextTranslateResponse(BaseModel):
    request_id: str

    text: str
