from urllib import response

from httpx import stream
import requests
import json
import pandas as pd
import os
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
def get_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={"model":"bge-m3","input":text_list})
    embedding=r.json()["embeddings"]
    return embedding
if __name__ == "__main__":
    jsons=os.listdir("new_jsons")
    my_dict=[]
    chunk_id=0
    for json_file in jsons:
        with open (f"new_jsons/{json_file}")as f:
            content=json.load(f)
            print(f"creating embedding for {json_file}")
            embeddings=get_embedding([c['text'] for c in content["chunks"]])
            for i,chunk in enumerate(content["chunks"]):
                chunk['chunk_id']=chunk_id
                chunk["embedding"]=embeddings[i]
                chunk_id+=1
                my_dict.append(chunk)

    df=pd.DataFrame.from_records(my_dict)
    joblib.dump(df,"embeddings.joblib")

