# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .job import Job
from .._models import BaseModel

__all__ = ["Jobs"]


class Jobs(BaseModel):
    """Response model for listing jobs.

    Attributes:
        items: list of job metadata responses
        next_cursor: Optional cursor for pagination to get next page of results
    """

    items: List[Job]

    next_cursor: Optional[str] = None
