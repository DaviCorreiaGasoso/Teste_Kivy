from kivy.app import App
from kivy.uix.label import Label

class MinhaAplicacao(App):
    def build(self):
        return Label(text='Olá SESI/SENAI', font_size = 100, font_name='Arial')

if __name__ == '__main__':
    MinhaAplicacao().run()