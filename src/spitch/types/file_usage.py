# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FileUsage"]


class FileUsage(BaseModel):
    num_files: int

    total: str

    total_bytes: int

    used: str

    used_bytes: int
