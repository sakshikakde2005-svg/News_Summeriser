# News Article Summarizer using NLP

## Project Overview
This project automatically summarizes long news articles into short summaries using Natural Language Processing (NLP).

## Features
- Summarize news articles automatically
- Extract article from URL
- Adjustable summary length
- Simple Streamlit web interface

## Technologies Used
- Python
- NLTK
- Newspaper3k
- Streamlit

## Installation

Clone the repository

git clone https://github.com/username/news-summarizer

Install dependencies

pip install -r requirements.txt

Run application

streamlit run app.py

## Algorithm
The system uses Extractive Summarization:
1. Tokenization
2. Stopword removal
3. Word frequency calculation
4. Sentence scoring
5. Top sentence selection

## Future Improvements
- BERT based summarization
- Multi-language support
- News category detection