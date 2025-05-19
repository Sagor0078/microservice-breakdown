# AI Chat Log Summarizer

This project parses plain text chat logs between a user and an AI, analyzes the conversation, and generates a readable summary. It uses Python3.11, fastapi, `nltk` for natural language processing, and `pytest` for testing.

---

## Features

- Parse structured chat logs (User/AI format)
- Count total messages, user messages, AI messages
- Extract top keywords (excluding stopwords)
- Generate human-readable summaries

---

## Project Structure

```md
ai-chat-log-summarizer/
├── main.py
├── src/
│ ├── parser.py # Parses raw chat logs
│ ├── analyzer.py # Analyzes chat content
│ └── summarizer.py # Generates summary from analysis
├── tests/
│ ├── parser_test.py
│ ├── analyzer_test.py
│ └── summarizer_test.py
├── requirements.txt
└── README.md
```


---

## Installation

```bash
git clone https://github.com/Sagor0078/ai-chat-log-summarizer.git
cd ai-chat-log-summarizer
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##  NLTK Setup
This project uses NLTK stopwords. To download them:
```bash
python3.11
>> import nltk
>> nltk.download('stopwords')
>> exit()
```

## Running Tests
```bash 
pytest tests/
```
[![Directory docs](img/test.png)](https://github.com/Sagor0078/ai-chat-log-summarizer)


## Example Chat Log Format

```txt
User: Hello
AI: Hi there! How can I help you?
User: What is the capital of France?
AI: Paris is the capital of France.
```

## Example Summary Output
```txt
Summary:
- The conversation had 4 messages (2 complete exchanges).
- The user sent 2 messages, and the AI responded with 2 messages.
- The conversation was mainly about paris, capital.
- Most common keywords: paris, capital, france.
```

## How It Works

- Parser: Reads the log and extracts messages
- Analyzer: Counts messages, extracts keywords
- Summarizer: Combines everything into a summary

## fastapi cli app 

run the app: 
```bash
uvicorn main:app --reload
```

[![Directory docs](img/api.png)](https://github.com/Sagor0078/ai-chat-log-summarizer)
[![Directory docs](img/api2.png)](https://github.com/Sagor0078/ai-chat-log-summarizer)
