# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import speech_get_params, speech_generate_params, speech_transcibe_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["SpeechResource", "AsyncSpeechResource"]


class SpeechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        language: Literal["yo", "en", "ha", "ig"],
        text: str,
        stream: bool | NotGiven = NOT_GIVEN,
        voice: Literal["sade", "segun", "femi", "funmi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Synthesize

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            cast_to=object,
        )

    def get(
        self,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Speech

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/speech",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"file_id": file_id}, speech_get_params.SpeechGetParams),
            ),
            cast_to=object,
        )

    def transcibe(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig"],
        content: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Transcribe

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/transcriptions",
            body=maybe_transform(
                {
                    "language": language,
                    "content": content,
                    "url": url,
                },
                speech_transcibe_params.SpeechTranscibeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSpeechResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        language: Literal["yo", "en", "ha", "ig"],
        text: str,
        stream: bool | NotGiven = NOT_GIVEN,
        voice: Literal["sade", "segun", "femi", "funmi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Synthesize

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            cast_to=object,
        )

    async def get(
        self,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Speech

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/speech",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"file_id": file_id}, speech_get_params.SpeechGetParams),
            ),
            cast_to=object,
        )

    async def transcibe(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig"],
        content: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Transcribe

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/transcriptions",
            body=await async_maybe_transform(
                {
                    "language": language,
                    "content": content,
                    "url": url,
                },
                speech_transcibe_params.SpeechTranscibeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SpeechResourceWithRawResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.generate = to_raw_response_wrapper(
            speech.generate,
        )
        self.get = to_raw_response_wrapper(
            speech.get,
        )
        self.transcibe = to_raw_response_wrapper(
            speech.transcibe,
        )


class AsyncSpeechResourceWithRawResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.generate = async_to_raw_response_wrapper(
            speech.generate,
        )
        self.get = async_to_raw_response_wrapper(
            speech.get,
        )
        self.transcibe = async_to_raw_response_wrapper(
            speech.transcibe,
        )


class SpeechResourceWithStreamingResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.generate = to_streamed_response_wrapper(
            speech.generate,
        )
        self.get = to_streamed_response_wrapper(
            speech.get,
        )
        self.transcibe = to_streamed_response_wrapper(
            speech.transcibe,
        )


class AsyncSpeechResourceWithStreamingResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.generate = async_to_streamed_response_wrapper(
            speech.generate,
        )
        self.get = async_to_streamed_response_wrapper(
            speech.get,
        )
        self.transcibe = async_to_streamed_response_wrapper(
            speech.transcibe,
        )
