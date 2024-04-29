from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return Image(source="/Users/aluno.sesipaulista/Pictures/Screenshots/gorila.jpg")

class MeuApp(App):
    def build(self):
        return AsyncImage(source="https://s1.static.brasilescola.uol.com.br/be/2021/05/bandeira-de-pernambuco.jpg")
    
if __name__ == "__main__":
    MeuApp().run()