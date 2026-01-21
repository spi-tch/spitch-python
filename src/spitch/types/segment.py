# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Segment"]


class Segment(BaseModel):
    """a segment (sentence or word-level) of the transcript.

    It contains a start and end time.
    """

    end: float
    """the exact time when this segment ended."""

    start: float
    """the exact time when this segment started."""

    text: str
    """the text that belongs in this timeframe."""
