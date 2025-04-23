# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import speech_generate_params, speech_transcribe_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.speech_transcribe_response import SpeechTranscribeResponse

__all__ = ["SpeechResource", "AsyncSpeechResource"]


class SpeechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/spi-tch/spitch-python#accessing-raw-response-data-eg-headers
        """
        return SpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/spi-tch/spitch-python#with_streaming_response
        """
        return SpeechResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig", "am"],
        text: str,
        voice: Literal[
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
        ],
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Synthesize

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "audio/wav", **(extra_headers or {})}
        return self._post(
            "/v1/speech",
            body=maybe_transform(
                {
                    "language": language,
                    "text": text,
                    "voice": voice,
                },
                speech_generate_params.SpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, speech_generate_params.SpeechGenerateParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def transcribe(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig", "am"],
        content: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        multispeaker: Optional[bool] | NotGiven = NOT_GIVEN,
        timestamp: Optional[bool] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpeechTranscribeResponse:
        """
        Transcribe

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "language": language,
                "content": content,
                "multispeaker": multispeaker,
                "timestamp": timestamp,
                "url": url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/transcriptions",
            body=maybe_transform(body, speech_transcribe_params.SpeechTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechTranscribeResponse,
        )


class AsyncSpeechResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/spi-tch/spitch-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/spi-tch/spitch-python#with_streaming_response
        """
        return AsyncSpeechResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig", "am"],
        text: str,
        voice: Literal[
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
        ],
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Synthesize

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "audio/wav", **(extra_headers or {})}
        return await self._post(
            "/v1/speech",
            body=await async_maybe_transform(
                {
                    "language": language,
                    "text": text,
                    "voice": voice,
                },
                speech_generate_params.SpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"stream": stream}, speech_generate_params.SpeechGenerateParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def transcribe(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig", "am"],
        content: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        multispeaker: Optional[bool] | NotGiven = NOT_GIVEN,
        timestamp: Optional[bool] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpeechTranscribeResponse:
        """
        Transcribe

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "language": language,
                "content": content,
                "multispeaker": multispeaker,
                "timestamp": timestamp,
                "url": url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/transcriptions",
            body=await async_maybe_transform(body, speech_transcribe_params.SpeechTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechTranscribeResponse,
        )


class SpeechResourceWithRawResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.generate = to_custom_raw_response_wrapper(
            speech.generate,
            BinaryAPIResponse,
        )
        self.transcribe = to_raw_response_wrapper(
            speech.transcribe,
        )


class AsyncSpeechResourceWithRawResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.generate = async_to_custom_raw_response_wrapper(
            speech.generate,
            AsyncBinaryAPIResponse,
        )
        self.transcribe = async_to_raw_response_wrapper(
            speech.transcribe,
        )


class SpeechResourceWithStreamingResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.generate = to_custom_streamed_response_wrapper(
            speech.generate,
            StreamedBinaryAPIResponse
        )
        self.transcribe = to_streamed_response_wrapper(
            speech.transcribe,
        )


class AsyncSpeechResourceWithStreamingResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.generate = async_to_custom_streamed_response_wrapper(
            speech.generate,
            AsyncStreamedBinaryAPIResponse
        )
        self.transcribe = async_to_streamed_response_wrapper(
            speech.transcribe,
        )
