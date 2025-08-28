''''

Atividades Práticas:

    1. Crie uma função que receba um nome como parâmetro e exiba uma mensagem personalizada entre duas linhas de traços.
    Exemplo de saída:

    ------------------------------
    Olá, JOSÉ CARLOS!
    ------------------------------

    2. Crie uma função que receba a idade de uma pessoa e informe se ela é maior ou menor de idade.
    Exemplo de saída:

    Idade: 15 → Menor de idade  
    Idade: 22 → Maior de idade

    3. Crie uma função que receba uma mensagem e uma quantidade de vezes, e exiba a mensagem repetida conforme o número indicado.
    Exemplo de chamada:

    repetir_mensagem("Estudar é importante!", 3)

    4. Crie uma função que receba um número inteiro e exiba a tabuada de multiplicação dele, de 1 até 10.
    Exemplo de saída:

    5 x 1 = 5  
    5 x 2 = 10  
    ...  
    5 x 10 = 50

    5. Crie uma função que classifique a pessoa de acordo com a idade:

        •	Menor que 12 → Criança
        •	De 12 a 17 → Adolescente
        •	De 18 a 59 → Adulto
        •	60 ou mais → Idoso

    6. Crie uma função que receba o nome de uma pessoa e o turno (M = manhã, T = tarde, N = noite) e exiba uma saudação apropriada.
    Exemplo:

    mensagem_personalizada("Fernanda", "T")
    # Saída: Boa tarde, Fernanda!

'''

def exibe_nome_formatado(nome):
    print("-" * 30)
    print(f"Olá, {nome.upper()}!")
    print("-" * 30)

def verifica_maioridade(idade):
    if idade >= 18:
        print(f"Idade: {idade} → Maior de idade")
    else:
        print(f"Idade: {idade} → Maior de idade")

def repetir_mensagem(msg, quantidade):
    for i in range(quantidade):
        print(msg)

def mostra_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def categoria_idade(idade):
    if idade < 12:
        print("Criança")
    elif idade < 18:
        print("Adolescente")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")

def mensagem_personalizada(nome, turno):
    if turno == "M":
        print(f"Bom dia, {nome}!")
    elif turno == "T":
        print(f"Boa tarde, {nome}!")
    elif turno == "N":
        print(f"Boa noite, {nome}!")
    else:
        print("Turno inválido.")

# Exemplo de teste
exibe_nome_formatado("José Carlos")

# Exemplos de teste
verifica_maioridade(15)
verifica_maioridade(22)

# Exemplo de teste
repetir_mensagem("Estudar é importante!", 3)

# Exemplo de teste
mostra_tabuada(5)

# Exemplos de teste
categoria_idade(7)
categoria_idade(15)
categoria_idade(35)
categoria_idade(70)

# Exemplos de teste
mensagem_personalizada("Fernanda", "T")
mensagem_personalizada("João", "N")
mensagem_personalizada("Lucas", "X")