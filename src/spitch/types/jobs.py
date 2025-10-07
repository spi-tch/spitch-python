# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .job import Job
from .._models import BaseModel

__all__ = ["Jobs"]


class Jobs(BaseModel):
    items: List[Job]

    next_cursor: Optional[str] = None
