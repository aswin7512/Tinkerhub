from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class CounterLayout(BoxLayout):
    # We create a property that Kivy can watch for changes
    # When this string changes, the UI updates automatically!
    number_text = StringProperty("0")

    def increase_number(self):
        # Turn string to int, add 1, turn back to string
        current = int(self.number_text)
        self.number_text = str(current + 1)

    def decrease_number(self):
        current = int(self.number_text)
        self.number_text = str(current - 1)

class CounterApp(App):
    def build(self):
        return CounterLayout()

if __name__ == '__main__':
    CounterApp().run()