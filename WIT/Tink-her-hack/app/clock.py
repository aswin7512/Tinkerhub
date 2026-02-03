from kivy.app import App
from kivy.clock import Clock
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ClockLayout(BoxLayout):
    my_label = StringProperty("Start??")
    day_date = StringProperty("")
    event = None
    
    # This function is called every second by the Clock
    def update_time(self, dt):
        self.day_date = str(time.strftime("%Y-%m-%d %A"))
        self.my_label = str(time.strftime("%H:%M:%S"))
    

    def stop_time(self):
        self.event.cancel()
        self.event = None
        self.my_label = "Start??"
        self.day_date = ""
    
    
    def start_time(self):
        if not self.event:
            self.event = Clock.schedule_interval(self.update_time, 1)


class ClockApp(App):
    def build(self):        
        return ClockLayout()

    

if __name__ == '__main__':
    ClockApp().run()