from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ClickApp(App):
    def build(self):
        # Create a layout to hold widgets vertically
        layout = BoxLayout(orientation='vertical')
        
        # Create a label and a button
        self.label = Label(text="Press the button below")
        btn = Button(text="Click Me!")
        
        # Bind the button press to a function
        btn.bind(on_press=self.on_button_click)
        
        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    # This function runs when the button is pressed
    def on_button_click(self, instance):
        self.label.text = "You clicked it!"

if __name__ == '__main__':
    ClickApp().run()