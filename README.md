# Legal Chatbot 

## Overview
This repository contains the code for a legal chatbot prototype developed using Llama3 and FastAPI. The chatbot aims to assist users with legal queries by refining their questions, classifying them into relevant legal categories, and generating prompts for further processing.

## Features
- **Query Rewriting**: Enhances user queries for clarity and specificity.
- **Classification**: Classifies queries into various legal domains.
- **Prompt Generation**: Generates prompts for more effective responses.
- **Vector Database Simulation**: Stores and retrieves embeddings for similar legal documents.

## Technologies Used
- Python 3.12.4
- FastAPI
- Uvicorn
- Transformers (Llama3)
- PyTorch
- Requests

## Installation
To install the required libraries, run:

```bash
pip install fastapi uvicorn transformers torch requests
