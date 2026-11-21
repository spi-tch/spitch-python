from spitch import Spitch

with Spitch() as client:
    result = client.speech.transcribe(url="https://spitch.app/docs-assets/audio/voices/ngozi.wav")
    print(result.text)
    # To upload a local copy instead:
    # with open("ngozi.wav", "rb") as audio:
    #     print(client.speech.transcribe(content=audio).text)
