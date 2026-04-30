# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechGenerateParams"]


class SpeechGenerateParams(TypedDict, total=False):
    text: Required[str]
    """The text for which you want to generate audio."""

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
            "remi",
            "kingsley",
            "ngozi",
            "amara",
            "obinna",
            "ebuka",
            "hana",
            "haile",
            "tena",
            "tesfaye",
            "ufoma",
            "tega",
            "justice",
            "boma",
        ]
    ]
    """The voice you want to be used for audio generation."""

    format: Literal["mp3", "wav", "ogg_opus", "webm_opus", "mulaw", "alaw", "flac", "pcm_s16le"]
    """The audio format for the returned audio data, defaults to `wav`."""

    language: str
    """This is optional; an ISO 639 language code to be used for the generation."""

    speed: float
    """The speed of the voice, defaults to `1.0`"""
