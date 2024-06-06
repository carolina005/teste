from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Tela inicial
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Bem-vindo à Home'))
        
        btn_cliente = Button(text='Ir para Adicionar Cliente', on_release=self.go_to_add_cliente)
        layout.add_widget(btn_cliente)
        
        btn_hamburguer = Button(text='Ir para Adicionar Hamburguer', on_release=self.go_to_add_hamburguer)
        layout.add_widget(btn_hamburguer)
        
        btn_pedido = Button(text='Ir para Adicionar Pedido', on_release=self.go_to_add_pedido)
        layout.add_widget(btn_pedido)
        
        self.add_widget(layout)

    def go_to_add_cliente(self, instance):
        self.manager.current = 'add_cliente'
    
    def go_to_add_hamburguer(self, instance):
        self.manager.current = 'add_hamburguer'
    
    def go_to_add_pedido(self, instance):
        self.manager.current = 'add_pedido'

# Tela para adicionar clientes
class AddClienteScreen(Screen):
    def __init__(self, **kwargs):
        super(AddClienteScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Adicionar Cliente'))
        
        self.nome = TextInput(hint_text='Nome')
        self.morada = TextInput(hint_text='Morada')
        self.telefone = TextInput(hint_text='Telefone')
        
        layout.add_widget(self.nome)
        layout.add_widget(self.morada)
        layout.add_widget(self.telefone)
        
        btn_submit = Button(text='Submeter', on_release=self.submit_cliente)
        btn_back = Button(text='Voltar', on_release=self.go_back)
        
        layout.add_widget(btn_submit)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def submit_cliente(self, instance):
        print(f'Nome: {self.nome.text}, Morada: {self.morada.text}, Telefone: {self.telefone.text}')
        self.clear_inputs()

    def go_back(self, instance):
        self.manager.current = 'home'

    def clear_inputs(self):
        self.nome.text = ''
        self.morada.text = ''
        self.telefone.text = ''

# Tela para adicionar hambúrgueres
class AddHamburguerScreen(Screen):
    def __init__(self, **kwargs):
        super(AddHamburguerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Adicionar Hamburguer'))
        
        self.nome_hamburguer = TextInput(hint_text='Nome do Hamburguer')
        self.ingredientes = TextInput(hint_text='Ingredientes')
        
        layout.add_widget(self.nome_hamburguer)
        layout.add_widget(self.ingredientes)
        
        btn_submit = Button(text='Submeter', on_release=self.submit_hamburguer)
        btn_back = Button(text='Voltar', on_release=self.go_back)
        
        layout.add_widget(btn_submit)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def submit_hamburguer(self, instance):
        print(f'Nome do Hamburguer: {self.nome_hamburguer.text}, Ingredientes: {self.ingredientes.text}')
        self.clear_inputs()

    def go_back(self, instance):
        self.manager.current = 'home'

    def clear_inputs(self):
        self.nome_hamburguer.text = ''
        self.ingredientes.text = ''

# Tela para adicionar pedidos
class AddPedidoScreen(Screen):
    def __init__(self, **kwargs):
        super(AddPedidoScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Adicionar Pedido'))
        
        self.id_cliente = TextInput(hint_text='ID do Cliente')
        self.nome_hamburguer = TextInput(hint_text='Nome do Hamburguer')
        self.quantidade = TextInput(hint_text='Quantidade', input_filter='int')
        self.tamanho = TextInput(hint_text='Tamanho (infantil, normal, duplo)')
        self.valor_total = TextInput(hint_text='Valor Total', input_filter='float')
        
        layout.add_widget(self.id_cliente)
        layout.add_widget(self.nome_hamburguer)
        layout.add_widget(self.quantidade)
        layout.add_widget(self.tamanho)
        layout.add_widget(self.valor_total)
        
        btn_submit = Button(text='Submeter', on_release=self.submit_pedido)
        btn_back = Button(text='Voltar', on_release=self.go_back)
        
        layout.add_widget(btn_submit)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def submit_pedido(self, instance):
        print(f'ID do Cliente: {self.id_cliente.text}, Nome do Hamburguer: {self.nome_hamburguer.text}, Quantidade: {self.quantidade.text}, Tamanho: {self.tamanho.text}, Valor Total: {self.valor_total.text}')
        self.clear_inputs()

    def go_back(self, instance):
        self.manager.current = 'home'

    def clear_inputs(self):
        self.id_cliente.text = ''
        self.nome_hamburguer.text = ''
        self.quantidade.text = ''
        self.tamanho.text = ''
        self.valor_total.text = ''

# Gerenciador de telas
class MyScreenManager(ScreenManager):
    pass

# Aplicativo principal
class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AddClienteScreen(name='add_cliente'))
        sm.add_widget(AddHamburguerScreen(name='add_hamburguer'))
        sm.add_widget(AddPedidoScreen(name='add_pedido'))
        return sm

if __name__ == '__main__':
    MyApp().run()
