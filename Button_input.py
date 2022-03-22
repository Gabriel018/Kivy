import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyLayout,self).__init__(**kwargs)
        self.cols = 1
        self.maingrid = GridLayout()
        self.maingrid.cols = 2

        self.maingrid.add_widget(Label(text='Name: '))
        self.name = TextInput(multiline=False)
        self.maingrid.add_widget(self.name)

        self.maingrid.add_widget(Label(text='Last_Name: '))
        self.last_name = TextInput(multiline=False)
        self.maingrid.add_widget(self.last_name)

        self.maingrid.add_widget(Label(text='Curso: '))
        self.curso = TextInput(multiline=False)
        self.maingrid.add_widget(self.curso)

        self.add_widget(self.maingrid)

        self.Enviar = Button(text='Enviar')
        self.Enviar.bind(on_press=self.press)
        self.add_widget(self.Enviar)




    def press(self,instance):
        name = self.name.text
        last_name = self.last_name.text
        curso = self.curso.text
        self.add_widget(Label(text=f'Boa tarde,{name}{last_name}, seu curso escolhido foi,{curso}'))

class Myapp(App):
    def build(self):
        return  MyLayout()

if __name__ == '__main__':
    Myapp().run()