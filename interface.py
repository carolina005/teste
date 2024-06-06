# main.py (Aplicação Kivy)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.network.urlrequest import UrlRequest
import json

class Cliente:
    def __init__(self, nome, morada, telefone):
        self.nome = nome
        self.morada = morada
        self.telefone = telefone


class Pedido:
    def __init__(self, id_cliente, nome_hamburguer, quantidade, tamanho, valor_total):
        self.id_cliente = id_cliente
        self.nome_hamburguer = nome_hamburguer
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.valor_total = valor_total


class Hamburguer:
    def __init__(self, nome_hamburguer, ingredientes):
        self.nome_hamburguer = nome_hamburguer
        self.ingredientes = ingredientes


class Formulario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Criar o layout da aplicação
        self.criar_layout_app()

    # Criar o layout da aplicação
    def criar_layout_app(self):
        self.orientation = "vertical"
        self.padding = 20

        # Adicionar widgets de cliente
        self.add_cliente_widgets()

        # Adicionar widgets de hambúrguer
        self.add_hamburguer_widgets()

        # Adicionar widgets de pedido
        self.add_pedido_widgets()

        # Adicionar uma barra de progresso
        self.barra_de_progresso = ProgressBar(max=100, value=0)
        self.add_widget(self.barra_de_progresso)

    def add_cliente_widgets(self):
        grid = GridLayout(cols=2)
        self.add_widget(Label(text="Clientes"))
        self.add_widget(grid)

        grid.add_widget(Label(text="Nome"))
        self.txt_nome_cliente = TextInput()
        grid.add_widget(self.txt_nome_cliente)

        grid.add_widget(Label(text="Morada"))
        self.txt_morada_cliente = TextInput()
        grid.add_widget(self.txt_morada_cliente)

        grid.add_widget(Label(text="Telefone"))
        self.txt_telefone_cliente = TextInput()
        grid.add_widget(self.txt_telefone_cliente)

        btn_add_cliente = Button(text="Adicionar Cliente")
        btn_add_cliente.bind(on_release=self.adicionar_cliente)
        grid.add_widget(btn_add_cliente)

    def add_hamburguer_widgets(self):
        grid = GridLayout(cols=2)
        self.add_widget(Label(text="Hambúrgueres"))
        self.add_widget(grid)

        grid.add_widget(Label(text="Nome"))
        self.txt_nome_hamburguer = TextInput()
        grid.add_widget(self.txt_nome_hamburguer)

        grid.add_widget(Label(text="Ingredientes"))
        self.txt_ingredientes_hamburguer = TextInput()
        grid.add_widget(self.txt_ingredientes_hamburguer)

        btn_add_hamburguer = Button(text="Adicionar Hambúrguer")
        btn_add_hamburguer.bind(on_release=self.adicionar_hamburguer)
        grid.add_widget(btn_add_hamburguer)

    def add_pedido_widgets(self):
        grid = GridLayout(cols=2)
        self.add_widget(Label(text="Pedidos"))
        self.add_widget(grid)

        grid.add_widget(Label(text="ID Cliente"))
        self.txt_id_cliente_pedido = TextInput()
        grid.add_widget(self.txt_id_cliente_pedido)

        grid.add_widget(Label(text="Nome Hambúrguer"))
        self.txt_nome_hamburguer_pedido = TextInput()
        grid.add_widget(self.txt_nome_hamburguer_pedido)

        grid.add_widget(Label(text="Quantidade"))
        self.txt_quantidade_pedido = TextInput()
        grid.add_widget(self.txt_quantidade_pedido)

        grid.add_widget(Label(text="Tamanho"))
        self.spinner_tamanho_pedido = Spinner(text="normal", values=("infantil", "normal", "duplo"))
        grid.add_widget(self.spinner_tamanho_pedido)

        grid.add_widget(Label(text="Valor Total"))
        self.txt_valor_total_pedido = TextInput()
        grid.add_widget(self.txt_valor_total_pedido)

        btn_add_pedido = Button(text="Adicionar Pedido")
        btn_add_pedido.bind(on_release=self.adicionar_pedido)
        grid.add_widget(btn_add_pedido)

    def adicionar_cliente(self, instance):
        cliente = {
            "nome": self.txt_nome_cliente.text,
            "morada": self.txt_morada_cliente.text,
            "telefone": self.txt_telefone_cliente.text
        }
        UrlRequest('http://127.0.0.1:5000/clientes', req_body=json.dumps(cliente), req_headers={'Content-Type': 'application/json'}, on_success=self.atualizar_barra)

    def adicionar_hamburguer(self, instance):
        hamburguer = {
            "nome_hamburguer": self.txt_nome_hamburguer.text,
            "ingredientes": self.txt_ingredientes_hamburguer.text
        }
        UrlRequest('http://127.0.0.1:5000/hamburgueres', req_body=json.dumps(hamburguer), req_headers={'Content-Type': 'application/json'}, on_success=self.atualizar_barra)

    def adicionar_pedido(self, instance):
        pedido = {
            "id_cliente": int(self.txt_id_cliente_pedido.text),
            "nome_hamburguer": self.txt_nome_hamburguer_pedido.text,
            "quantidade": int(self.txt_quantidade_pedido.text),
            "tamanho": self.spinner_tamanho_pedido.text,
            "valor_total": float(self.txt_valor_total_pedido.text)
        }
        UrlRequest('http://127.0.0.1:5000/pedidos', req_body=json.dumps(pedido), req_headers={'Content-Type': 'application/json'}, on_success=self.atualizar_barra)

    def atualizar_barra(self, *args):
        self.barra_de_progresso.value += 10


class FormularioApp(App):
    def build(self):
        self.title = "Formulário Complexo"
        return Formulario()


if __name__ == "__main__":
    FormularioApp().run()
