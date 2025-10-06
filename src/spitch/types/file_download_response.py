# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["FileDownloadResponse"]


class FileDownloadResponse(BaseModel):
    expires_at: datetime

    file_id: str

    url: str
