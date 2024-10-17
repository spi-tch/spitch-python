# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechGenerateParams"]


class SpeechGenerateParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig"]]

    text: Required[str]

    stream: bool

    voice: Literal["sade", "segun", "femi", "funmi"]