# Speech

Types:

```python
from spitch.types import SpeechGenerateResponse, SpeechGetResponse, SpeechTranscibeResponse
```

Methods:

- <code title="post /v1/speech">client.speech.<a href="./src/spitch/resources/speech.py">generate</a>(\*\*<a href="src/spitch/types/speech_generate_params.py">params</a>) -> <a href="./src/spitch/types/speech_generate_response.py">object</a></code>
- <code title="get /v1/speech">client.speech.<a href="./src/spitch/resources/speech.py">get</a>(\*\*<a href="src/spitch/types/speech_get_params.py">params</a>) -> <a href="./src/spitch/types/speech_get_response.py">object</a></code>
- <code title="post /v1/transcriptions">client.speech.<a href="./src/spitch/resources/speech.py">transcibe</a>(\*\*<a href="src/spitch/types/speech_transcibe_params.py">params</a>) -> <a href="./src/spitch/types/speech_transcibe_response.py">object</a></code>

# Text

Types:

```python
from spitch.types import TextToneMarkResponse
```

Methods:

- <code title="post /v1/diacritics">client.text.<a href="./src/spitch/resources/text.py">tone_mark</a>(\*\*<a href="src/spitch/types/text_tone_mark_params.py">params</a>) -> <a href="./src/spitch/types/text_tone_mark_response.py">object</a></code>

# Misc

Types:

```python
from spitch.types import MiscPingResponse
```

Methods:

- <code title="get /v1/ping">client.misc.<a href="./src/spitch/resources/misc.py">ping</a>() -> <a href="./src/spitch/types/misc_ping_response.py">object</a></code>
