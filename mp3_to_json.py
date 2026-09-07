import whisper
import json
import os

os.makedirs("jsons", exist_ok=True)

model = whisper.load_model("base")
audios = os.listdir("videos_mp3")
for audio in audios:
    print(audio)
    if "#" in audio and "_" in audio:
        number = audio.split("#")[0].strip()
        title = audio.split("_")[1].split(".")[0].strip()
    else:
        number = "unknown"
        title = audio.split(".")[0]
    print(number, title)
    result = model.transcribe(
        audio=f"videos_mp3/{audio}",
        language="en",
        task="transcribe",
        fp16=False,
        word_timestamps=False,
    )

    chunk = []
    for segment in result["segments"]:
        chunk.append({
            "number": number,
            "title": title,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"],
        })
    chunk_with_metadata = {"chunks": chunk, "text": result["text"]}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunk_with_metadata, f)