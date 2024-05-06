from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MeuApp (App):
    def build(self):
        layout = FloatLayout()

        botao1 = Button(text='Botão 1', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.1, 'y':0.8})
        botao2 = Button(text='Botão 2', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'center_y':0.5})
        botao3 = Button(text='Botão 3', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.9, 'y':0.1})
        
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)

        return layout

if __name__ == '__main__':
    MeuApp().run()