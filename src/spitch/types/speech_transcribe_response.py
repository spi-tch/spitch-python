# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SpeechTranscribeResponse", "Segment"]


class Segment(BaseModel):
    end: Optional[int] = None

    speaker: Optional[int] = None

    start: Optional[int] = None

    text: Optional[int] = None


class SpeechTranscribeResponse(BaseModel):
    request_id: str

    segments: Optional[List[Optional[Segment]]] = None

    text: Optional[str] = None
