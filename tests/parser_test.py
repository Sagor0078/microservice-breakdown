import textwrap
from src.parser import parse_chat_log


def test_parse_chat_log(tmp_path):
    chat_content = textwrap.dedent("""
        User: Hello
        AI: Hi there! How can I help you?
        User: What is the capital of France?
        AI: Paris is the capital of France.
    """)
    chat_file = tmp_path / "sample_chat.txt"
    chat_file.write_text(chat_content.strip())

    parsed = parse_chat_log(str(chat_file))

    assert isinstance(parsed, dict)
    assert "user_messages" in parsed
    assert "ai_messages" in parsed
    assert len(parsed["user_messages"]) == 2
    assert len(parsed["ai_messages"]) == 2
