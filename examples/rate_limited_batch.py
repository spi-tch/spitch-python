"""Read metadata for each file ID: python examples/rate_limited_batch.py FILE_ID [FILE_ID ...]."""

from __future__ import annotations

import sys
import time
import asyncio
import argparse

from spitch import AsyncSpitch, APIStatusError, RateLimitError
from spitch.types import FileMeta

MAX_ATTEMPTS = 3  # Includes the first request.
BUDGET_SECONDS = 30
LIMIT_HEADERS = ("Retry-After", "RateLimit-Limit", "RateLimit-Remaining", "RateLimit-Reset", "X-Usage-Tier")


async def read_file(client: AsyncSpitch, file_id: str) -> FileMeta:
    deadline = time.monotonic() + BUDGET_SECONDS
    for attempt in range(1, MAX_ATTEMPTS + 1):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise RuntimeError("File retry deadline reached.")
        try:
            return await asyncio.wait_for(client.files.get(file_id), timeout=remaining)
        except RateLimitError as error:
            headers = error.response.headers
            advice = ", ".join(f"{name}: {headers[name]}" for name in LIMIT_HEADERS if name in headers)
            print(f"HTTP 429 (attempt {attempt}/{MAX_ATTEMPTS}): {advice}", file=sys.stderr)
            if attempt == MAX_ATTEMPTS:
                break
            delay = headers.get("Retry-After", "").strip()
            if not (delay.isascii() and delay.isdecimal()):
                raise RuntimeError("No usable Retry-After in seconds; stopping the batch.") from error
            seconds = float(delay)
            if seconds >= deadline - time.monotonic():
                raise RuntimeError("Retry-After exceeds the remaining file budget.") from error
            await asyncio.sleep(seconds)
    raise RuntimeError("File retry attempts exhausted.")


async def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file_ids", metavar="FILE_ID", nargs="+")
    args = parser.parse_args()
    # The loop owns all retries. Keep one file in flight at a time.
    async with AsyncSpitch(max_retries=0) as client:
        for file_id in args.file_ids:
            file = await read_file(client, file_id)
            print(file.file_id, file.status)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except APIStatusError as exc:
        sys.exit("HTTP 402: check workspace billing." if exc.status_code == 402 else f"HTTP {exc.status_code}")
    except (asyncio.TimeoutError, RuntimeError) as exc:
        sys.exit(str(exc) or "File retry deadline reached.")
