import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "cognitivecomputations/dolphin-mistral-24b-venice-edition:free"
SYSTEM_PROMPT = "You are a friendly helper..."

messages = [{"role": "system", "content": SYSTEM_PROMPT}]


def ask_gpt():
    try:
        payload = {"model": MODEL, "messages": messages}

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
    print("GPT CLI (type 'exit' to quit)\n")

    while True:
        user_text = input("You: ").strip()

        if user_text.lower() in ["exit", "quit"]:
            print("Goodbye.")
            break

        if not user_text:
            continue

        messages.append({"role": "user", "content": user_text})

        reply = ask_gpt()

        messages.append({"role": "assistant", "content": reply})

        print(f"Bot: {reply}\n")