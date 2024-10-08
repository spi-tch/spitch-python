# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import text_tone_mark_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["TextResource", "AsyncTextResource"]


class TextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/spi-tch/spitch-python#accessing-raw-response-data-eg-headers
        """
        return TextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/spi-tch/spitch-python#with_streaming_response
        """
        return TextResourceWithStreamingResponse(self)

    def tone_mark(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig"],
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Tone Mark

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/diacritics",
            body=maybe_transform(
                {
                    "language": language,
                    "text": text,
                },
                text_tone_mark_params.TextToneMarkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/spi-tch/spitch-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/spi-tch/spitch-python#with_streaming_response
        """
        return AsyncTextResourceWithStreamingResponse(self)

    async def tone_mark(
        self,
        *,
        language: Literal["yo", "en", "ha", "ig"],
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Tone Mark

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/diacritics",
            body=await async_maybe_transform(
                {
                    "language": language,
                    "text": text,
                },
                text_tone_mark_params.TextToneMarkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TextResourceWithRawResponse:
    def __init__(self, text: TextResource) -> None:
        self._text = text

        self.tone_mark = to_raw_response_wrapper(
            text.tone_mark,
        )


class AsyncTextResourceWithRawResponse:
    def __init__(self, text: AsyncTextResource) -> None:
        self._text = text

        self.tone_mark = async_to_raw_response_wrapper(
            text.tone_mark,
        )


class TextResourceWithStreamingResponse:
    def __init__(self, text: TextResource) -> None:
        self._text = text

        self.tone_mark = to_streamed_response_wrapper(
            text.tone_mark,
        )


class AsyncTextResourceWithStreamingResponse:
    def __init__(self, text: AsyncTextResource) -> None:
        self._text = text

        self.tone_mark = async_to_streamed_response_wrapper(
            text.tone_mark,
        )
