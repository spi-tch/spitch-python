# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from spitch import Spitch, AsyncSpitch
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Spitch) -> None:
        transcription = client.transcriptions.create(
            language="yo",
        )
        assert_matches_type(object, transcription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Spitch) -> None:
        transcription = client.transcriptions.create(
            language="yo",
            content=b"raw file contents",
            url="url",
        )
        assert_matches_type(object, transcription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Spitch) -> None:
        response = client.transcriptions.with_raw_response.create(
            language="yo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(object, transcription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Spitch) -> None:
        with client.transcriptions.with_streaming_response.create(
            language="yo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(object, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSpitch) -> None:
        transcription = await async_client.transcriptions.create(
            language="yo",
        )
        assert_matches_type(object, transcription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSpitch) -> None:
        transcription = await async_client.transcriptions.create(
            language="yo",
            content=b"raw file contents",
            url="url",
        )
        assert_matches_type(object, transcription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSpitch) -> None:
        response = await async_client.transcriptions.with_raw_response.create(
            language="yo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(object, transcription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSpitch) -> None:
        async with async_client.transcriptions.with_streaming_response.create(
            language="yo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(object, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True
