from kivy.app import App 
from kivy.uix.image import Image, AsyncImage
from kivy.uix.video import Video

class ImagemPC(App):
    def build(self):
        return Image(source="/Users/aluno.sesipaulista/Pictures/Screenshots/gorila.jpg")

class ImagemWeb(App):
    def build(self):
        return AsyncImage(source="https://s1.static.brasilescola.uol.com.br/be/2021/05/bandeira-de-pernambuco.jpg")

class VideoPC(App):
    def build(self):
        return Video(source="C:/Users/aluno.sesipaulista/Videos/Captures/Calculadora - GeoGebra - Opera 2023-11-27 15-43-07.mp4")

    
if __name__ == "__main__":
    VideoPC().run()