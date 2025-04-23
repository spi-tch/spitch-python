# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["SpeechTranscribeParams"]


class SpeechTranscribeParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig", "am"]]

    content: Optional[FileTypes]

    multispeaker: Optional[bool]

    timestamp: Optional[bool]

    url: Optional[str]
