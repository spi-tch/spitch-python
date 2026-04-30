# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .segment import Segment
from .._models import BaseModel

__all__ = ["Transcription"]


class Transcription(BaseModel):
    """Response from speech-to-text."""

    request_id: Optional[str] = None
    """for audit purposes."""

    segments: Optional[List[Segment]] = None
    """Either `sentence-level` or `word-level` groupings of your transcript.

    Each sentence (or word) will fall within a time range.
    """

    text: Optional[str] = None
