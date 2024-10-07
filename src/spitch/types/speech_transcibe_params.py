# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["SpeechTranscibeParams"]


class SpeechTranscibeParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig"]]

    content: Optional[FileTypes]

    url: Optional[str]
