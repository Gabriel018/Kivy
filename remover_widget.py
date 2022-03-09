from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class Start(Screen):
    def add_btn(self):
        new_lbl = Label(text='Ola Mundo')
        self.ids.grid.add_widget(new_lbl)
    def remove_btn(self):
        self.ids.grid.remove_widget(self.ids.label)

class Main(App):
    def build(self):
        return Start()
if __name__ == '__main__':
    Main().run()