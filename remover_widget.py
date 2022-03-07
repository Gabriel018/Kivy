from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class lbl(BoxLayout):
    pass

class teste_remove(App):
    def build(self):
        return lbl()



teste_remove().run()