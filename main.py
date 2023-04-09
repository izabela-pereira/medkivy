#Imports necessários para os widgets do Kivy utilizados. DatePicker e HourPicker fazem parte do
# KivyMD (tive dificuldades de compreender o funcionamento).
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# Passa o arquivo kv com as propriedades
# O arquivo .kv traz as propriedades de todos os widgets utilizados. Assim como o .css para o .js.
Builder.load_file('medapp.kv')

class MyGridLayout(Widget):
#Inicializa os objetos sem qualquer valor
    nome = ObjectProperty(None)
    tipo = ObjectProperty(None)
    dataexame = ObjectProperty(None)
    horario = ObjectProperty(None)

    # Cria função ativada pelo pressionar do botão. Esta função faz com que os inputs sejam
    # gravados e mostrados no popup.
    def press(self):
        nome = self.nome.text
        tipo = self.tipo.text
        dataexame = self.dataexame.text
        horario = self.horario.text

        # Cria popup de sucesso de cadastro
        # size_hint determina tamanho do popup, se 1 = janela inteira
        popup = Popup(title='CADASTRO DE EXAME',
                      content=Label(text=f'Exame {nome} do tipo {tipo} no dia {dataexame} '
                                         f'às {horario} horas cadastrado com sucesso.'), size_hint=(0.60, 0.60),
                      size=(400, 400))
        popup.open()

        # Limpa os inputs
        self.nome.text = ""
        self.tipo.text = ""
        self.dataexame.text = ""
        self.horario.text = ""

    #Cria função linkada ao checkbox
    def checkbox_click(self, instance, value):
        if value == True:
            print("É necessário jejum de 8 horas.")

#Cria e faz build do Aplicativo
class MedApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MedApp().run()

