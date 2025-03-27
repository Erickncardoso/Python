#concatenação delas com exceção do primeiro caractere de cada uma.
"""palavra3 = "Gabrielly"
palavra4= "Fiap"
print(palavra3[1:]+ palavra4[1:])"""
from typing import final, reveal_type

from unicodedata import numeric

#concatenação de três cópias dos dois últimos caracteres.
"""palavra5= "Gabrielly"
print((palavra5[-2:])*3)"""

#Faça uma tabela mostrando os valores que i, j e n assumem depois de cada execução do laço while:

"""i=0
j=10
n=0
while i<j:
    print(i, j, n)
    i=i+1
    j=j-1
    n=n+1"""

#Faça um programa para exibiros números de 1 a 100
"""numero = 0
while numero <= 100:
    print(numero)
    numero+=1"""


#Faça um programa para exibiros números de 50 a 100
"""numero = 50
while numero <= 100:
    print(numero)
    numero+=1"""

#programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.
"""numero= 10
while numero <= 10 and numero >= 0:
    print(numero)
    numero = numero - 1
print("Fogo!")"""


#Faça um programa para imprimir de 1 até o número digitado pelo usuário, mostrando apenas os números pares.
"""num_usuario = int(input("Digite um número: "))
numero = 1
while numero <= num_usuario:
    print(numero)
    numero+=1"""


#Faça um programa para imprimir de 1 até o número digitado pelo usuário, mostrando apenas os números ímpares.
"""num_usuario = int(input("Digite um número: "))
numero = 1
while numero <= num_usuario:
    if numero%2 != 0:
        print(numero)
    numero+=1"""


#Faça um programa que dada uma lista de tamanho desconhecido contendo as notas de uma turma de alunos, retorne a média dessas notas.
"""notas = [10, 9, 8, 7, 9, 10, 3]  # Lista de notas
qtd_notas = len(notas)  # Quantidade de notas
media = sum(notas) / qtd_notas  # Calcula a média
print(f"A média das notas é: {media:.2f}")  # Exibe a média com 2 casas decimais"""

#Faça um programa para exibir os resultados da tabuada de um número digitado pelo usuário. Ex.: 2x1 = 2, 2x2 = 4, …
"""n_usuario=int(input("Digite o número que gostaria de ver a tabuada:"))
vezes = 0
while vezes < 10:
    vezes= vezes + 1
    valor= n_usuario*vezes
    print(n_usuario , "x" , vezes , "=" , valor)"""

#Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e terminar com 10.
"""n_usuario=int(input("Digite o número que gostaria de ver a tabuada: "))
vezes_usuario=int(input("Digite até qual valor gostaria de multiplicar: "))
vezes=0
while vezes < vezes_usuario:
    vezes= vezes + 1
    valor= n_usuario*vezes
    print(n_usuario , "x" , vezes , "=" , valor)"""



#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4
"""num1= 10
num2=9
vezes = 0
soma=0
while vezes < num2:
    vezes+=1
    soma+=num1
print(f"O resultado de {num1} x {num2} é: {soma}")"""


#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão.

"""num1=10
num2=2
divisao = 0

while num1 >= num2:
    num1-=num2
    divisao+=1


print(f"O resultado de {num1} / {num2} é: {divisao}")"""


#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

"""deposito= 1200
taxa= 0.05
meses= 24
contador= 0

while contador <= meses:
    print(f"Mês {contador + 1}: R$ {deposito:.2f}")
    contador+=1
    deposito= (deposito*taxa)+deposito
"""



#Faça um programa para interromper a execução do while assim que 0 for digitado
"""while True:
    numero=int(input("Digite um número:"))
    if numero == 0:
        break
"""

#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados
"""contador=0
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    contador += 1
    print(f"Foram digitados {contador}")
"""

#Escreva um programa para controlar uma pequena
#máquina registradora. Você deve solicitar ao usuário que digite o
#código do produto e a quantidade comprada. Utilize a tabela de
#códigos a seguir para obter o preço de cada produto:


"""print("código           preço")
print("   1              0.50 ")
print("   2              1.00 ")
print("   3              4.00 ")
print("   5              7.00 ")
print("   9              8.00 ")


total_compra = 0
while True:
    opcao = int(input("Digite o código do produto desejado, caso queira finalizar a compra, digite 0 :"))
    if opcao == 1:
        qtd_desejada = int(input("Digite a quantidade desejada:"))
        total_compra = total_compra + (0.50*qtd_desejada)
    elif opcao == 2:
        qtd_desejada = int(input("Digite a quantidade desejada:"))
        total_compra = total_compra + (1*qtd_desejada)
    elif opcao == 3:
        qtd_desejada = int(input("Digite a quantidade desejada:"))
        total_compra = total_compra + (4*qtd_desejada)
    elif opcao == 5:
        qtd_desejada = int(input("Digite a quantidade desejada:"))
        total_compra = total_compra + (7*qtd_desejada)
    elif opcao == 9:
        qtd_desejada = int(input("Digite a quantidade desejada:"))
        total_compra = total_compra + (8*qtd_desejada)
    elif opcao == 0:
        print(f"O total da sua compra foi de {total_compra} reais")
        break

    else:
        print("Codigo inválido")
        break
"""



































