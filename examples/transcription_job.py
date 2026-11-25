"""Run submit once, then run resume with the printed ID in another process."""

import sys
import argparse

from spitch import Spitch

parser = argparse.ArgumentParser()
commands = parser.add_subparsers(dest="command", required=True)
commands.add_parser("submit").add_argument("url")
resume = commands.add_parser("resume")
resume.add_argument("job_id")
resume.add_argument("--timeout", type=float, default=300)
args = parser.parse_args()

with Spitch() as client:
    if args.command == "submit":
        print(client.speech.submit_transcription(url=args.url).id)
    else:
        try:
            job = client.speech.wait_for_transcription(args.job_id, timeout=args.timeout)
        except TimeoutError:
            sys.exit(f"Deadline reached. Resume again with {args.job_id}.")
        if job.status == "failed":
            sys.exit(f"Transcription failed: {job.error}")
        if job.result is None:
            sys.exit("The completed job has no result.")
        print(job.result.text)
