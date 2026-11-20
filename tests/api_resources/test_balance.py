from spitch import Spitch, AsyncSpitch
from spitch.types import Balance


def test_balance(client: Spitch) -> None:
    balance = client.balance.get()
    assert isinstance(balance, Balance)
    assert balance.amount == "12.34567890123456789"
    assert balance.currency == "USD"


async def test_async_balance(async_client: AsyncSpitch) -> None:
    balance = await async_client.balance.get()
    assert isinstance(balance, Balance)
    assert balance.amount == "12.34567890123456789"
    assert balance.currency == "USD"
