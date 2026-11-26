from __future__ import annotations

import asyncio

import httpx
import pytest

from spitch import AsyncSpitch, APIStatusError
from examples.rate_limited_batch import read_file


@pytest.mark.parametrize(
    ("statuses", "advice", "message"),
    [
        ([429, 200], "0", ""),
        ([429, 429, 429], "0", "attempts exhausted"),
        ([429], None, "No usable Retry-After"),
        ([429], "bad", "No usable Retry-After"),
        ([429], "90", "remaining file budget"),
        ([402], "0", ""),
    ],
)
def test_batch_retry_policy(
    statuses: list[int], advice: str | None, message: str, capsys: pytest.CaptureFixture[str]
) -> None:
    responses = iter(statuses)
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.method)
        status = next(responses)
        headers = {"RateLimit-Limit": "60", "RateLimit-Remaining": "0", "RateLimit-Reset": "2"}
        if advice is not None:
            headers["Retry-After"] = advice
        data = {"file_id": "demo", "status": "ready", "created_at": "2026-11-26T09:00:00Z"}
        return httpx.Response(status, headers=headers, json=data if status == 200 else {"detail": "fixture"})

    async def run() -> None:
        transport = httpx.MockTransport(handler)
        async with AsyncSpitch(
            api_key="demo", max_retries=0, http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            if message:
                with pytest.raises(RuntimeError, match=message):
                    await read_file(client, "demo")
            elif statuses == [402]:
                with pytest.raises(APIStatusError) as raised:
                    await read_file(client, "demo")
                assert raised.value.status_code == 402
            else:
                assert (await read_file(client, "demo")).file_id == "demo"

    asyncio.run(run())
    assert calls == ["GET"] * len(statuses)
    if statuses[0] == 429:
        output = capsys.readouterr().err
        assert "RateLimit-Remaining: 0" in output
        if advice is not None:
            assert f"Retry-After: {advice}" in output
