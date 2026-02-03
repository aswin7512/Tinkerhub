from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import time

class ClockApp(App):
    def build(self):
        # 1. Create the Label
        self.my_label = Label(text="Starting...", font_size='50sp')
        
        # 2. Schedule the update function to run every 1 second
        Clock.schedule_interval(self.update_time, 1)
        
        return self.my_label

    # This function is called every second by the Clock
    def update_time(self, dt):
        # Get current time string
        current_time = time.strftime("%H:%M:%S")
        # Update the label text
        self.my_label.text = current_time

if __name__ == '__main__':
    ClockApp().run()