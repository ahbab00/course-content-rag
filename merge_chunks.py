import os 
import json
import math
from tracemalloc import start
n=5
for filename in os.listdir("jsons"):
    if filename.endswith(".json"):
        file_path = os.path.join("jsons", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            new_chunks=[]
            new_chuncks=len(data["chunks"])
            num_groups = math.ceil(new_chuncks / n)
            for i in range(num_groups):
                start_index = i * n
                end_index = min((i + 1) * n, new_chuncks)
                chunk_group = data["chunks"][start_index:end_index]
                new_chunks.append(
                    {
                        "number": data["chunks"][0]["number"],
                        "title": chunk_group[0]["title"],    
                        "start": chunk_group[0]["start"],
                        "end": chunk_group[-1]["end"],
                        "text": " ".join([c["text"] for c  in chunk_group]),
                    }
                )
            # for saving it as a file 
            os.makedirs("new_jsons", exist_ok=True)
            with open(os.path.join("new_jsons", filename), "w", encoding="utf-8") as f:
                json.dump({"chunks": new_chunks,"data": data["text"]}, f, ensure_ascii=False, indent=4)