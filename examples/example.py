#!/usr/bin/env -S rye run python

from spitch import Spitch

client = Spitch(
    client_id="My Client ID",
    client_secret="My Client Secret",
    token_url="My Token URL",
)
transcription = client.transcriptions.create(
    language="yo",
)
print(transcription)
