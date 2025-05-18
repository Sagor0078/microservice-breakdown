import re
from collections import Counter
from nltk.corpus import stopwords

def analyze_chat(parsed_chat):
    all_messages = parsed_chat["user_messages"] + parsed_chat["ai_messages"]
    total_messages = len(all_messages)
    user_messages = len(parsed_chat["user_messages"])
    ai_messages = len(parsed_chat["ai_messages"])
    all_text = " ".join(all_messages).lower()
    tokens = re.findall(r'\b\w+\b', all_text)
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    top_keywords = [word for word, _ in Counter(filtered_tokens).most_common(5)]
    conversation_nature = ", ".join(top_keywords[:2]) if top_keywords else "general topics"
    return {
        "total_messages": total_messages,
        "user_messages": user_messages,
        "ai_messages": ai_messages,
        "top_keywords": top_keywords,
        "conversation_nature": conversation_nature
    }
