from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


class add_tarefa(ScrollView):
    def __init__(self,tarefas):
        super().__init__()
        for tarefa in tarefas:
            self.ids.Caixa.add_widget(Label(text=tarefa,font_size=20,size_hint_y=None,height=200))

class Teste(App):
    def build(self):
        return add_tarefa(["Estudar",'Comer','fazer sexo,','ler','Musculaçao'])

Teste().run()