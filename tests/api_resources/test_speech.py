# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from spitch import Spitch, AsyncSpitch
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Spitch) -> None:
        speech = client.speech.generate(
            language="yo",
            text="text",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Spitch) -> None:
        speech = client.speech.generate(
            language="yo",
            text="text",
            stream=True,
            voice="sade",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Spitch) -> None:
        response = client.speech.with_raw_response.generate(
            language="yo",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = response.parse()
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Spitch) -> None:
        with client.speech.with_streaming_response.generate(
            language="yo",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = response.parse()
            assert_matches_type(object, speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_transcibe(self, client: Spitch) -> None:
        speech = client.speech.transcibe(
            language="yo",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    def test_method_transcibe_with_all_params(self, client: Spitch) -> None:
        speech = client.speech.transcibe(
            language="yo",
            content=b"raw file contents",
            url="url",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    def test_raw_response_transcibe(self, client: Spitch) -> None:
        response = client.speech.with_raw_response.transcibe(
            language="yo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = response.parse()
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    def test_streaming_response_transcibe(self, client: Spitch) -> None:
        with client.speech.with_streaming_response.transcibe(
            language="yo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = response.parse()
            assert_matches_type(object, speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeech:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate(self, async_client: AsyncSpitch) -> None:
        speech = await async_client.speech.generate(
            language="yo",
            text="text",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncSpitch) -> None:
        speech = await async_client.speech.generate(
            language="yo",
            text="text",
            stream=True,
            voice="sade",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncSpitch) -> None:
        response = await async_client.speech.with_raw_response.generate(
            language="yo",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = await response.parse()
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncSpitch) -> None:
        async with async_client.speech.with_streaming_response.generate(
            language="yo",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = await response.parse()
            assert_matches_type(object, speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_transcibe(self, async_client: AsyncSpitch) -> None:
        speech = await async_client.speech.transcibe(
            language="yo",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    async def test_method_transcibe_with_all_params(self, async_client: AsyncSpitch) -> None:
        speech = await async_client.speech.transcibe(
            language="yo",
            content=b"raw file contents",
            url="url",
        )
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    async def test_raw_response_transcibe(self, async_client: AsyncSpitch) -> None:
        response = await async_client.speech.with_raw_response.transcibe(
            language="yo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = await response.parse()
        assert_matches_type(object, speech, path=["response"])

    @parametrize
    async def test_streaming_response_transcibe(self, async_client: AsyncSpitch) -> None:
        async with async_client.speech.with_streaming_response.transcibe(
            language="yo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = await response.parse()
            assert_matches_type(object, speech, path=["response"])

        assert cast(Any, response.is_closed) is True
