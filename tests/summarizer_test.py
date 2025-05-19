from src.summarizer import ChatSummarizer

def test_generate_summary():
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

    analysis = {
        "total_messages": 4,
        "user_messages": 2,
        "ai_messages": 2,
        "top_keywords": ["paris", "capital", "france"],
        "conversation_nature": "paris, capital"
    }

    summarizer = ChatSummarizer(parsed_chat, analysis)
    summary = summarizer.generate_summary()

    # Basic structure assertions
    assert isinstance(summary, str)
    assert "Summary:" in summary
    assert "- The conversation had 4 messages (2 complete exchanges)." in summary
    assert "- The user sent 2 messages, and the AI responded with 2 messages." in summary
    assert "- The conversation was mainly about paris, capital." in summary
    assert "- Most common keywords: paris, capital, france." in summary
