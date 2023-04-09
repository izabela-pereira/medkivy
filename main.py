from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# Designate Our .kv design file
Builder.load_file('medapp.kv')

class MyGridLayout(Widget):
    nome = ObjectProperty(None)
    tipo = ObjectProperty(None)

    def press(self):
        nome = self.nome.text
        tipo = self.tipo.text
        # Cria popup de sucesso de cadastro
        # size_hint determina tamanho do popup, se 1 = janela inteira
        popup = Popup(title='CADASTRO DE EXAME',
                      content=Label(text=f'Exame {nome} do tipo {tipo} cadastrado com sucesso.'), size_hint=(0.5, 0.5),
                      size=(400, 400))
        popup.open()

        print(f'Exame {nome} do tipo {tipo} cadastrado com sucesso.')
        # Limpa os inputs
        self.nome.text = ""
        self.tipo.text = ""

class MedApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MedApp().run()

