# mp3 to text
import whisper
import json

model = whisper.load_model("base")
result = model.transcribe(
	audio="videos_mp3/1_MIT_kinetic.mp3",
	language="en",
	task="transcribe",
	fp16=False,
    word_timestamps=False
)
print(result["segments"])
chunk=[]
for segment in result["segments"]:
	chunk.append({
		"start": segment["start"],
		"end": segment["end"],
		"text": segment["text"]})
print(chunk)
with open("output.json", "w") as f:
	json.dump(chunk, f)