from typing_extensions import Literal

from .._models import BaseModel


class Balance(BaseModel):
    amount: str
    """Available prepaid credit as an exact decimal string."""

    currency: Literal["USD"]
