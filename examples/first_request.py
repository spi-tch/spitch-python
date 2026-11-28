"""Generate a WAV and print the request ID to match in Studio Logs."""

from spitch import Spitch

with Spitch(max_retries=0) as client:
    response = client.speech.generate(
        text="Nnọọ na Spitch. Ọ dị ezigbo mma inwe gị ebe a.",
        voice="ngozi",
        language="ig",
        format="wav",
    )
    response.write_to_file("hello.wav")

print("Saved hello.wav")
request_id = response.headers.get("x-request-id")
if not request_id:
    raise SystemExit("The response did not include a request ID.")
print(f"Request ID: {request_id}")
