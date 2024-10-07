#!/usr/bin/env -S rye run python
import os

from spitch import Spitch

client = Spitch(api_key=os.getenv('SPITCH_API_KEY'))
transcription = client.speech.generate(
    language="yo",
    text="Bawo ni ololufe?"
)
