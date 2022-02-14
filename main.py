from kivymd.app import MDApp
import requests
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from tela import cod_helper
from kivymd.uix.dialog import MDDialog

#cod_helper = ('''
#MDTextField:
#    hint_text: 'Insira o código da moeda desejada:'
#    pos_hint: {'center_x':0.5, 'center_y': 0.5}
#    size_hint_x: None
#    width: 300
#''')

class MeuAplicativo(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        button = MDRectangleFlatButton(text='Converter', pos_hint={'center_x':0.5, 'center_y': 0.4},
                                       on_release=self.result)
        sair = MDFlatButton(text= 'Sair', pos_hint={'center_x': 0.5, 'center_y':0.2},
                                      on_release= self.close_app)
        self.cod = Builder.load_string(cod_helper)
        screen.add_widget(self.cod)
        screen.add_widget(button)
        screen.add_widget(sair)
        return screen

    def close_app(self, obj):
        MDApp.stop(self)

    def result(self, obj):
        valor = self.pegar_moeda(self.cod.text)
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = f'O valor atual do(a) {self.cod.text}, em reais é:', text = valor,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def pegar_moeda(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}--BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        b = f"R$ {cotacao}"
        return b


MeuAplicativo().run()