import json
import runpy
from pathlib import Path

import httpx
import respx
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("starter", ["first_request.py", "first_request_async.py"])
def test_first_request_writes_wav_and_prints_response_id(
    starter: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    respx_mock: respx.MockRouter,
) -> None:
    audio = (ROOT / "scripts" / "fixtures" / "silence.wav").read_bytes()
    route = respx_mock.post("https://starter.test/v1/speech").mock(
        return_value=httpx.Response(
            200, headers={"Content-Type": "audio/wav", "X-Request-Id": "demo-response-id"}, content=audio
        )
    )
    monkeypatch.setenv("SPITCH_BASE_URL", "https://starter.test")
    monkeypatch.setenv("SPITCH_API_KEY", "fixture-key")
    monkeypatch.chdir(tmp_path)

    runpy.run_path(str(ROOT / "examples" / starter), run_name="__main__")

    assert route.call_count == 1
    assert json.loads(route.calls.last.request.content) == {
        "text": "Nnọọ na Spitch. Ọ dị ezigbo mma inwe gị ebe a.",
        "voice": "ngozi",
        "language": "ig",
        "format": "wav",
    }
    assert (tmp_path / "hello.wav").read_bytes() == audio
    assert capsys.readouterr().out.splitlines() == ["Saved hello.wav", "Request ID: demo-response-id"]
