# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Diacritics"]


class Diacritics(BaseModel):
    """
    Response model for text diacritization requests.

        Attributes:
            request_id: Unique identifier for the diacritization request
            text: Text with added diacritical marks for proper pronunciation
            language: Language code for the diacritized text
    """

    request_id: str

    text: str
