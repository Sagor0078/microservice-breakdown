def parse_chat_log(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    user_messages = []
    ai_messages = []
    for line in lines:
        if line.startswith("User:"):
            user_messages.append(line[len("User:"):].strip())
        elif line.startswith("AI:"):
            ai_messages.append(line[len("AI:"):].strip())
    return {"user_messages": user_messages, "ai_messages": ai_messages}
