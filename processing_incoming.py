
from preprocessing_json import get_embedding
import joblib
import numpy as np
import pandas as pd
import os
import requests
import json
from sklearn.metrics.pairwise import cosine_similarity

# Load the precomputed embeddings
df=joblib.load("embeddings.joblib")
def inferance(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={"model":"llama3.2","prompt":prompt,"stream":False})
    response= r.json()
    print(response)
    return response

incoming_query=input("ask a question ")
query_embedding=get_embedding([incoming_query])[0]
# print(query_embedding)

# find cosine similarities in query_embedding with other emqbeddings
# print(np.vstack(df["embedding"].values))
# print(np.vstack(df["embedding"]).shape)
similarities=cosine_similarity(np.vstack(df["embedding"]),[query_embedding]).flatten()
# print(similarities)
top_results=5
max_indices=similarities.argsort()[::-1][0:top_results]
# print(max_indices)
new_df=df.loc[max_indices]
# print(new_df[["number","title","text"]])
prompt=f'''This is MIT course of physics to teach student about the basic of the physics. here are videos subtitle chunks containing video title , video number, video text , video start time in seconds, video end time in seconds and chunk id

{new_df[["number","title","start","end","text"]].to_json(orient="records")}

--------------------------------------------------------

"{incoming_query}"

user asked this question related to the video chunks ,you have to answer in human not in that format this format is for you to understand the context and provide a helpful response. you have to explain where and how much content is taught where (in which and what timestamps) and guide the user to go to that perticular video and used it . if user asked unrealeted question then tell him/her that you can asked only course related question.and also format the answer in a way that it is easy to understand and also provide the video number and title in the answer.and dont metion the number just human readable format. if the answer is not found in the video chunks then tell the user that you are unable to find the answer in the video chunks and suggest them to ask another question related to the course content.





'''
with open("prompt.txt","w")as f:
    f.write(prompt) 

response=inferance(prompt)["response"]
print(response)

with open("response.txt","w")as f:
    f.write(response)
# for index,item in new_df.iterrows():
#     print(index,item['title'],item["number"],item["text"],item["start"],item["end"],item["chunk_id"])