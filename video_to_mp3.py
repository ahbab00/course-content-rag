# convert the videos into mp3
import os 
import subprocess
files=os.listdir("videos")
for file in files:
    print(file)
    tutorial_name=file.split(".")[0].split("#")[1].strip()
    print(tutorial_name)
    file_name=file.split("#")[0].strip()
    print(file_name,tutorial_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"videos_mp3/{tutorial_name}_{file_name}.mp3"])