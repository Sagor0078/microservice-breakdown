import pytest
from unittest.mock import patch
from src.analyzer import analyze_chat

@patch("src.analyzer.stopwords.words")
def test_analyze_chat(mock_stopwords):
    mock_stopwords.return_value = ["is", "the", "of", "and", "a", "to", "in"]

    parsed_chat = {
        "user_messages": [
            "Hello, how are you?",
            "What is the capital of France?"
        ],
        "ai_messages": [
            "Hi there! I'm fine, thank you.",
            "Paris is the capital of France."
        ]
    }

    result = analyze_chat(parsed_chat)

    assert result["total_messages"] == 4
    assert result["user_messages"] == 2
    assert result["ai_messages"] == 2
    assert isinstance(result["top_keywords"], list)
    assert all(isinstance(k, str) for k in result["top_keywords"])
    assert len(result["top_keywords"]) <= 5
    assert isinstance(result["conversation_nature"], str)
