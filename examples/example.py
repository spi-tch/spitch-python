#!/usr/bin/env -S rye run python
import os
import time
from pathlib import Path

from spitch import Spitch

client = Spitch(api_key=os.getenv('SPITCH_API_KEY'))
speech_file_path = Path(__file__).parent / "speech.mp3"


def main():
    start_time = time.time()
    with client.speech.with_streaming_response.generate(
        language="yo",
        text="Bawo ni ololufe?"
    ) as speech:
        print(f"Time to first byte: {int((time.time() - start_time) * 1000)}ms")
        speech.stream_to_file(speech_file_path)


if __name__ == "__main__":
    main()
