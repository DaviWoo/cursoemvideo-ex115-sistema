from sistema.sistema import *  # Importa todas as funções do arquivo "sistema.py"
from time import sleep
from termcolor import colored
import smtplib  # Importa a biblioteca que será usada para o envio do email



while True:  # Faz o looping do menu
    a = menu()  # Cria uma variável para receber o valor que menu() retorna
    if a == 4:  # Antecipa o valor de "a" para saber que opção o usuário escolheu antes de preparar o envio do email

        correio = verificar(a)  # correio recebe aquele dicionário com as informações do email
        obj = smtplib.SMTP('smtp.gmail.com: 587')  # Faz conexão com o servidor smtp do gmail
        obj.ehlo()  # Faz um ping para o servidor (diz um "Olá, mundo! Estou aqui!"
        obj.starttls()  # Criptografa a conexão para evitar problemas
        obj.login(correio['email'], correio['senha'])  # Faz login com o email e a senha dados
        obj.sendmail(correio["email"], correio["destino"], f'Subject: Lista de usuários cadastrados\n{correio["msg"]}'.encode('utf-8'))
        # Acima, o email é enviado. De "email" para "destino" com o assunto "Lista de usuários cadastrados" e a mensagem
        # novamente passando a mensagem para utf-8 para evitar problemas
        obj.quit()  # Encerra a conexão
        print(colored('Email enviado com sucesso!', 'green'))

        with open(f'{correio["path"]}/sistema.txt', 'r') as file:
            linhas = file.readlines()

        del linhas[0:3]
        del linhas[-3:-1]

        # O código acima e abaixo tiram o conteúdo que foi adicionado ao arquivo antes do envio do email

        with open(f'{correio["path"]}/sistema.txt', 'w') as file:
            file.writelines(linhas)



    else: verificar(a)  # Se não for a opção de enviar email, não é recebido um valor de retorno
    if a == 5: break




print(colored('Programa feito por: Davi', 'cyan'))
sleep(3)  # Créditos finais