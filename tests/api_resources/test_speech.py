# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from spitch import Spitch, AsyncSpitch
from tests.utils import assert_matches_type
from spitch.types import Transcription
from spitch._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate(self, client: Spitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.speech.generate(
            language="yo",
            text="text",
            voice="sade",
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate_with_all_params(self, client: Spitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.speech.generate(
            language="yo",
            text="text",
            voice="sade",
            format="wav",
            model="legacy",
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_generate(self, client: Spitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = client.speech.with_raw_response.generate(
            language="yo",
            text="text",
            voice="sade",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert speech.json() == {"foo": "bar"}
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_generate(self, client: Spitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.speech.with_streaming_response.generate(
            language="yo",
            text="text",
            voice="sade",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, StreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True

    @parametrize
    def test_method_transcribe(self, client: Spitch) -> None:
        speech = client.speech.transcribe(
            language="yo",
        )
        assert_matches_type(Transcription, speech, path=["response"])

    @parametrize
    def test_method_transcribe_with_all_params(self, client: Spitch) -> None:
        speech = client.speech.transcribe(
            language="yo",
            content=b"raw file contents",
            model="mansa_v1",
            special_words="special_words",
            timestamp="sentence",
            url="url",
        )
        assert_matches_type(Transcription, speech, path=["response"])

    @parametrize
    def test_raw_response_transcribe(self, client: Spitch) -> None:
        response = client.speech.with_raw_response.transcribe(
            language="yo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = response.parse()
        assert_matches_type(Transcription, speech, path=["response"])

    @parametrize
    def test_streaming_response_transcribe(self, client: Spitch) -> None:
        with client.speech.with_streaming_response.transcribe(
            language="yo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = response.parse()
            assert_matches_type(Transcription, speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate(self, async_client: AsyncSpitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.speech.generate(
            language="yo",
            text="text",
            voice="sade",
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate_with_all_params(self, async_client: AsyncSpitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.speech.generate(
            language="yo",
            text="text",
            voice="sade",
            format="wav",
            model="legacy",
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_generate(self, async_client: AsyncSpitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = await async_client.speech.with_raw_response.generate(
            language="yo",
            text="text",
            voice="sade",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await speech.json() == {"foo": "bar"}
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_generate(self, async_client: AsyncSpitch, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.speech.with_streaming_response.generate(
            language="yo",
            text="text",
            voice="sade",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True

    @parametrize
    async def test_method_transcribe(self, async_client: AsyncSpitch) -> None:
        speech = await async_client.speech.transcribe(
            language="yo",
        )
        assert_matches_type(Transcription, speech, path=["response"])

    @parametrize
    async def test_method_transcribe_with_all_params(self, async_client: AsyncSpitch) -> None:
        speech = await async_client.speech.transcribe(
            language="yo",
            content=b"raw file contents",
            model="mansa_v1",
            special_words="special_words",
            timestamp="sentence",
            url="url",
        )
        assert_matches_type(Transcription, speech, path=["response"])

    @parametrize
    async def test_raw_response_transcribe(self, async_client: AsyncSpitch) -> None:
        response = await async_client.speech.with_raw_response.transcribe(
            language="yo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = await response.parse()
        assert_matches_type(Transcription, speech, path=["response"])

    @parametrize
    async def test_streaming_response_transcribe(self, async_client: AsyncSpitch) -> None:
        async with async_client.speech.with_streaming_response.transcribe(
            language="yo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = await response.parse()
            assert_matches_type(Transcription, speech, path=["response"])

        assert cast(Any, response.is_closed) is True
