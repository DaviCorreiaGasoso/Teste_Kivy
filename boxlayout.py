from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Horizontal (App) :
    def build(self):
        layout_horizontal = BoxLayout(orientation='horizontal', spacing=10, padding=[20,10])

        botao1 = Button(text='Botão 1')
        botao2 = Button(text='Botão 2')
        botao3 = Button(text='Botão 3')
        
        layout_horizontal.add_widget(botao1)
        layout_horizontal.add_widget(botao2)
        layout_horizontal.add_widget(botao3)

        return layout_horizontal

class Elaborado(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', spacing=10)

        #Criando e adicionando um botão com texto, cor de fundo e tamanho de fonte personalizados
        botao1 = Button(text='Botão 1', background_color=(0.2, 0.7, 0.3, 1), font_size=20)
        layout.add_widget(botao1)

        #Criando e adicionando um botão com texto diferente e alinhamento horizontal personalidado
        botao2 = Button(text='Clique Aqui', halign='center')
        layout.add_widget(botao2)

        #Criando e adicionando um botão com texto grande e cor de fundo personalizada
        botao3 = Button(text='Clique para Continuar', background_color=(0.9, 0.5, 0.1, 1), font_size=30)
        layout.add_widget(botao3)

        #Criando e adicionando um botão com ação personalizada ao ser pressionado
        def acao_botao(instance):
            instance.text = 'O seu botão foi apertado'
        botao4 = Button(text='Botão 4')
        botao4.bind(on_press=acao_botao)
        layout.add_widget(botao4)

        #Adicionando um rótulo para exibir informações adicionais
        info_label = Label(text='Pressione os botões para ver suas ações')
        layout.add_widget(info_label)

        return layout


if __name__ == '__main__':
    Elaborado().run()
