# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextTranslateParams"]


class TextTranslateParams(TypedDict, total=False):
    source: Required[Literal["yo", "en", "ha", "ig", "am"]]

    target: Required[Literal["yo", "en", "ha", "ig", "am"]]

    text: Required[str]
