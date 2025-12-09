# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["FileDownloadResponse"]


class FileDownloadResponse(BaseModel):
    """Response model for file download URLs.

    Attributes:
        file_id: Unique identifier for the file
        url: Pre-signed download URL
        expires_at: When the download URL expires
    """

    expires_at: datetime

    file_id: str

    url: str
