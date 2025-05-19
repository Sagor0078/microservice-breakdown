class ChatSummarizer:
    def __init__(self, parsed_chat, analysis):
        self.parsed_chat = parsed_chat
        self.analysis = analysis

    def generate_summary(self):
        total_exchanges = min(
            len(self.parsed_chat["user_messages"]), len(self.parsed_chat["ai_messages"])
        )
        keywords_text = ", ".join(self.analysis["top_keywords"])
        summary = "Summary:\n"
        summary += f"- The conversation had {self.analysis['total_messages']} messages "
        summary += f"({total_exchanges} complete exchanges).\n"
        summary += f"- The user sent {self.analysis['user_messages']} messages, "
        summary += (
            f"and the AI responded with {self.analysis['ai_messages']} messages.\n"
        )
        summary += f"- The conversation was mainly about {self.analysis['conversation_nature']}.\n"
        summary += f"- Most common keywords: {keywords_text}.\n"
        return summary
