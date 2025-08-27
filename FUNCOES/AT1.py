'''
Atividades Práticas:

    1.	Crie uma função chamada boas_vindas() que exiba três mensagens diferentes.
    2.	Crie uma função linha() que imprima uma linha com 30 traços (-) e use-a antes e depois de uma mensagem central.
    3.	Monte uma função chamada menu() que mostre três opções no estilo:

        1 - Ver saldo
        2 - Sacar
        3 - Sair
'''

def boas_vindas():
    print("Olá, aluno(a)!")
    print("Seja bem-vindo à aula de funções em Python.")
    print("Vamos aprender a organizar melhor nossos programas!")

def linha():
    print("-" * 30)

def menu():
    print("MENU PRINCIPAL")
    print("1 - Ver saldo")
    print("2 - Sacar")
    print("3 - Sair")

#boas_vindas()

# Uso da função com uma mensagem no meio
#linha()
#print("Curso de Programação em Python")
#linha()

#menu()

while True:
    linha()
    menu()
    opcao = input("Escolha uma opção (ou 'sair'): ")
    if opcao.lower() == 'sair':
        break