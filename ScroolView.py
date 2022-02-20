import kivy
from  kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Teste(App,ScrollView):
    def build(self):

     grad = BoxLayout(size_hint_y=None,orientation='vertical')
     self.lbl = Label(text='Loja',font_size=30)
     self.lbl1 = Label(text='Produtos',font_size=30)
     self.lbl2 = Label(text = 'Contato',font_size=30)
     grad.add_widget(self.lbl)
     grad.add_widget(self.lbl1)
     grad.add_widget(self.lbl2)
     self.lbl = Label(text='Loja', font_size=30)
     self.lbl1 = Label(text='Produtos', font_size=30)
     self.lbl2 = Label(text='Contato', font_size=30)
     grad.add_widget(self.lbl)
     grad.add_widget(self.lbl1)
     grad.add_widget(self.lbl2)
     self.lbl = Label(text='Loja', font_size=30)
     self.lbl1 = Label(text='Produtos', font_size=30)
     self.lbl2 = Label(text='Contato', font_size=30)
     grad.add_widget(self.lbl)
     grad.add_widget(self.lbl1)
     grad.add_widget(self.lbl2)

     return grad


Teste().run()
