from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput


kv = ''' 
GridLayout:

    cols:2
    rows:2
    padding:20
    spacing:20
    Label:
        text:"Digite seu nome"
        size_hint_x: 1
        size_hint_y: None
        font_size: 25
        
    TextInput:
        size_hint_x: 1
        size_hint_y: None
        height: 40          
    Label:
        text:"Digite sua senha"
        font_size: 25
        size_hint: (1, None)
    TextInput:   
        size_hint: (1, None)
        height: 40  
     '''

class lang(App):
    def build(self):
        return Builder.load_string(kv)



lang().run()
