# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Transcription", "Timestamp"]


class Timestamp(BaseModel):
    end: float

    start: float

    text: str


class Transcription(BaseModel):
    request_id: str

    text: str

    timestamps: Optional[List[Timestamp]] = None
