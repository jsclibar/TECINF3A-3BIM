# =====================================================
# PARTE 1 – Saída de Dados e Funções Simples
# =====================================================

# Exercício 1
print("Bem-vindo ao mundo Python!")
print("Aprender programação pode ser divertido.")
print("Vamos praticar bastante!")

# O que o comando print() faz exatamente?
# -> Ele exibe informações no console, ou seja, imprime mensagens na tela.

# Como o Python entende que estamos lidando com texto?
# -> Tudo que está entre aspas (simples ou duplas) é interpretado como texto (string).

# -----------------------------------------------------

# Exercício 2
nome = "Carlos"
print("Quantidade de letras:", len(nome))

# O que len() retorna?
# -> Retorna o número de caracteres da string, ou seja, o comprimento do texto.

# Esse valor serve pra quê, na prática?
# -> Pode ser usado para validar limites, criar condições ou exibir estatísticas.
# Por exemplo, verificar se o nome de usuário tem mais de 3 letras.

# -----------------------------------------------------

# Exercício 3
texto = input("Digite algo: ")
if texto.isalpha():
    print("Você digitou apenas letras!")
else:
    print("Você digitou algo que não é só letra.")

# Quando essa função pode ser útil em um jogo como o da forca?
# -> Para garantir que o jogador digitou uma letra válida e não números ou símbolos.
# Isso evita erros na lógica do jogo e mantém a coerência das regras.

# =====================================================
# PARTE 2 – Variáveis e Tipagem Dinâmica
# =====================================================

# Exercício 4
x = 5
print("Tipo de x:", type(x))  # int

x = "cinco"
print("Novo tipo de x:", type(x))  # str

# O que você percebeu sobre o tipo da variável?
# -> O tipo da variável mudou automaticamente de inteiro (int) para texto (str).

# Isso é uma vantagem ou desvantagem? Explique.
# -> É uma vantagem pela flexibilidade, mas pode causar erros difíceis de encontrar em programas maiores.
# Por isso, em projetos grandes é comum usar tipagem estática (como em linguagens como Java ou C++).

# -----------------------------------------------------

# Exercício 5
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
print(f"Olá, {nome}! Você tem {idade} anos.")

# Qual foi o tipo de dado de cada variável?
# -> nome = str (texto), idade = int (número inteiro, convertido com int()).

# Como foi feita a junção dos dados na mensagem final?
# -> Usamos f-string (f"...") que permite inserir variáveis diretamente entre chaves {}.

# =====================================================
# PARTE 3 – Listas em Ação
# =====================================================

# Exercício 6
palavras = ["gato", "cachorro", "pássaro", "peixe", "tartaruga"]

print("Tamanho da lista:", len(palavras))  # Retorna 5
print("Primeiro item:", palavras[0])      # Índice 0 = primeiro item
print("Último item:", palavras[-1])       # Índice -1 = último item

print("Itens da lista:")
for palavra in palavras:
    print(palavra)

# O que é uma lista? Para que ela serve?
# -> Lista é uma estrutura que armazena vários dados em uma única variável.
# Ideal para armazenar sequências: nomes, números, itens etc.

# O que acontece se você tentar acessar um índice que não existe?
# -> O Python retorna um erro do tipo IndexError.

# -----------------------------------------------------

# Exercício 7
palavra_usuario = input("Digite uma palavra: ")

if palavra_usuario in palavras:
    print("Essa palavra está na lista!")
else:
    print("Essa palavra NÃO está na lista.")

# Como a verificação foi feita?
# -> Com o operador "in", que verifica se um item está presente na lista.

# Essa lógica pode ser usada em jogos? Dê um exemplo.
# -> Sim! No jogo da forca, por exemplo, pode-se verificar se a letra digitada está na lista de letras da palavra secreta.

# =====================================================
# PARTE 4 – Condicional: if, elif, else
# =====================================================

# Exercício 8
idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é criança.")
elif idade < 18:
    print("Adolescente.")
elif idade < 60:
    print("Adulto.")
else:
    print("Idoso.")

# Qual a importância da indentação no if?
# -> Define os blocos de código que pertencem a cada condição. Sem ela, o código não funciona.

# O que muda se a ordem das condições for alterada?
# -> Pode gerar resultados incorretos. Ex: se colocar "idade < 60" antes de "idade < 12", toda idade abaixo de 60 cairia nesse bloco e as outras condições nunca seriam avaliadas.

# =====================================================
# PARTE 5 – Laços de Repetição
# =====================================================

# Exercício 9
for i in range(1, 6):
    print(i)

# O que cada parte do laço for está fazendo?
# -> range(1,6) gera números de 1 até 5.
# -> i recebe cada número dessa sequência, um por vez.
# -> print(i) mostra o valor atual.

# -----------------------------------------------------

# Exercício 10
tentativas = 0
senha = ""

while senha != "python123":
    senha = input("Digite a senha: ")
    tentativas += 1

print(f"Senha correta! Tentativas: {tentativas}")

# Quando usar while em vez de for?
# -> Quando não sabemos quantas vezes algo deve ser repetido, ou seja, enquanto uma condição for verdadeira.

# O que acontece se nunca colocarmos uma condição de parada?
# -> O programa entra em um **laço infinito**, que nunca termina. Isso pode travar o programa ou o computador.

# =====================================================
# PARTE 6 – Mini Desafio Prático: Lógica da Forca Simplificada
# =====================================================

palavra = "morango"
tentativas = 5
acertos = 0

for i in range(tentativas):
    letra = input(f"Tentativa {i+1} - Digite uma letra: ")
    if letra.lower() in palavra:
        print("Acertou!")
        acertos += 1
    else:
        print("Errou!")

print(f"Você acertou {acertos} letras.")

# Como você armazenou os acertos?
# -> Com a variável "acertos", que vai somando +1 toda vez que o usuário acerta uma letra.

# O que aconteceria se a palavra tivesse letras repetidas?
# -> Se o usuário digitar uma letra que aparece mais de uma vez, o programa vai contar apenas 1 acerto.

# Quais estruturas e funções básicas foram usadas?
# -> Variáveis, laço for, condição if, input, método lower() (para garantir que letra minúscula funcione), operador "in".