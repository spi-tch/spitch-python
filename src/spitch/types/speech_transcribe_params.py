# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["SpeechTranscribeParams"]


class SpeechTranscribeParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig", "am"]]

    content: Optional[FileTypes]

    model: Optional[Literal["mansa_v1", "legacy", "human"]]

    special_words: Optional[str]

    timestamp: Optional[Literal["sentence", "word", "none"]]

    url: Optional[str]
