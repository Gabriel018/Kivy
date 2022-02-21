import kivy
from  kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class Teste(App):
    def build(self):

     grad = GridLayout(cols=1, size_hint_y=None)
     grad.bind(minimum_height = grad.setter('height'))

     for i in range(50):
      btn = Button(text=str(i),size_hint_y=None,height=40)
      grad.add_widget(btn)

     root = ScrollView(size_hint=(1,None),size=(Window.width,Window.height))
     root.add_widget(grad)
     return root


Teste().run()
