# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    """Metadata info for this file."""

    created_at: datetime

    file_id: str

    original_name: Optional[str] = None

    size_bytes: Optional[int] = None

    status: str

    uploaded_by: Optional[str] = None
