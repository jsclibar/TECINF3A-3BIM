'''
PARTE 1 – Saída de Dados e Funções Simples

Exercício 1
Crie um código que imprima 3 mensagens diferentes usando print().
Depois, responda:

	•	O que o comando print() faz exatamente?
	•	Como o Python entende que estamos lidando com texto?

Exercício 2
Crie uma variável com seu nome e use len() para mostrar quantas letras ele tem.
Depois, responda:

	•	O que len() retorna?
	•	Esse valor serve pra quê, na prática?

Exercício 3
Peça para o usuário digitar algo e use isalpha() para verificar se ele digitou apenas letras.
Mostre uma mensagem personalizada com o resultado.
Depois, responda:

	•	Quando essa função pode ser útil em um jogo como o da forca?

PARTE 2 – Variáveis e Tipagem Dinâmica

Exercício 4
Crie uma variável x com o valor 5. Depois, mude o valor dela para "cinco".
Imprima o tipo da variável nas duas situações com type(x).

Depois, responda:

	•	O que você percebeu sobre o tipo da variável?
	•	Isso é uma vantagem ou desvantagem? Explique.

Exercício 5
Crie um programa que:

	1.	Solicite o nome do usuário
	2.	Solicite a idade
	3.	Mostre uma mensagem como: Olá, João! Você tem 17 anos.

Depois, explique:

	•	Qual foi o tipo de dado de cada variável (str, int, etc)?
	•	Como foi feita a junção dos dados na mensagem final?

PARTE 3 – Listas em Ação

Exercício 6
Crie uma lista chamada palavras com 5 palavras de sua escolha.

Depois, faça:

	•	Imprima o tamanho da lista
	•	Mostre o primeiro e o último item
	•	Percorra a lista e imprima os itens com um for

Responda:

	•	O que é uma lista? Para que ela serve?
	•	O que acontece se você tentar acessar um índice que não existe?

Exercício 7
Peça para o usuário digitar uma palavra. Verifique se essa palavra está dentro da lista palavras.
Mostre uma mensagem apropriada se estiver ou não.

Depois, explique:

	•	Como a verificação foi feita?
	•	Essa lógica pode ser usada em jogos? Dê um exemplo.

PARTE 4 – Condicional: if, elif, else

Exercício 8
Crie um programa que:

	1.	Peça para o usuário digitar sua idade
	2.	Mostre:
	•	“Você é criança” se idade < 12
	•	“Adolescente” se idade entre 12 e 17
	•	“Adulto” se idade entre 18 e 59
	•	“Idoso” se idade >= 60

Depois, responda:

	•	Qual a importância da indentação no if?
	•	O que muda se a ordem das condições for alterada?

PARTE 5 – Laços de Repetição

Exercício 9
Use for para imprimir os números de 1 a 5, um por linha.
Depois, explique o que cada parte do laço for está fazendo.

Exercício 10
Use while para pedir uma senha ao usuário até que ele digite "python123".
Mostre quantas tentativas ele usou.

Depois, responda:

	•	Quando usar while em vez de for?
	•	O que acontece se nunca colocarmos uma condição de parada?

PARTE 6 – Mini Desafio Prático: Lógica da Forca Simplificada

Crie um programa com a seguinte lógica:

	•	A palavra secreta é "morango".
	•	O usuário pode tentar adivinhar 5 letras (uma por vez).
	•	Cada vez que ele digitar uma letra, diga se está ou não na palavra.
	•	No final, mostre quantas letras ele acertou.

    # Dica de estrutura básica:
    palavra = "morango"
    tentativas = 5
    acertos = 0

Depois, responda:

	•	Como você armazenou os acertos?
	•	O que aconteceria se a palavra tivesse letras repetidas?
	•	Quais estruturas e funções básicas você usou para resolver?
'''