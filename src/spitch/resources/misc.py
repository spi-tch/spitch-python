# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["MiscResource", "AsyncMiscResource"]


class MiscResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MiscResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/spi-tch/spitch-python#accessing-raw-response-data-eg-headers
        """
        return MiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiscResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/spi-tch/spitch-python#with_streaming_response
        """
        return MiscResourceWithStreamingResponse(self)

    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Ping"""
        return self._get(
            "/v1/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMiscResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMiscResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/spi-tch/spitch-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiscResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/spi-tch/spitch-python#with_streaming_response
        """
        return AsyncMiscResourceWithStreamingResponse(self)

    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Ping"""
        return await self._get(
            "/v1/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MiscResourceWithRawResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

        self.ping = to_raw_response_wrapper(
            misc.ping,
        )


class AsyncMiscResourceWithRawResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

        self.ping = async_to_raw_response_wrapper(
            misc.ping,
        )


class MiscResourceWithStreamingResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

        self.ping = to_streamed_response_wrapper(
            misc.ping,
        )


class AsyncMiscResourceWithStreamingResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

        self.ping = async_to_streamed_response_wrapper(
            misc.ping,
        )
