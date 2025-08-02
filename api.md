# Speech

Types:

```python
from spitch.types import SpeechTranscribeResponse
```

Methods:

- <code title="post /v1/speech">client.speech.<a href="./src/spitch/resources/speech.py">generate</a>(\*\*<a href="src/spitch/types/speech_generate_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/transcriptions">client.speech.<a href="./src/spitch/resources/speech.py">transcribe</a>(\*\*<a href="src/spitch/types/speech_transcribe_params.py">params</a>) -> <a href="./src/spitch/types/speech_transcribe_response.py">SpeechTranscribeResponse</a></code>

# Text

Types:

```python
from spitch.types import TextToneMarkResponse, TextTranslateResponse
```

Methods:

- <code title="post /v1/diacritics">client.text.<a href="./src/spitch/resources/text.py">tone_mark</a>(\*\*<a href="src/spitch/types/text_tone_mark_params.py">params</a>) -> <a href="./src/spitch/types/text_tone_mark_response.py">TextToneMarkResponse</a></code>
- <code title="post /v1/translate">client.text.<a href="./src/spitch/resources/text.py">translate</a>(\*\*<a href="src/spitch/types/text_translate_params.py">params</a>) -> <a href="./src/spitch/types/text_translate_response.py">TextTranslateResponse</a></code>
