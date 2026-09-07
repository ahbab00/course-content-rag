# How to use Rag AI teaching assistant on your own data 

# step 1-> Collect All your videos 
           move all videos to a video folder

# step 2-> Convert to Mp3
      convert all the videos files mp3 by running video_to_mp3.py


# step 3-> convert mp3 to json 
      convert all the mp3 to json running mp3_to_json.py   

# step 4-> Convert json files to vector
      using preprocessing_json convert the json files to a dataframe with embeddings and save is as a joblib pickle

# step 5 -> prompt generation and feeding to the llm
   read the joblib file and load it into the memory.then create a relevent prompt as per user query and feed it to LLM