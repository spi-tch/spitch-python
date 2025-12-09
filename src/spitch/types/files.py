# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from .._models import BaseModel

__all__ = ["Files"]


class Files(BaseModel):
    """Response model for listing files.

    Attributes:
        items: List of file metadata responses
        next_cursor: Optional cursor for pagination to get next page of results
    """

    items: List[File]

    next_cursor: Optional[str] = None
