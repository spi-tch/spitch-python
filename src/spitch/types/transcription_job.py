from typing import Any, Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .transcription import Transcription

__all__ = ["TranscriptionJob"]


class TranscriptionJob(BaseModel):
    id: str
    status: Literal["queued", "processing", "succeeded", "failed"]
    created_at: str
    polling_url: str
    completed_at: Optional[str] = None
    result: Optional[Transcription] = None
    error: Optional[Dict[str, Any]] = None
