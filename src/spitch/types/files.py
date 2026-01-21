# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from .._models import BaseModel

__all__ = ["Files"]


class Files(BaseModel):
    """an array of file information."""

    items: List[File]

    next_cursor: Optional[str] = None
