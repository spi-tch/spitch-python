# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from spitch import Spitch, AsyncSpitch
from tests.utils import assert_matches_type
from spitch.types import TextToneMarkResponse, TextTranslateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_tone_mark(self, client: Spitch) -> None:
        text = client.text.tone_mark(
            language="yo",
            text="text",
        )
        assert_matches_type(TextToneMarkResponse, text, path=["response"])

    @parametrize
    def test_raw_response_tone_mark(self, client: Spitch) -> None:
        response = client.text.with_raw_response.tone_mark(
            language="yo",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text = response.parse()
        assert_matches_type(TextToneMarkResponse, text, path=["response"])

    @parametrize
    def test_streaming_response_tone_mark(self, client: Spitch) -> None:
        with client.text.with_streaming_response.tone_mark(
            language="yo",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text = response.parse()
            assert_matches_type(TextToneMarkResponse, text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_translate(self, client: Spitch) -> None:
        text = client.text.translate(
            source="yo",
            target="yo",
            text="text",
        )
        assert_matches_type(TextTranslateResponse, text, path=["response"])

    @parametrize
    def test_raw_response_translate(self, client: Spitch) -> None:
        response = client.text.with_raw_response.translate(
            source="yo",
            target="yo",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text = response.parse()
        assert_matches_type(TextTranslateResponse, text, path=["response"])

    @parametrize
    def test_streaming_response_translate(self, client: Spitch) -> None:
        with client.text.with_streaming_response.translate(
            source="yo",
            target="yo",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text = response.parse()
            assert_matches_type(TextTranslateResponse, text, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncText:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_tone_mark(self, async_client: AsyncSpitch) -> None:
        text = await async_client.text.tone_mark(
            language="yo",
            text="text",
        )
        assert_matches_type(TextToneMarkResponse, text, path=["response"])

    @parametrize
    async def test_raw_response_tone_mark(self, async_client: AsyncSpitch) -> None:
        response = await async_client.text.with_raw_response.tone_mark(
            language="yo",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text = await response.parse()
        assert_matches_type(TextToneMarkResponse, text, path=["response"])

    @parametrize
    async def test_streaming_response_tone_mark(self, async_client: AsyncSpitch) -> None:
        async with async_client.text.with_streaming_response.tone_mark(
            language="yo",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text = await response.parse()
            assert_matches_type(TextToneMarkResponse, text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_translate(self, async_client: AsyncSpitch) -> None:
        text = await async_client.text.translate(
            source="yo",
            target="yo",
            text="text",
        )
        assert_matches_type(TextTranslateResponse, text, path=["response"])

    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncSpitch) -> None:
        response = await async_client.text.with_raw_response.translate(
            source="yo",
            target="yo",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text = await response.parse()
        assert_matches_type(TextTranslateResponse, text, path=["response"])

    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncSpitch) -> None:
        async with async_client.text.with_streaming_response.translate(
            source="yo",
            target="yo",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text = await response.parse()
            assert_matches_type(TextTranslateResponse, text, path=["response"])

        assert cast(Any, response.is_closed) is True
