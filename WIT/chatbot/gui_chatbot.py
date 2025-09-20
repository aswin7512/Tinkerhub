import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# 🔑 Your OpenRouter API key here
API_KEY = "paste here"          # paste your api key here
URL = "https://openrouter.ai/api/v1/chat/completions"

# 📝 Choose your model here (just edit this string)
MODEL = "google/gemini-2.5-flash-image-preview:free"
# Example: "meta-llama/llama-3.1-8b-instruct:free"
# Example: "anthropic/claude-3.5-sonnet"


class GPTApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # User input
        self.input = TextInput(
            hint_text="Type your message", multiline=True, size_hint=(1, 0.3)
        )
        self.layout.add_widget(self.input)

        # Send button
        self.button = Button(text="Send", size_hint=(1, 0.1))
        self.button.bind(on_press=self.send_message)
        self.layout.add_widget(self.button)

        # Chat output
        self.label = Label(text="Chat will appear here", halign="left", valign="top")
        self.label.bind(size=self.label.setter("text_size"))
        self.layout.add_widget(self.label)

        return self.layout

    def send_message(self, instance):
        user_text = self.input.text.strip()
        if not user_text:
            return

        # Add user message
        self.label.text += f"\n\nYou: {user_text}"
        self.input.text = ""

        try:
            # Call OpenRouter with chosen MODEL
            payload = {
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "You are a friendly helper."},
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
            reply = resp.json()["choices"][0]["message"]["content"]

            # Add bot reply
            self.label.text += f"\nBot: {reply.strip()}"
        except Exception as e:
            self.label.text += f"\n[Error: {e}]"


if __name__ == "__main__":
    GPTApp().run()