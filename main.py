from kivymd.app import MDApp
import requests
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from tela import cod_helper, cod2_helper
from kivymd.uix.dialog import MDDialog


class MeuAplicativo(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        button = MDRectangleFlatButton(text='Converter', pos_hint={'center_x':0.5, 'center_y': 0.3},
                                       on_release=self.result)
        sair = MDFlatButton(text= 'Sair', pos_hint={'center_x': 0.5, 'center_y':0.15},
                                      on_release= self.close_app)
        self.cod = Builder.load_string(cod_helper)
        self.cod2 = Builder.load_string(cod2_helper)
        screen.add_widget(self.cod)
        screen.add_widget(self.cod2)
        screen.add_widget(button)
        screen.add_widget(sair)
        return screen

    def close_app(self, obj):
        MDApp.stop(self)

    def result(self, obj):
        valor = self.pegar_moeda(self.cod.text)
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = f'O valor atual do(a) {self.cod.text}, em {self.cod2.text}:', text = valor,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def pegar_moeda(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}--{self.cod2.text}"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}{self.cod2.text}"]["bid"]
        b = cotacao
        return b

if __name__ == '__main__':
    MeuAplicativo().run()