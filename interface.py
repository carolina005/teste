import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

class CallCenterApp(App):
    def build(self):
        return CallCenterScreen()

class CallCenterScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.server_url = 'http://127.0.0.1:5000'  # URL do servidor Flask

        self.add_widget(Label(text="Nome Cliente:"))
        self.cliente_nome = TextInput(multiline=False)
        self.add_widget(self.cliente_nome)

        self.add_widget(Label(text="Morada:"))
        self.morada = TextInput(multiline=False)
        self.add_widget(self.morada)

        self.add_widget(Label(text="Telefone:"))
        self.telefone = TextInput(multiline=False)
        self.add_widget(self.telefone)

        self.add_widget(Label(text="Nome Hamburguer:"))
        self.hamburguer_nome = Spinner(text='Carregando...', values=[])
        self.add_widget(self.hamburguer_nome)
        self.load_hamburgers()

        self.add_widget(Label(text="Quantidade:"))
        self.quantidade = TextInput(multiline=False)
        self.add_widget(self.quantidade)

        self.add_widget(Label(text="Tamanho:"))
        self.tamanho = Spinner(text='Selecione um tamanho', values=['infantil', 'normal', 'duplo'])
        self.add_widget(self.tamanho)

        self.add_widget(Label(text="Valor Total:"))
        self.valor_total = TextInput(multiline=False)
        self.add_widget(self.valor_total)

        self.submit_button = Button(text="Fazer Pedido", on_press=self.make_order)
        self.add_widget(self.submit_button)

    def load_hamburgers(self):
        response = requests.get(f'{self.server_url}/hamburgers')
        if response.status_code == 200:
            self.hamburguer_nome.values = response.json()

    def make_order(self, instance):
        order_data = {
            'nome': self.cliente_nome.text,
            'morada': self.morada.text,
            'telefone': self.telefone.text,
            'hamburguer': self.hamburguer_nome.text,
            'quantidade': int(self.quantidade.text),
            'tamanho': self.tamanho.text,
            'valor_total': float(self.valor_total.text)
        }
        response = requests.post(f'{self.server_url}/order', json=order_data)
        if response.status_code == 200:
            popup = Popup(title='Sucesso', content=Label(text='Pedido realizado com sucesso!'), size_hint=(0.5, 0.5))
            popup.open()

if __name__ == '__main__':
    CallCenterApp().run()
