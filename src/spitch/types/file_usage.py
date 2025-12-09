# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FileUsage"]


class FileUsage(BaseModel):
    """Storage usage information for an organization.

    Attributes:
        total: Human-readable total storage limit
        used: Human-readable used storage amount
        total_bytes: Total storage limit in bytes
        used_bytes: Used storage amount in bytes
        num_files: Number of files stored
    """

    num_files: int

    total: str

    total_bytes: int

    used: str

    used_bytes: int
