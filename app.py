import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout



class MyApp(App):

    def build(self):
     box = BoxLayout(orientation= 'vertical')
     text = TextInput(font_size = 30,height=80 , size_hint_y=None,)
     s = Scatter()
     float = FloatLayout()
     lbs = Label(font_size=30)

     float.add_widget(s)
     s.add_widget(lbs)
     box.add_widget(text)
     box.add_widget(float)

     text.bind(text=lbs.setter('text'))
     return box

if __name__ == '__main__':
    MyApp().run()