# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["SpeechTranscribeParams"]


class SpeechTranscribeParams(TypedDict, total=False):
    content: Required[Union[FileTypes, str]]
    """The audio file or content that you want to transcribe.

    This could be; `file bytes`, a `url to an audio file` (ensure the link does not
    require authentication to access the file) or a `file UUID`.
    """

    language: Optional[str]
    """
    This is optional, an ISO-639 language code that corresponds to the language in
    the `content`.
    """

    model: Optional[Literal["mansa_v1", "legacy"]]
    """
    Select the model to be used to perform the transcription, this param has been
    deprecated.
    """

    special_words: Optional[str]

    timestamp: Optional[Literal["sentence", "word"]]
