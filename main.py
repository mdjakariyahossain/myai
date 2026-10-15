from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.input = TextInput(hint_text='আপনার প্রশ্ন লিখুন...', multiline=False)
        btn = Button(text='উত্তর দিন', size_hint=(1, 0.3))
        self.output = Label(text='উত্তর এখানে দেখাবে')
        
        btn.bind(on_press=self.answer)
        
        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(self.output)
        return layout
    
    def answer(self, instance):
        # এখানে আপনি AI API যোগ করতে পারবেন
        q = self.input.text
        self.output.text = f"আপনি লিখেছেন: {q}"

AIApp().run()
