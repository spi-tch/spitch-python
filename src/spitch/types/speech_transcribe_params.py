# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SpeechTranscribeParams"]


class SpeechTranscribeParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig", "am", "pcm"]]

    content: Union[FileTypes, str, None]

    model: Optional[Literal["mansa_v1", "legacy"]]

    special_words: Optional[str]

    timestamp: Optional[Literal["sentence", "word", "none"]]

    url: Optional[str]

    x_data_retention: Annotated[bool, PropertyInfo(alias="X-Data-Retention")]
