# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SpeechTranscribeResponse", "Timestamp"]


class Timestamp(BaseModel):
    end: float

    start: float

    text: str


class SpeechTranscribeResponse(BaseModel):
    request_id: str

    text: str

    timestamps: Optional[List[Timestamp]] = None
