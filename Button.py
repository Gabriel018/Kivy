import kivy
from  kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Teste(App):
    def build(self):

     grad = BoxLayout(orientation='vertical')
     btn = Button(text='Clicar',on_release=self.alterar)
     self.lbl = Label(text='Ola Mundo')
     grad.add_widget(self.lbl)
     grad.add_widget(btn)
     return grad
    def alterar(self,lbl):
        self.lbl.text='Alterado'


Teste().run()
