# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SpeechGenerateParams"]


class SpeechGenerateParams(TypedDict, total=False):
    language: Required[Literal["yo", "en", "ha", "ig", "am", "pcm"]]

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
            "john",
            "jude",
            "lina",
            "lucy",
            "henry",
            "kani",
            "ngozi",
            "amara",
            "obinna",
            "ebuka",
            "hana",
            "selam",
            "tena",
            "tesfaye",
        ]
    ]

    model: Optional[str]

    spitch_x_data_retention: Annotated[bool, PropertyInfo(alias="Spitch-X-Data-Retention")]
