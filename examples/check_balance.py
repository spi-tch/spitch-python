"""Set SPITCH_API_KEY and run this script before queuing a batch."""

import sys
from decimal import Decimal

from spitch import Spitch, APIError


def main() -> int:
    with Spitch() as client:
        try:
            balance = client.balance.get()
        except APIError as error:
            print(f"Balance lookup failed ({type(error).__name__}). Hold the batch.", file=sys.stderr)
            return 2

    print(f"{balance.amount} {balance.currency}")
    if Decimal(balance.amount) < Decimal("5"):
        print("Below the 5 USD minimum. Hold the batch.")
        return 1
    print("Credit check passed. The batch can be queued.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
