# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechGenerateParams"]


class SpeechGenerateParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig", "am"]]

    text: Required[str]

    voice: Required[
        Literal[
            "sade",
            "segun",
            "femi",
            "funmi",
            "amina",
            "aliyu",
            "hasan",
            "zainab",
            "ngozi",
            "amara",
            "ebuka",
            "obinna",
            "lucy",
            "lina",
            "john",
            "jude",
            "henry",
            "kani",
            "hana",
            "selam",
            "tena",
            "tesfaye",
        ]
    ]

    stream: bool
