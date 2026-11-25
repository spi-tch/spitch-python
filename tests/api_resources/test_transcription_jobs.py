from __future__ import annotations

import httpx
import pytest

from spitch import Spitch, AsyncSpitch


@pytest.mark.parametrize("terminal", ["succeeded", "failed"])
def test_resume_by_id(terminal: str) -> None:
    calls: list[str] = []
    states = iter(["queued", "processing", terminal])

    def respond(request: httpx.Request) -> httpx.Response:
        calls.append(request.method)
        if request.method == "POST":
            assert request.url.params["async"] == "true"
            assert b'name="url"' in request.read()
        else:
            assert request.url.path == "/v1/transcriptions/demo"
        return httpx.Response(
            200,
            json={"id": "demo", "status": next(states), "created_at": "now", "polling_url": "/v1/transcriptions/demo"},
        )

    with Spitch(api_key="demo", http_client=httpx.Client(transport=httpx.MockTransport(respond))) as client:
        accepted = client.speech.submit_transcription(url="https://example.org/audio.wav")
        assert client.speech.wait_for_transcription(accepted.id, poll_interval=0.001).status == terminal
    assert calls == ["POST", "GET", "GET"]


async def test_async_poll_deadline() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        return httpx.Response(
            200,
            json={"id": "demo", "status": "processing", "created_at": "now", "polling_url": "/v1/transcriptions/demo"},
        )

    async with AsyncSpitch(
        api_key="demo", http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond))
    ) as client:
        assert (await client.speech.get_transcription("demo")).status == "processing"
        with pytest.raises(TimeoutError):
            await client.speech.wait_for_transcription("demo", timeout=0.02)


async def test_async_upload_and_read_raw_response() -> None:
    calls: list[str] = []

    def respond(request: httpx.Request) -> httpx.Response:
        calls.append(request.method)
        if request.method == "POST":
            assert request.url.params["async"] == "true"
            assert b'filename="clip.wav"' in request.read()
        return httpx.Response(
            200,
            json={
                "id": "demo",
                "status": "succeeded",
                "created_at": "now",
                "polling_url": "/v1/transcriptions/demo",
                "result": {"text": "hello"},
            },
        )

    async with AsyncSpitch(
        api_key="demo", http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond))
    ) as client:
        accepted = await client.speech.with_raw_response.submit_transcription(
            content=("clip.wav", b"audio", "audio/wav")
        )
        job = await accepted.parse()
        result = await client.speech.wait_for_transcription(job.id)
        assert result.result is not None and result.result.text == "hello"
    assert calls == ["POST", "GET"]
