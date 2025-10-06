# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileUploadResponse"]


class FileUploadResponse(BaseModel):
    category: Optional[str] = None

    content_type: Optional[str] = None

    created_at: datetime

    file_id: str

    original_name: Optional[str] = None

    size_bytes: Optional[int] = None

    status: str
