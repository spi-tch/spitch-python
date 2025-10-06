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

# Files

Types:

```python
from spitch.types import FileListResponse, FileGetResponse
```

Methods:

- <code title="get /v1/files">client.files.<a href="./src/spitch/resources/files.py">list</a>(\*\*<a href="src/spitch/types/file_list_params.py">params</a>) -> <a href="./src/spitch/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/spitch/resources/files.py">delete</a>(file_id) -> object</code>
- <code title="get /v1/files/{file_id}/url">client.files.<a href="./src/spitch/resources/files.py">download</a>(file_id, \*\*<a href="src/spitch/types/file_download_params.py">params</a>) -> object</code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/spitch/resources/files.py">get</a>(file_id) -> <a href="./src/spitch/types/file_get_response.py">FileGetResponse</a></code>
- <code title="post /v1/files">client.files.<a href="./src/spitch/resources/files.py">upload</a>(\*\*<a href="src/spitch/types/file_upload_params.py">params</a>) -> object</code>
- <code title="get /v1/files:usage">client.files.<a href="./src/spitch/resources/files.py">usage</a>() -> object</code>
