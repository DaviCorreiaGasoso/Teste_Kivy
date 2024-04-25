from kivy.app import App
from kivy.uix.button import Button

class MeuApp (App):
    def build(self):
        return Button(text="Olá SESI! Esse é meu primeiro programa no kivy \n Eu sou sesiano")

if __name__ == '__main__':
    MeuApp().run()