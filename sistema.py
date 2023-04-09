from termcolor import colored  # Importando uma biblioteca que facilita o uso de cores
from time import sleep
from os import remove # Função que será usada para apagar todos os cadastros


def ponto(): # Essa função é só para deixar bonitinho, é opcional.
    sleep(0.35)
    print('.', end='')
    sleep(0.35)
    print('.', end='')
    sleep(0.35)
    print('.')
    sleep(0.35)


def menu():  # Função do Menu principal. Confirma que a opção é válida e retorna a opção escolhida
    linha('           MENU PRINCIPAL', last=False, num=25)
    linha(num=25, options=True)
    escolha = 0

    while True:
        try:
            escolha = int(input(colored('Sua opção: ', 'green')))

            while escolha not in [1, 2, 3, 4, 5]:
                escolha = int(input(colored('Sua opção: ', 'green')))
        except:
            print(colored('Digite uma opção válida', 'red'))
            continue
        break

    print('―'*25)

    return escolha


def linha(txt='', num=25, first=True, last=True, options=False):  # Função para facilitar o uso de linha
    if options is False:
        if first is True:
            print('―'*num)
        print(txt)
        if last is True:
            print('―'*num)

    elif options is True:
        choices = ['', 'Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Apagar todos os cadastros', 'Enviar cadastros por Email', 'Sair do Sistema']
        print('―'*num)
        for c in range(1,6):
            print(colored(f'{c} — ', 'yellow'), end='')
            print(colored(choices[c], 'cyan'))

        print('―'*num)



def verificar(option):  # Função que realiza ações dependendo da opção escolhida no menu
    path = 'C:/Users/DaviT/PycharmProjects/CursoemVideo/ex115/sistema' #Caminho do local onde um arquivo txt será criado
    if option == 1:
        print(colored('Procurando usuários cadastrados', 'yellow'), end='')
        ponto()
        try:
            with open(f'{path}/sistema.txt', 'r+') as file:  # Tenta achar um arquivo txt no caminho especificado
                print(file.read())  # Se achar um arquivo, printa os usuários registrados na tela

        except:  # Se der erro, isso é, se o programa NÃO ACHAR um arquivo "sistema.txt", responde dessa forma
            print(colored('Nenhum usuário foi cadastrado', 'red'))
            print(colored('Que tal começar seu primeiro cadastro? Digite 2', 'green'))
            sleep(3)
            pass  # Passa sem fazer nada

    if option == 2:
        linha(txt='            NOVO CADASTRO', first=False)
        nome = str(input('Nome: ')).strip()
        idade = 0

        while True:
            try: idade = int(input('Idade: '))
            except:
                print(colored('Digite uma idade válida', 'red'))
                continue
            break

        with open(f'{path}/sistema.txt', 'a+') as file:  # Abre "sistema.txt" no modo de adicionar conteúdo
            # Se não houver um arquivo "sistema.txt" em {path}, o programa o criará.
            file.write(f'\n{nome} - {idade}')  # Adiciona o nome e a idade no arquivo

    if option == 3:
        sn = str(input(colored('Confirme [S/N]: ', 'red'))).strip()[0].upper()
        while sn not in 'SN':
            sn = str(input(colored('Confirme [S/N]: ')))
        if sn == 'S': remove(f'{path}/sistema.txt')  # Chamada à função remove do módulo OS para apagar um arquivo
        elif sn == 'N': pass

    if option == 4:
        email = 'Email que o sistema usará para enviar o email'
        senha = 'A senha desse email'
        destino = str(input('Email de destino: '))
        while destino.isnumeric() or '@' not in destino:  # Validação básica de Email
            print(colored('Digite um email válido: ', 'red'))
            destino = str(input('Email de destino: '))
        msg = ''

        with open(f'{path}/sistema.txt', 'r') as file:
            content = file.readlines()  # A variável {content} recebe uma lista que contém cada linha em sistema.txt

        with open(f'{path}/sistema.txt', 'w', encoding='utf-8') as file:  # Adiciona uma mensagem antes da lista de usuários cadastrados
            # O parâmetro "encoding='utf-8'" foi usado para evitar conflitos com a codificação "ASCII" padrão para envio de emails
            file.write('\nComo solicitado, segue a lista dos usuários cadastrados:\n')
            file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            file.writelines(content)
            file.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nEmail enviado pelo programa de Davi')


        with open(f'{path}/sistema.txt', 'r', encoding='utf-8') as arquivo:
            msg = arquivo.read()  # Abre o arquivo mais uma vez para passar a mensagem do email a uma variável

        correio = {'email': email, 'senha': senha, 'destino': destino, 'msg': msg, 'path': path}

        return correio  # Retorna um dicionário com as informações usadas para enviar o email

    if option == 5:
        pass