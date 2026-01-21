# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileUsage"]


class FileUsage(BaseModel):
    num_files: Optional[int] = None
    """number of files available."""

    total: Optional[str] = None
    """total storage available in human-readable format"""

    total_bytes: Optional[int] = None
    """storage used in bytes"""

    used: Optional[str] = None
    """storage used in human-readable format"""

    used_bytes: Optional[int] = None
    """total storage available in bytes"""
