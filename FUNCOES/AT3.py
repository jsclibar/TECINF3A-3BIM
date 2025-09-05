''''

1. Crie uma função dobro(valor) que receba um número e retorne o dobro desse número.

2. Crie uma função area_retangulo(base, altura) que calcule e retorne a área de um retângulo.

3. Crie uma função calcula_media(n1, n2, n3) que calcule a média de três notas e retorne esse valor.
   Depois, use o valor retornado para dizer se o aluno foi aprovado (média ≥ 7) ou reprovado.

4. Crie uma função raiz_quadrada(numero) que retorne a raiz quadrada de um número. #Dica: Importe a biblioteca math e use a função sqrt.

5. Crie uma função fatorial(n) que calcule o fatorial de um número inteiro (ex: 5! = 5x4x3x2x1).

6. Crie uma função conversor_temperatura(celsius) que converta uma temperatura em graus Celsius para Fahrenheit e retorne o valor convertido.
   Use a fórmula:
   F = C x 1.8 + 32

'''

def dobro(valor):
    return valor * 2

# Teste
resultado = dobro(5)
print("Dobro:", resultado)

def area_retangulo(base, altura):
    return base * altura

# Teste
print("Área:", area_retangulo(4, 6))

def calcula_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Teste
media = calcula_media(7, 8, 6)
print("Média:", media)
if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")

import math

def raiz_quadrada(numero):
    return math.sqrt(numero)

# Teste
print("Raiz quadrada:", raiz_quadrada(25))

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Teste
print("Fatorial de 5:", fatorial(5))

def conversor_temperatura(celsius):
    return celsius * 1.8 + 32

# Teste
print("Temperatura em Fahrenheit:", conversor_temperatura(25))