from Userfile import User
from random import randint


def excluir(codigo, info, error):
    with open('data.txt', 'r', encoding='utf=8' )as arq:
        linhas = arq.readlines()
        with open('data.txt', 'w', encoding='utf=8' )as arq_w:
            for linha in linhas:
                lista_linha = linha.split()
                if codigo == lista_linha[2]:
                    linhas.remove(linha)
                    info('Excluir', 'Usuário excluído')
                    break
                else:
                    continue
            else:
                error('Excluir', 'Usuário não encontrado')
            for linha_f in linhas:
                arq_w.write(linha_f)    
                
                
def buscar(input_busca_janela, info, error):
     with open('data.txt', 'r', encoding='utf=8' )as arq:
        for linha in arq:
            objeto = linha.split()
            if objeto[2] == input_busca_janela:
                mensagem = f'Seu usuário é {objeto[0]} e seu codigo é {objeto[2]}'
                info('Buscar', mensagem)
                break
            elif objeto[0] == input_busca_janela:
                mensagem = f'Seu usuário é {objeto[0]} e seu codigo é {objeto[2]}'
                info('Buscar', mensagem)
                break
            else:
                pass
        else:
            error("Busca", "Usuário ou código inexistente")


def fazedor_codigo():
    user_codigo = randint(1, 1000)
    with open('data.txt', 'r', encoding='utf=8' )as arq:
        for linha in arq:
            objeto = linha.split()
            if objeto[2] != user_codigo:
                pass
            else:
                fazedor_codigo()
    return user_codigo


def cadastrar(usuario_cadastro, senha_cadastro, cadastro, login, info, error):
    objeto_user = User(usuario_cadastro, senha_cadastro, fazedor_codigo())
    count = 0
    with open("data.txt", "r+", encoding="utf-8") as arq:
        if objeto_user.usuario.count(' ') == 0 and objeto_user.senha.count(' ') == 0:
            for linha in arq:
                objeto = linha.split()
                if objeto[0] == objeto_user.usuario:
                    count += 1
                else:
                    pass
            if count == 0:
                arq.write(f'{objeto_user.usuario} {objeto_user.senha} {objeto_user.codigo}\n')
                info('Cadastrar', 'Usuario cadastrado com sucesso')
                cadastro.hide()
                login.show()
            elif count > 0:
                error('Cadastrar', 'Usuário já existente')
        else:
            error('Cadastrar', 'Usuario ou senha com caracteres invalidos: não pode espaço')


def logar(usuario_login, senha_login, login, janela, info, error):
    with open("data.txt", "r", encoding='utf=8') as arq:
        for linha in arq:
            objeto = linha.split()
            if objeto[0] == usuario_login and objeto[1] == senha_login:
                info("Login", "Login bem-sucedido!")
                login.hide()
                janela.show()
                break
            else:
                pass
        else:
            error("Login", "Usuário ou senha incorretos")
