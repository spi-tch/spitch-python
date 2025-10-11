# Speech

Types:

```python
from spitch.types import Transcription
```

Methods:

- <code title="post /v1/speech">client.speech.<a href="./src/spitch/resources/speech.py">generate</a>(\*\*<a href="src/spitch/types/speech_generate_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/transcriptions">client.speech.<a href="./src/spitch/resources/speech.py">transcribe</a>(\*\*<a href="src/spitch/types/speech_transcribe_params.py">params</a>) -> <a href="./src/spitch/types/transcription.py">Transcription</a></code>

# Text

Types:

```python
from spitch.types import Diacritics, Translation
```

Methods:

- <code title="post /v1/diacritics">client.text.<a href="./src/spitch/resources/text.py">tone_mark</a>(\*\*<a href="src/spitch/types/text_tone_mark_params.py">params</a>) -> <a href="./src/spitch/types/diacritics.py">Diacritics</a></code>
- <code title="post /v1/translate">client.text.<a href="./src/spitch/resources/text.py">translate</a>(\*\*<a href="src/spitch/types/text_translate_params.py">params</a>) -> <a href="./src/spitch/types/translation.py">Translation</a></code>

# Files

Types:

```python
from spitch.types import File, FileUsage, Files, FileDownloadResponse
```

Methods:

- <code title="get /v1/files">client.files.<a href="./src/spitch/resources/files.py">list</a>(\*\*<a href="src/spitch/types/file_list_params.py">params</a>) -> <a href="./src/spitch/types/file.py">SyncFilesCursor[File]</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/spitch/resources/files.py">delete</a>(file_id) -> object</code>
- <code title="get /v1/files/{file_id}/url">client.files.<a href="./src/spitch/resources/files.py">download</a>(file_id, \*\*<a href="src/spitch/types/file_download_params.py">params</a>) -> <a href="./src/spitch/types/file_download_response.py">FileDownloadResponse</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/spitch/resources/files.py">get</a>(file_id) -> <a href="./src/spitch/types/file.py">File</a></code>
- <code title="post /v1/files">client.files.<a href="./src/spitch/resources/files.py">upload</a>(\*\*<a href="src/spitch/types/file_upload_params.py">params</a>) -> <a href="./src/spitch/types/file.py">File</a></code>
- <code title="get /v1/files:usage">client.files.<a href="./src/spitch/resources/files.py">usage</a>() -> <a href="./src/spitch/types/file_usage.py">FileUsage</a></code>

# Jobs

Types:

```python
from spitch.types import Job, Jobs
```

Methods:

- <code title="get /v1/jobs">client.jobs.<a href="./src/spitch/resources/jobs.py">list</a>(\*\*<a href="src/spitch/types/job_list_params.py">params</a>) -> <a href="./src/spitch/types/job.py">SyncFilesCursor[Job]</a></code>
- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/spitch/resources/jobs.py">get</a>(job_id) -> <a href="./src/spitch/types/job.py">Job</a></code>
