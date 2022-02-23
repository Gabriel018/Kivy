from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


kv = ''' 
BoxLayout:
    Label:
        text:"Ola Mundo"
     '''

class lang(App):
    def build(self):
        return Builder.load_string(kv)



lang().run()
