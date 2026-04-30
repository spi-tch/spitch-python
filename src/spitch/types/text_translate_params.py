# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextTranslateParams"]


class TextTranslateParams(TypedDict, total=False):
    target: Required[str]
    """An ISO 639 code of the language you want to translate to."""

    text: Required[str]
    """The text to be translated."""

    formality: Literal["casual", "formal"]
    """Whether to be `formal` or `casual`."""

    source: Optional[str]
    """An ISO 639 code of the language you're translating from"""

    tone: Literal["neutral", "warm", "professional", "narration"]
    """The tone of the translated text."""
