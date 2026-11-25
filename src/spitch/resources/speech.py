# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import math
import time
from typing import Union, Optional
from urllib.parse import quote
from typing_extensions import Literal

import anyio
import httpx

from ..types import speech_generate_params, speech_transcribe_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, async_maybe_transform
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
from .._exceptions import APITimeoutError
from .._base_client import make_request_options
from ..types.transcription import Transcription
from ..types.transcription_job import TranscriptionJob

__all__ = ["SpeechResource", "AsyncSpeechResource"]


def _transcription_source(content: FileTypes | str | Omit, url: str | Omit) -> dict[str, object]:
    if isinstance(content, Omit) == isinstance(url, Omit):
        raise ValueError("Supply exactly one audio source: content for a file or url for a public audio URL.")
    if not isinstance(content, (Omit, str)):
        return {"content": content}
    address = content if isinstance(content, str) else url
    if not isinstance(address, str) or not address.strip():
        raise ValueError("Supply a public HTTP(S) audio URL in url.")
    parsed = httpx.URL(address)
    if parsed.scheme not in {"http", "https"} or not parsed.host:
        raise ValueError("Supply a public HTTP(S) audio URL in url.")
    return {"url": address}


def _job_path(job_id: str) -> str:
    if not job_id or job_id in {".", ".."}:
        raise ValueError("Provide a transcription job ID.")
    return "/v1/transcriptions/" + quote(job_id, safe="")


def _deadline(timeout: float, poll_interval: float) -> float:
    if not all(math.isfinite(value) and value > 0 for value in (timeout, poll_interval)):
        raise ValueError("timeout and poll_interval must be positive and finite.")
    return time.monotonic() + timeout


def _remaining(deadline: float, job_id: str) -> float:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise TimeoutError(f"Timed out waiting for transcription {job_id}. Resume with the same job ID.")
    return remaining


def _transcription_body(
    content: FileTypes | str | Omit,
    url: str | Omit,
    language: str | None | Omit,
    model: str | None | Omit,
    special_words: str | None | Omit,
    timestamp: str | None | Omit,
) -> dict[str, object]:
    return {
        **_transcription_source(content, url),
        "language": language,
        "model": model,
        "special_words": special_words,
        "timestamp": timestamp,
    }


class SpeechResource(SyncAPIResource):
    """All speech-focused APIs (TTS and STT)"""

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
        ],
        format: Literal["mp3", "wav", "ogg_opus", "webm_opus", "mulaw", "alaw", "flac", "pcm_s16le"] | Omit = omit,
        language: str | Omit = omit,
        speed: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Generate audio

        Args:
          text: The text for which you want to generate audio.

          voice: The voice you want to be used for audio generation.

          format: The audio format for the returned audio data, defaults to `wav`.

          language: This is optional; an ISO 639 language code to be used for the generation.

          speed: The speed of the voice, defaults to `1.0`

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
                    "text": text,
                    "voice": voice,
                    "format": format,
                    "language": language,
                    "speed": speed,
                },
                speech_generate_params.SpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def transcribe(
        self,
        *,
        content: Union[FileTypes, str] | Omit = omit,
        url: str | Omit = omit,
        language: Optional[str] | Omit = omit,
        model: Optional[Literal["mansa_v1", "legacy"]] | Omit = omit,
        special_words: Optional[str] | Omit = omit,
        timestamp: Optional[Literal["sentence", "word"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transcription:
        """Convert speech to text.

        Upload audio file containing speech and get back text
        that represents the content of the audio file.

        Args:
          content: Audio to upload. Supply exactly one of content or url.

          url: Public HTTP(S) URL of the recording.

          language: This is optional, an ISO-639 language code that corresponds to the language in
              the `content`.

          model: Select the model to be used to perform the transcription, this param has been
              deprecated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = _transcription_body(content, url, language, model, special_words, timestamp)
        files = extract_files(body, paths=[["content"]])
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
            cast_to=Transcription,
        )

    def submit_transcription(
        self,
        *,
        content: Union[FileTypes, str] | Omit = omit,
        url: str | Omit = omit,
        language: Optional[str] | Omit = omit,
        model: Optional[Literal["mansa_v1", "legacy"]] | Omit = omit,
        special_words: Optional[str] | Omit = omit,
        timestamp: Optional[Literal["sentence", "word"]] | Omit = omit,
        extra_headers: Headers | None = None,
    ) -> TranscriptionJob:
        """Submit one background job. Save the returned ID to resume later."""
        body = _transcription_body(content, url, language, model, special_words, timestamp)
        files = extract_files(body, paths=[["content"]])
        # The API creates a new job for each POST. Never replay an ambiguous submission.
        return self._post(
            "/v1/transcriptions",
            body=maybe_transform(body, speech_transcribe_params.SpeechTranscribeParams),
            files=files,
            options={
                "headers": {"Content-Type": "multipart/form-data", **(extra_headers or {})},
                "params": {"async": "true"},
                "max_retries": 0,
            },
            cast_to=TranscriptionJob,
        )

    def get_transcription(self, job_id: str, *, extra_headers: Headers | None = None) -> TranscriptionJob:
        """Read the current state, transcript or failure for a saved job ID."""
        return self._get(
            _job_path(job_id), cast_to=TranscriptionJob, options=make_request_options(extra_headers=extra_headers)
        )

    def wait_for_transcription(
        self, job_id: str, *, timeout: float = 300, poll_interval: float = 2
    ) -> TranscriptionJob:
        """Poll by ID until succeeded or failed. Both timing arguments are in seconds."""
        path = _job_path(job_id)
        deadline = _deadline(timeout, poll_interval)
        while True:
            remaining = _remaining(deadline, job_id)
            try:
                job = self._get(path, cast_to=TranscriptionJob, options={"timeout": remaining, "max_retries": 0})
            except APITimeoutError as exc:
                raise TimeoutError(
                    f"Timed out waiting for transcription {job_id}. Resume with the same job ID."
                ) from exc
            remaining = _remaining(deadline, job_id)
            if job.status in ("succeeded", "failed"):
                return job
            self._sleep(min(poll_interval, remaining))


class AsyncSpeechResource(AsyncAPIResource):
    """All speech-focused APIs (TTS and STT)"""

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
        ],
        format: Literal["mp3", "wav", "ogg_opus", "webm_opus", "mulaw", "alaw", "flac", "pcm_s16le"] | Omit = omit,
        language: str | Omit = omit,
        speed: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Generate audio

        Args:
          text: The text for which you want to generate audio.

          voice: The voice you want to be used for audio generation.

          format: The audio format for the returned audio data, defaults to `wav`.

          language: This is optional; an ISO 639 language code to be used for the generation.

          speed: The speed of the voice, defaults to `1.0`

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
                    "text": text,
                    "voice": voice,
                    "format": format,
                    "language": language,
                    "speed": speed,
                },
                speech_generate_params.SpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def transcribe(
        self,
        *,
        content: Union[FileTypes, str] | Omit = omit,
        url: str | Omit = omit,
        language: Optional[str] | Omit = omit,
        model: Optional[Literal["mansa_v1", "legacy"]] | Omit = omit,
        special_words: Optional[str] | Omit = omit,
        timestamp: Optional[Literal["sentence", "word"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transcription:
        """Convert speech to text.

        Upload audio file containing speech and get back text
        that represents the content of the audio file.

        Args:
          content: Audio to upload. Supply exactly one of content or url.

          url: Public HTTP(S) URL of the recording.

          language: This is optional, an ISO-639 language code that corresponds to the language in
              the `content`.

          model: Select the model to be used to perform the transcription, this param has been
              deprecated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = _transcription_body(content, url, language, model, special_words, timestamp)
        files = extract_files(body, paths=[["content"]])
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
            cast_to=Transcription,
        )

    async def submit_transcription(
        self,
        *,
        content: Union[FileTypes, str] | Omit = omit,
        url: str | Omit = omit,
        language: Optional[str] | Omit = omit,
        model: Optional[Literal["mansa_v1", "legacy"]] | Omit = omit,
        special_words: Optional[str] | Omit = omit,
        timestamp: Optional[Literal["sentence", "word"]] | Omit = omit,
        extra_headers: Headers | None = None,
    ) -> TranscriptionJob:
        """Submit one background job. Save the returned ID to resume later."""
        body = _transcription_body(content, url, language, model, special_words, timestamp)
        files = extract_files(body, paths=[["content"]])
        # The API creates a new job for each POST. Never replay an ambiguous submission.
        return await self._post(
            "/v1/transcriptions",
            body=await async_maybe_transform(body, speech_transcribe_params.SpeechTranscribeParams),
            files=files,
            options={
                "headers": {"Content-Type": "multipart/form-data", **(extra_headers or {})},
                "params": {"async": "true"},
                "max_retries": 0,
            },
            cast_to=TranscriptionJob,
        )

    async def get_transcription(self, job_id: str, *, extra_headers: Headers | None = None) -> TranscriptionJob:
        """Read the current state, transcript or failure for a saved job ID."""
        return await self._get(
            _job_path(job_id), cast_to=TranscriptionJob, options=make_request_options(extra_headers=extra_headers)
        )

    async def wait_for_transcription(
        self, job_id: str, *, timeout: float = 300, poll_interval: float = 2
    ) -> TranscriptionJob:
        """Poll by ID until succeeded or failed. Both timing arguments are in seconds."""
        path = _job_path(job_id)
        deadline = _deadline(timeout, poll_interval)
        with anyio.fail_after(timeout):
            while True:
                remaining = _remaining(deadline, job_id)
                try:
                    job = await self._get(
                        path, cast_to=TranscriptionJob, options={"timeout": remaining, "max_retries": 0}
                    )
                except APITimeoutError as exc:
                    raise TimeoutError(
                        f"Timed out waiting for transcription {job_id}. Resume with the same job ID."
                    ) from exc
                remaining = _remaining(deadline, job_id)
                if job.status in ("succeeded", "failed"):
                    return job
                await self._sleep(min(poll_interval, remaining))


class SpeechResourceWithRawResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.generate = to_custom_raw_response_wrapper(
            speech.generate,
            BinaryAPIResponse,
        )
        self.submit_transcription = to_raw_response_wrapper(speech.submit_transcription)
        self.get_transcription = to_raw_response_wrapper(speech.get_transcription)
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
        self.submit_transcription = async_to_raw_response_wrapper(speech.submit_transcription)
        self.get_transcription = async_to_raw_response_wrapper(speech.get_transcription)
        self.transcribe = async_to_raw_response_wrapper(
            speech.transcribe,
        )


class SpeechResourceWithStreamingResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.generate = to_custom_streamed_response_wrapper(
            speech.generate,
            StreamedBinaryAPIResponse,
        )
        self.submit_transcription = to_streamed_response_wrapper(speech.submit_transcription)
        self.get_transcription = to_streamed_response_wrapper(speech.get_transcription)
        self.transcribe = to_streamed_response_wrapper(
            speech.transcribe,
        )


class AsyncSpeechResourceWithStreamingResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.generate = async_to_custom_streamed_response_wrapper(
            speech.generate,
            AsyncStreamedBinaryAPIResponse,
        )
        self.submit_transcription = async_to_streamed_response_wrapper(speech.submit_transcription)
        self.get_transcription = async_to_streamed_response_wrapper(speech.get_transcription)
        self.transcribe = async_to_streamed_response_wrapper(
            speech.transcribe,
        )
