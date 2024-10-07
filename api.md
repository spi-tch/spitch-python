# Speech

Types:

```python
from spitch.types import SpeechGenerateResponse, SpeechTranscibeResponse
```

Methods:

- <code title="post /v1/speech">client.speech.<a href="./src/spitch/resources/speech.py">generate</a>(\*\*<a href="src/spitch/types/speech_generate_params.py">params</a>) -> <a href="./src/spitch/types/speech_generate_response.py">object</a></code>
- <code title="post /v1/transcriptions">client.speech.<a href="./src/spitch/resources/speech.py">transcibe</a>(\*\*<a href="src/spitch/types/speech_transcibe_params.py">params</a>) -> <a href="./src/spitch/types/speech_transcibe_response.py">object</a></code>

# Text

Types:

```python
from spitch.types import TextToneMarkResponse
```

Methods:

- <code title="post /v1/diacritics">client.text.<a href="./src/spitch/resources/text.py">tone_mark</a>(\*\*<a href="src/spitch/types/text_tone_mark_params.py">params</a>) -> <a href="./src/spitch/types/text_tone_mark_response.py">object</a></code>
