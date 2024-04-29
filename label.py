from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaAplicacao(App):
    def build(self):
        return Label(
            text='Olá SESI',
            halign='center',
            valign='top',
            size_hint = (None, None),
            size = (150, 50),
            text_size=(150, None)
            )

if __name__ == '__main__':
    MinhaAplicacao().run()