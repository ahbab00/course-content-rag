# Course Content RAG

An end-to-end Retrieval-Augmented Generation (RAG) system that transforms MIT course lecture videos into a searchable knowledge base. The project automatically processes lecture videos, generates transcripts, creates embeddings, retrieves relevant context, and uses a local LLM to answer questions grounded in course content.

## Overview

This project enables users to ask natural language questions about lecture material and receive context-aware answers generated from the course transcripts.

The pipeline starts with raw lecture videos and converts them into a structured knowledge base through transcription, chunking, embedding generation, semantic retrieval, and LLM-powered response generation.

---

## Features

- Automatic video-to-audio conversion using FFmpeg
- Speech-to-text transcription using Whisper
- Transcript chunking for efficient retrieval
- Embedding generation and storage
- Semantic search over lecture content
- Retrieval-Augmented Generation (RAG)
- Local inference using Ollama and Llama 3.2
- Context-aware question answering

---

## Architecture

```text
MIT Course Videos
        ↓
video_to_mp3.py
        ↓
MP3 Files
        ↓
mp3_to_json.py
        ↓
JSON Transcripts
        ↓
merge_chunks.py
        ↓
Chunked Content
        ↓
preprocessing_json.py
        ↓
embeddings.joblib
        ↓
processing_incoming.py
        ↓
Prompt Generation
        ↓
Ollama Llama 3.2
        ↓
Generated Answer
```

---

## Project Structure

```text
course-content-rag/
│
├── jsons/
├── new_jsons/
├── utils/
│
├── video_to_mp3.py
├── mp3_to_json.py
├── merge_chunks.py
├── preprocessing_json.py
├── processing_incoming.py
│
├── embeddings.joblib
├── prompt.txt
├── response.txt
└── README.md
```

---

## Workflow

### Step 1: Collect Lecture Videos

Store lecture videos inside the `videos` directory.

### Step 2: Convert Videos to Audio

Extract audio from lecture videos using FFmpeg.

```bash
python video_to_mp3.py
```

### Step 3: Generate Transcripts

Convert MP3 files into JSON transcripts using Whisper.

```bash
python mp3_to_json.py
```

### Step 4: Chunk and Process Content

Merge transcript chunks and prepare the data for embedding generation.

```bash
python merge_chunks.py
python preprocessing_json.py
```

### Step 5: Create Embeddings

Generate embeddings and store them in `embeddings.joblib` for semantic retrieval.

### Step 6: Ask Questions

Query the knowledge base and generate answers using Ollama Llama 3.2.

```bash
python processing_incoming.py
```

---

## Tech Stack

- Python
- FFmpeg
- OpenAI Whisper
- Joblib
- JSON
- Ollama
- Llama 3.2
- Retrieval-Augmented Generation (RAG)

---

## Example Questions

- Explain the concept discussed in lecture 3.
- Summarize the main ideas from a lecture.
- What examples were used to explain a topic?
- What is the definition of a specific concept?
- Compare two concepts covered in the course.

---

## Learning Outcomes

This project provided hands-on experience with:

- Building an end-to-end RAG pipeline
- Speech-to-text processing
- Transcript preprocessing
- Semantic retrieval systems
- Vector embeddings
- Prompt engineering
- Local LLM deployment with Ollama
- Educational AI applications

---

## Future Improvements

- Streamlit web interface
- Support for multiple courses
- Citation-based responses
- Hybrid retrieval methods
- Re-ranking models
- Performance evaluation framework
- Real-time document ingestion

---

## Author

Built as a practical exploration of Retrieval-Augmented Generation (RAG), semantic search, and local LLM-powered question answering on educational content.