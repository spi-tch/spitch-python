# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Job"]


class Job(BaseModel):
    created_by: str

    due_date: datetime

    job_id: str

    org_id: str

    status: str
