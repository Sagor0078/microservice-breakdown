from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
from src.parser import parse_chat_log
from src.analyzer import analyze_chat
from src.summarizer import ChatSummarizer
import tempfile
import shutil

app = FastAPI(title="AI Chat Log Summarizer API")

@app.post("/summarize", response_class=PlainTextResponse)
async def summarize_chat(file: UploadFile = File(...)):
    """
    Accepts a chat log text file upload and returns a summary.
    """
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    # Parse, analyze, and summarize
    parsed_chat = parse_chat_log(tmp_path)
    analysis = analyze_chat(parsed_chat)
    summarizer = ChatSummarizer(parsed_chat, analysis)
    summary = summarizer.generate_summary()

    return summary
