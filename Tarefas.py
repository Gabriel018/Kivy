from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class add_tarefa(BoxLayout):
    def __init__(self,tarefas):
        super().__init__()
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class Teste(App):
    def build(self):
        return add_tarefa(["Estudar",'Comer'])

Teste().run()