from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class PronunciationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.title_label = Label(text='Pronunciation Coach', font_size=26, size_hint_y=None, height=50)
        layout.add_widget(self.title_label)
        
        self.prompt_label = Label(text='Read aloud:\n"Hello, how are you doing today?"', font_size=20, halign='center')
        layout.add_widget(self.prompt_label)
        
        self.feedback_label = Label(text='Tap the button below and speak into your microphone.', font_size=16, halign='center')
        layout.add_widget(self.feedback_label)
        
        self.record_btn = Button(text='🎙️ Start Speaking', size_hint_y=None, height=60)
        self.record_btn.bind(on_press=self.simulate_listening)
        layout.add_widget(self.record_btn)
        
        return layout

    def simulate_listening(self, instance):
        self.feedback_label.text = "Analyzing speech...\nGreat work! Focus on rounding your 'o' sounds."

if __name__ == '__main__':
    PronunciationApp().run()
