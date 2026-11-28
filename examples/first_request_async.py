"""Run the first speech request with the asynchronous client."""

import asyncio

from spitch import AsyncSpitch


async def main() -> None:
    async with AsyncSpitch(max_retries=0) as client:
        response = await client.speech.generate(
            text="Nnọọ na Spitch. Ọ dị ezigbo mma inwe gị ebe a.",
            voice="ngozi",
            language="ig",
            format="wav",
        )
        await response.write_to_file("hello.wav")

    print("Saved hello.wav")
    request_id = response.headers.get("x-request-id")
    if not request_id:
        raise SystemExit("The response did not include a request ID.")
    print(f"Request ID: {request_id}")


if __name__ == "__main__":
    asyncio.run(main())
