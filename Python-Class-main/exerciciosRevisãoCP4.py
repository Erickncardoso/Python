#EX1 - Crie uma função que recebe várias strings e as junta em uma única string separada por espaço.
"""soma = " "
def junta(*args): #o args se torna uma tupla, e por isso, precisamos utilizar o for para realizar essa soma
    global soma
    for i in args:
        soma += i + " "  #o i esta percorrendo o args pois ele se tornou uma tupla(lista que nao pode ser alterada) e o i é cada elemento do arg
    return soma

print(junta("oi","tudo","bem"))"""


#Ex2 - Crie uma função chamada média que aceita um número variável de argumentos e retorna a média.

"""def media(*args):
    soma = 0
    med = 0
    for i in args:
        soma += i
        med = soma / len(args)
    return med
print(media(10,10,10))"""

#EX3 - Crie uma função lambda que retorne a soma de 3 números
"""a = lambda x,y,z: x+y+z
print(a(1,2,3))"""

#EX4 - Crie uma função lambda para inverter uma string
"""b = lambda x: x[::-1]
print(b("gabrielly"))"""

#EX 5 - Crie uma função lambda que verifica se a string é um palíndromo
"""c = lambda x: "É palíndromo" if x == x[::-1] else "Não é palíndromo" #ou apenas x == x[::-1] e ele retorna true or false 
print(c("arara"))"""

#List Comprehensions
#EX6 - Crie uma lista com os quadrados dos números de 1 a 10
"""x = [i*i for i in range(1,11)]
print(x)"""

#EX7 - Gere uma lista contendo apenas os números pares de 1 a 20
"""y = [i for i in range(1,21) if i%2==0]
print(y)"""

# EX8 - Crie uma lista contendo o comprimento de cada palavra na lista ["Python", "List", "Comprehension", "Exercícios"]
"""list = ["Python", "List", "Comprehension", "Exercícios"]
z = [len(i) for i in list]
print(z)"""

#EX9 - Converta uma lista de temperaturas em Celsius [0, 10, 20, 30, 40] para Fahrenheit usando a fórmula F = C * 9/5 + 32.
"""list1 = [0, 10, 20, 30, 40]
h = [i*9/5 + 32 for i in list1]
print(h)
"""

#EX10 - Gere uma lista com os números de 1 a 20, substituindo os múltiplos de 3 por "Fizz"

"""g = ["Fizz" if i%3==0 else i for i in range(1,21)]
print(g)"""

##EX11 - Dada a lista de palavras ["maçã", "banana", "uva", "morango", "abacaxi"], crie uma nova lista contendo apenas as palavras com mais de 5 letras
"""list2 = ["maçã", "banana", "uva", "morango", "abacaxi"]
l = [i for i in list2 if len(i)==5]
print(l)"""

#EX12 - Calcule o produto interno entre dois vetores (v e w)
#Se você tem dois vetores de mesmo tamanho, o produto interno (ou escalar) é: Multiplicar os elementos correspondentes e somar os resultados

"""v = [1, 2, 3]
w = [4, 5, 6]
result2 = 0
for i in range(len(w)):
    result = 0  #a variavel do resultado precisa estar dentro do for para zerar e começar de novo
    result += v[i] * w[i]
    result2 += result
print(result2)"""

#EX13 - Inicialize uma matriz de dimensões l x c atribuindo valores de 1 até l x c para os elementos da matriz.

"""l = 2
c = 2
matriz = []
for i in range(l):
    lista = []
    for j in range(c):
        lista.append(int(input("Digite os valores que gostaria de adicionar em sua matriz: ")))
    matriz.append(lista)  #esse append precisa estar fora do for para nãp repetir varias vezes
print(matriz)"""

#EX14 - Printe somente as colunas pares da matriz
"""def par():
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    pares = []
    for i in range(len(matriz)):
        lista = []
        for j in range(len(matriz[0])):
            if j%2 == 0:
                lista.append(matriz[i][j])
        pares.append(lista)
    return pares

print(par())"""

#EX15 - Printe somente as linhas impares da matriz*****

"""matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
impar = []
for i in range(len(matriz)):
    if i %2!=0:
        impar.append(matriz[i])
print(impar)
"""

#EX16 - Printe somente a diagonal da matriz
"""matriz = [
        [1, 2],
        [4, 5]
    ]

for i in range(len(matriz)):
    print(matriz[i][i])
    matriz[i][i]+=matriz[i][i] #preciso somar os dois juntos para pular ára o proximo """

#EX17 - Faça um programa que calcule o traço de uma matriz - soma dos elementos da diagonal
"""matriz = [
        [1, 2],
        [4, 5]
    ]
soma = 0
for i in range(len(matriz)):
    soma += matriz[i][i]
    matriz[i][i]+=matriz[i][i]
print(soma)"""

#EX18 - Faça um programa que calcule a soma de duas matrizes
"""matriza = [
        [1, 2],
        [4, 5]
    ]
matrizb = [
        [1, 2],
        [4, 5]
    ]
matrizc = []

if len(matriza) == len(matrizb) and len(matriza[0]) == len(matrizb[0]):
    for i in range(len(matriza)):  #para somar duas matrizes elas precisam ser iguais, por isso precisamos usar o if
        lista = []
        for j in range(len(matriza[0])):
            c = matrizb[i][j]+matriza[i][j]
            lista.append(c)
        matrizc.append(lista)
    print(matrizc)"""

#EX19 - Faça um programa que lhe dê a transposta de uma matriz

"""matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]

for i in range(len(matriz[0])):
    for j in range(len(matriz)):
        print(matriz[j][i], end = " ")
    print()"""

#EX20 - Faça um programa que calcule a multiplicação entre duas matrizes

"""matriza = [
        [1, 2],
        [4, 5]
    ]
matrizb = [
        [1, 2],
        [4, 5]
    ]
matrizc = []
for i in range(len(matriza)):
    for j in range(len(matriza[0])):
        s = matriza[i][j]*matrizb[i][j]
        matrizc.append(s)

print(matrizc)"""













