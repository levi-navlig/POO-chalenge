from guizero import App, Text, TextBox, PushButton, Box, Window, error, info
from main import cadastrar, logar, buscar, excluir

def dados_excluir():
    excluir(input_excluir_janela.value, info, error)

def voltar_cadastro():
    cadastro.hide()
    janela.enable()
    
def voltar_janela():
    janela.hide()
    login.show()
    
def dados_buscar():
    buscar(input_busca_janela.value, info, error)
    
def dados_cadastrar():
    cadastrar(input_usuario_cadastro.value, input_senha_cadastro.value, cadastro, login, info, error)

def dados_logar():
    logar(input_usuario_login.value, input_senha_login.value, login, janela, info, error)
    
def ir_cadastro():
    janela.disable()
    cadastro.show()
    cadastro.enable()

def cancelar():
    login.destroy()
    print('app canceled.')


login = App(title='Login', width=300, height=200, bg='#b3daff')
login.tk.resizable(0, 0)
login.text_color = '#001a00'

Text(login, text='Login')
top_box_login = Box(login, align='top', border=False, layout='grid',)
Text(top_box_login, text='Usuário:', grid=[0, 1])
Text(top_box_login, text='Senha:', grid=[0, 2])
input_usuario_login = TextBox(top_box_login, width=30, grid=[1, 1])
input_senha_login = TextBox(top_box_login, width=30, grid=[1, 2], hide_text=True)
input_usuario_login.bg = '#ffffff'
input_senha_login.bg = '#ffffff'
bottom_box_login = Box(login, align='bottom', border=False, layout='grid')
botao_enviar_login = PushButton(bottom_box_login, text='Enviar', command=dados_logar, grid=[0, 0],)
botao_cancelar_login = PushButton(bottom_box_login, text='Cancelar', command=cancelar, grid=[1, 0])
botao_enviar_login.bg = '#99ceff'
botao_cancelar_login.bg = '#99ceff'

janela = Window(login, title='Janela', width=300, height=200, bg='#b3daff')
login.tk.resizable(0, 0)
janela.text_color = '#001a00'

Text(janela, text='Janela principal')
top_box_janela = Box(janela, align='top', border=False, layout='grid')
Text(top_box_janela, text='Buscar:', grid=[0, 0])
input_busca_janela = TextBox(top_box_janela, width=30, grid=[1, 0])
input_busca_janela.bg = '#ffffff'
Text(janela, text='Obs: para busca, utilize usuário ou código', size=8)
middle_box_janela = Box(janela, border=False, layout='grid')
Text(middle_box_janela, text='Excluir:', grid=[0, 0])
input_excluir_janela = TextBox(middle_box_janela, width=30, grid=[1, 0])
input_excluir_janela.bg = '#ffffff'
Text(janela, text='Obs: para excluir, utilize o código de usuário', size=8)
bottom_box_janela_I = Box(janela, align='bottom', border=False, layout='grid')
bottom_box_janela_II = Box(janela, align='bottom', border=False, layout='grid')
botao_voltar_janela = PushButton(bottom_box_janela_I, text='Voltar', command=voltar_janela, grid=[0, 0])
botao_cadastar_janela = PushButton(bottom_box_janela_I, text='Cadastrar', command=ir_cadastro, grid=[1, 0])
botao_cancelar_janela = PushButton(bottom_box_janela_I, text='Cancelar', command=cancelar, grid=[2, 0])
botao_buscar_janela = PushButton(bottom_box_janela_II, text='Buscar', command=dados_buscar, grid=[0, 1], image='lupa.png')
botao_excluir_user_janela = PushButton(bottom_box_janela_II, text='Excluir', command=dados_excluir, grid=[1, 1], image='lixo.png')
botao_voltar_janela.bg = '#99ceff'
botao_cadastar_janela.bg = '#99ceff'
botao_cancelar_janela.bg = '#99ceff'
botao_buscar_janela.bg = '#99ceff'
botao_excluir_user_janela.bg = '#99ceff'



cadastro = Window(login, title='Cadastro', width=300, height=200, bg='#b3daff')
cadastro.tk.resizable(0, 0)
cadastro.text_color = '#001a00'

Text(cadastro, text='Cadastro')
top_box_cadastro = Box(cadastro, align='top', border=False, layout='grid')
Text(top_box_cadastro, text='Usuário:', grid=[0, 1])
Text(top_box_cadastro, text='Senha:', grid=[0, 2])
input_usuario_cadastro = TextBox(top_box_cadastro, width=30, grid=[1, 1])
input_senha_cadastro = TextBox(top_box_cadastro, width=30, grid=[1, 2], hide_text=True)
input_usuario_cadastro.bg = '#ffffff'
input_senha_cadastro.bg = '#ffffff'
Text(cadastro, text='Obs: Usuários ou senhas com espaço serão invalidados', size=8)
bottom_box_cadastro = Box(cadastro, align='bottom', border=True, layout='grid')
botao_voltar_cadastro = PushButton(bottom_box_cadastro, text='Voltar', command=voltar_cadastro, grid=[0, 0])
botao_enviar_cadastro = PushButton(bottom_box_cadastro, text='Enviar', command=dados_cadastrar, grid=[1, 0])
botao_cancelar_cadastro = PushButton(bottom_box_cadastro, text='Cancelar', command=cancelar, grid=[2, 0])

janela.hide()
cadastro.hide()
login.display()
