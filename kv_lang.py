from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput


kv = ''' 

FloatLayout
     
    Label:
        text:"Digite seu nome"
       
        font_size: 25
        
    TextInput:
        
        height: 40          
    Label:
        text:"Digite sua senha"
       
    TextInput:   

        height: 40  
     '''

class lang(App):
    def build(self):
        return Builder.load_string(kv)



lang().run()
