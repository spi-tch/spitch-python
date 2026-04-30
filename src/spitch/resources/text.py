# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import text_tone_mark_params, text_translate_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.diacritics import Diacritics
from ..types.translation import Translation

__all__ = ["TextResource", "AsyncTextResource"]


class TextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        language: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Diacritics:
        """
        Add appropriate tone marks to text.

        Args:
          language: Only Yoruba is supported at the moment.

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
            cast_to=Diacritics,
        )

    def translate(
        self,
        *,
        target: str,
        text: str,
        formality: Literal["casual", "formal"] | Omit = omit,
        source: Optional[str] | Omit = omit,
        tone: Literal["neutral", "warm", "professional", "narration"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Translation:
        """Translate text from one language to another.

        Select the source and target
        languages, and get text in new language.

        Args:
          target: An ISO 639 code of the language you want to translate to.

          text: The text to be translated.

          formality: Whether to be `formal` or `casual`.

          source: An ISO 639 code of the language you're translating from

          tone: The tone of the translated text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/translate",
            body=maybe_transform(
                {
                    "target": target,
                    "text": text,
                    "formality": formality,
                    "source": source,
                    "tone": tone,
                },
                text_translate_params.TextTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Translation,
        )


class AsyncTextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        language: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Diacritics:
        """
        Add appropriate tone marks to text.

        Args:
          language: Only Yoruba is supported at the moment.

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
            cast_to=Diacritics,
        )

    async def translate(
        self,
        *,
        target: str,
        text: str,
        formality: Literal["casual", "formal"] | Omit = omit,
        source: Optional[str] | Omit = omit,
        tone: Literal["neutral", "warm", "professional", "narration"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Translation:
        """Translate text from one language to another.

        Select the source and target
        languages, and get text in new language.

        Args:
          target: An ISO 639 code of the language you want to translate to.

          text: The text to be translated.

          formality: Whether to be `formal` or `casual`.

          source: An ISO 639 code of the language you're translating from

          tone: The tone of the translated text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/translate",
            body=await async_maybe_transform(
                {
                    "target": target,
                    "text": text,
                    "formality": formality,
                    "source": source,
                    "tone": tone,
                },
                text_translate_params.TextTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Translation,
        )


class TextResourceWithRawResponse:
    def __init__(self, text: TextResource) -> None:
        self._text = text

        self.tone_mark = to_raw_response_wrapper(
            text.tone_mark,
        )
        self.translate = to_raw_response_wrapper(
            text.translate,
        )


class AsyncTextResourceWithRawResponse:
    def __init__(self, text: AsyncTextResource) -> None:
        self._text = text

        self.tone_mark = async_to_raw_response_wrapper(
            text.tone_mark,
        )
        self.translate = async_to_raw_response_wrapper(
            text.translate,
        )


class TextResourceWithStreamingResponse:
    def __init__(self, text: TextResource) -> None:
        self._text = text

        self.tone_mark = to_streamed_response_wrapper(
            text.tone_mark,
        )
        self.translate = to_streamed_response_wrapper(
            text.translate,
        )


class AsyncTextResourceWithStreamingResponse:
    def __init__(self, text: AsyncTextResource) -> None:
        self._text = text

        self.tone_mark = async_to_streamed_response_wrapper(
            text.tone_mark,
        )
        self.translate = async_to_streamed_response_wrapper(
            text.translate,
        )
