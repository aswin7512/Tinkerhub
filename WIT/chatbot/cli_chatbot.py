import requests

API_KEY = "API-KEY"     #PASTE YOUR API KEY HERE
URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "google/gemini-2.5-flash-image-preview:free"
# Example: "meta-llama/llama-3.1-8b-instruct:free"
# Example: "anthropic/claude-3.5-sonnet"

# 📝 Personality / system prompt
SYSTEM_PROMPT = "You are a friendly helper."


def ask_gpt(user_text):
    try:
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
        }
        resp = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=30,
        )
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Error: {e}]"


if __name__ == "__main__":
    print("🤖 GPT CLI (type 'exit' to quit)")
    while True:
        user = input("\nYou: ")
        if user.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break
        reply = ask_gpt(user)
        print(f"Bot: {reply.strip()}")