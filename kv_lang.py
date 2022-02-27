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
    TextInput:          
    Label:
        text:"Digite sua senha"
    TextInput:   
     '''

class lang(App):
    def build(self):
        return Builder.load_string(kv)



lang().run()
