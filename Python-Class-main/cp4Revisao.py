#Ex 1
#Escreva um programa que leia 2
#números do usuário e exiba o resultado de
#2a x 3b, em que a é o primeiro número e b
#o segundo

"""a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))

result = (2*a) * (3*b)
print(f'O resultado de (2x{a})x(2x{b}) é {result}')"""


#While
#O bloco é repetido enquanto a condição for verdadeira
#A condição é um expressão ou dado do tipo booleano
#O continue pula para a proxima execução do while

#Listas
#Para verificar se o elemento esta ou não em uma lista, usamos o in, ou seja:
#elento in lista
#Esse operador retorna True ou False caso o elemento esteja ou não
#na lista, respectivamente.
#Para adicionar elementos em uma lista, usamos o append:
#nomedalista.append(valorquequeratribuir)
#A operação de soma em listas gera uma nova lista que é o
#resultado de “grudar” lista2 ao final da lista1. Isto é conhecido
#como concatenação de listas
#lista1.extend(lista2): Concatena duas listas
#O operador “*” faz repetições da concatenação
#EXEMPLO:
lista1 = ["oi", "tudo","bem"]
lista2 = ["sim", "e","voce"]
lista1.extend(lista2)

#lista.insert(índice, dado) insere na lista o dado antes da posição
#índice
#del lista[posição] remove da lista o item da posição especificada;
#Também podemos remover um item da lista pelo valor utilizando o
#método remove;
#Podemos contar o número de elementos na lista com um certo
#valor usando o método count
#O método index é utilizado para obter a posição de um elemento
#em uma lista
#Outra opção para remover um elemento de uma lista é utilizando o
#método pop.
#O método pop recebe como parâmetro a posição do elemento a ser
#removido da lista. Caso o parâmetro seja omitido, o último
#elemento da lista será removido.
#Como resposta, o método retorna o elemento removido.
#Cada elemento da posição especificada até o fim da lista é
#realocado para a posição anterior
#O método reverse inverte a ordem dos elementos de uma lista.
#O método reverse não recebe nenhum parâmetro e modifica
#automaticamente a lista
#Uma lista pode ser ordenada utilizando o método sort.
#O método sort possui o parâmetro opcional reverse, que indica se
#a lista deve ser ordenada de forma crescente (False) ou
#decrescente (True). Por padrão, o valor desse parâmetro é False
#(ordenação crescente)
#Podemos usar a função sorted para obter uma cópia ordenada de
#uma lista, sem alterar a lista original
#Se quisermos uma cópia independente de uma lista podemos
#utilizar o método copy.
#O método copy retorna uma cópia da lista
#A função min retorna o menor valor em uma lista:
#A função max retorna o maior valor em uma lista:
#A função sum retorna a soma de todos os elementos de uma lista

#EX2
produtos = ["Caixa", "Lapís", "Caneta","Caneca", "Sapato"]

contador = 0
"""while True:
    escolha = input("Digite Adicionar se quiser adicionar um protudo e retirar se quiser retirar um prodtudo: ")
    if escolha == "adicionar":
        qtd = int(input("Digite a qtd de itens que gostaria de add: "))
        for i in range(qtd):
            add = input("Digite o produto que gostaria de adicionar: ")
            produtos.append(add)
        print(f"Produtos após adição: {produtos}")
    elif escolha == "retirar":
        ret = input("Digite o produto que gostaria de retirar")
        if ret in produtos:
            produtos.remove(ret)  #nesse caso não podemos usar o pop pois ele esperar o indice e não o valor
            print(f"Produto retirado. Produtos restantes: {produtos}")
        else:
            print("Esse produto não está em nossa lista")
    elif escolha == "sair":
        print("Saindo...")
        break
    else:
        print("Opção inválçida")
        continue
print("Inventário final de produtos:", produtos)
"""

#Funções
#def nome(parametros):
#    comandos
#    return valor do retorno

#Os parametros são variáveis que são inicializadas com valores indicados durante a chamada da função
#O comando return devolve para o invocador da função o resultado da execução desta

#O conceito de desempacotamento de parâmetros em Python está relacionado a funções que podem receber um número
# #indefinido de argumentos. Esse comportamento é útil quando não sabemos de antemão quantos parâmetros uma função deve aceitar.


#EX3 - Funções que recebem um número indeterminado de parâmetros
"""def soma(*args):  #o * serve para dizer que a função pode receber um número vari´vel de argumentos posicionais
    s = 0
    for x in args: #percorre os elemnetos dessa tupla 
        s += x
    return s

print(soma(1,3,4,5)) #o parâmetro args vai se tornar uma tupla com todos os argumentos passados para a função."""

#EX4 - Crie uma função que recebe várias strings e as junta em uma única string separada por espaço.

"""def soma_st(*args):
    st = " "
    for i in args:
        st = st + i + " "
    return st
print(soma_st("oi", "tudo", "bem"))"""

#Ex5 - Crie uma função chamada média que aceita um número variável de argumentos e retorna a média.

"""def media(*args):
    med = 0
    for i in args:
        med += i
    result = med / len(args)  #o resultado precisa ser calculado após o loop para a contar dar certo
    return result #return precisa estar na indentação da def 
print(media(10,10,10))"""

#Variaveis locais e Variaveis locais

#Uma variável é chamada local se ela é criada ou alterada dentro de uma função
#Nesse caso, ela existe somente dentro daquela função, e após o término da execução da mesma a variável deixa de existir

#Uma variável é chamada global se ela for criada fora de qualquer função.
#Essa variável pode ser visível por todas as funções

#Escopo de Variáveis
#O escopo de uma variável determina de quais partes do código ela pode ser acessada, ou seja, de quais partes do código a variável é visível.
#A regra de escopo em Python é bem simples:
#As variáveis globais são visíveis por todas as funções.
#As variáveis locais são visíveis apenas na função onde foram criadas.


#EX6 - Crie um programa que simule um banco, usando variáveis globais saldo e transacoes. Implemente as funções depositar(valor), sacar(valor) e extrato()

"""saldo = 0  #não esquecer de especificar que essas variaveis sao globais com "global nome"
transacoes = []

def depositar():
    global saldo
    global transacoes
    valor = float(input("Digite o valor: "))
    saldo += valor
    mens = "Deposito no valor de R$", valor
    transacoes.append(mens)
    return saldo

def sacar():
    global transacoes
    global saldo
    valor = float(input("Digite o valor: "))
    saldo -= valor
    mens1 = "Saque no valor de R$", valor
    transacoes.append(mens1)
    return saldo

def extrato():
    global transacoes
    global saldo
    print(f'Segue histórico de transações: {transacoes}')
    return transacoes

while True:
    escolha = input("Qual opção gostaria, depositar, sacar ou verificar o extrato: ")
    if escolha == "deposito":
        depositar()
    elif escolha == "saque":
        sacar()
    elif escolha == "extrato":
        extrato()
    else:
        print("Opção inválida")
        continue
"""

#Modulos - Funções que realizam tarefas comuns tais como cálculos matemáticos, manipulações de strings, manipulação de caracteres, programação Web, programação gráfica, etc

#Para usar uma função que está definida em um módulo, primeiro o programa deve importar o módulo usando o comando import:
"""import NomeDoModulo"""

#Após ter importado o módulo, o programa pode chamar as funções daquele módulo da seguinte forma:
"""NomeDoModulo.NomeDaFuncao(arg0,..., argn)"""

#Importa todos os elementos do módulo:
"""from NomeDoModulo import *"""
#(tomar cuidado por conta do nome de funções repetidas)
#Importa apenas a função nome-função:
"""from NomeDoModulo import nome-funcao"""


#Exemplo Módulos
#• Números aleatórios: random
#- randint
#- random
#- uniform
#- sample
#- shuffle
#Aguardar execução: time
#- sleep

#Arquivo um "calculadora"
"""import somasub   #importa os outros arquivos para a função funcionar aqui
import multidiv

num1= float(input("Digite o numéro 1:"))  #passa os paremetros das variaveis solicitando que o usuario coloque os numeros e a opção para realizar a conta 
num2= float(input("Digite o numéro 2:"))
op=input("Digite qual operação gostaria de realizar:")

if op == "+":      #colocar a condição para chamar as funções 
    print(somasub.soma(num1,num2))  #chamar as funções passando os parametros do num1 e num2 
elif op == "-":
    print(somasub.sub(num1,num2))
elif op == "*":
    print(multidiv.multi(num1,num2))
elif op == "/":
    print(multidiv.div(num1, num2))
else:
    print("Operação inválida")
    """

#Arquivo um "somasub"
"""def soma(num1,num2):  #contruindo a função e passando o parametro
    valor= num1+num2       #dando o nome de uma variavel para valor para podermos realizar a conta e achar o resultado 
    return valor        #retornando o valor para o codigo trazer o resultado 

def sub(num1,num2):
    valor = num1 - num2
    return valor
"""
#Arquivo um "multidiv"
"""def multi(num1, num2):
    valor = num1 * num2
    return valor


def div(num1, num2):
    valor = num1 / num2
    return valor"""

#Arquivo 1 - principal
#quando queremos puxar uma função desse modo, precisamos especificar de onde vamos puxare o que vamos puxar, poderiamos por exemplo deixar todas as funções em um local só
"""from contarpalavras import contar_palavras   
from contarvogais import contar_vogais
from reverterstring import  reverter


print(contar_vogais("Oi tudo bem com você?"))

print(reverter("Oi tudo bem com você?"))

print(contar_palavras("ooie, tudo bem? como você está?"))"""

#arquivo 2 - contar vogal
#para contar a quantidade de vogais dentro de uma string
"""def contar_vogais(palavra):
    qtde = 0
    for i in palavra   :
        if i =="a" or i =="e" or i == "i" or i == "o" or i == "u":
            qtde += 1
    return qtde"""


#arquivo 3 - contar palavra
"""def contar_palavras(texto):
    qtde = 1
    for i in texto:
        if i == " ":
            qtde+=1
    return qtde"""

#arquivo 4 - reverter
#para reverter uma string
"""def reverter(palavra):
    return palavra[::-1]#::começo- fim -1 olhar ao contrario"""


#Função Lambda
#Apenas funções simples (única expressão) podem ser definidas nessa notação
"""lambda <parâmetros>: <código com retorno>"""


"""a = lambda x: x*2    #escreveu lambda, passou o parametro que no caso é o x e depois dos : colocou o que ele quer que faça com o parametro
print(a(2))"""
"""b = lambda x, y: x * y   #Podemos passar um ou mais parametros
print(b(2, 3))"""

"""c = lambda k: k.lower()
print(c('OLA'))"""

#EX1 - Crie uma função lambda que retorne a soma de 3 números
"""soma = lambda x,y,z: x+y+z
print(soma(1,2,3))"""

#ex2 - Crie uma função lambda para inverter uma string

"""reverte = lambda x: x[::-1]  #passei o parametro da lambda e depois sinalizei que quero inverter o indice x 

print(reverte("Oi tudo bem"))"""

#EX 3 - Crie uma função lambda que verifica se a string é um palíndromo
"""palindromo = lambda x: x == x[::-1]
print(palindromo("arara"))"""

#ou podemos utilizar o if da seguinte forma:
"""palindromo = lambda x: "É palíndromo" if x == x[::-1] else "Não é palíndromo"  #podemos passar true or false em vez da string"""

#List Comprehensions
#Forma simples de criar listas

"""L = [x for x in range(10)]
P = [x for x in range(10) if x % 2 == 0]  #primeiro cria a lista com o for para percorrer e depois passa a condição if 
print(P)
print(L)"""

#EX1 - Crie uma lista com os quadrados dos números de 1 a 10
"""quadrados = [i*i for i in range(11)]  #colocar ate o 11 pois para em um anterior, o que você quer que aconteça com o indice precisa sert colocado a frente da lista, no primeiro indice
print(quadrados)"""

#EX2 - Gere uma lista contendo apenas os números pares de 1 a 20
"""num_pares =  [ i for i in range(1,21) if i%2 == 0]
print(num_pares)"""

# EX3 - Crie uma lista contendo o comprimento de cada palavra na lista ["Python", "List", "Comprehension", "Exercícios"].
"""lista = ["Python", "List", "Comprehension", "Exercícios"]
comprimento = [len(i) for i in lista]
print(comprimento)"""

#EX4 - Converta uma lista de temperaturas em Celsius [0, 10, 20, 30, 40] para Fahrenheit usando a fórmula F = C * 9/5 + 32.
"""temp = [0, 10, 20, 30, 40]
convert = [(i*9/5 + 32) for i in temp]
print(convert)
"""

#EX5 - Gere uma lista com os números de 1 a 20, substituindo os múltiplos de 3 por "Fizz"
"""multi_3 = ["Fizz" if i%3 == 0 else i for i in range(1,21)]  #nesse caso colocamos a condição if em primeiro e colocamos o else após com apenas o list comprehensions
print(multi_3)  #caso queria colocar m,ais de uma condição if, basta colocar ao final da lista"""

#EX6 - Dada a lista de palavras ["maçã", "banana", "uva", "morango", "abacaxi"], crie uma nova lista contendo apenas as palavras com mais de 5 letras

"""palavras = ["maçã", "banana", "uva", "morango", "abacaxi", "gabis"]

contagem = [i for i in palavras if len(i) == 5]
print(contagem)"""

#math case
#Estrutura concisa: Permite que transformar estruturas aninhadas com ramificações complexas de forma concisa e legível.
#Legibilidade: Com sua sintaxe clara, torna o código legível e autoexplicativo
#Segurança: Possibilita que todos os padrões possíveis sejam tratados em cada Case

"""match <expressão>:
    case <valor 1>:
    <instruções>
    case <valor 2>:
    <instruções>"""

#EX1 - Calcule o produto interno entre dois vetores (v e w)
#Se você tem dois vetores de mesmo tamanho, o produto interno (ou escalar) é: Multiplicar os elementos correspondentes e somar os resultados
"""v = [1, 2, 3]
w = [4, 5, 6]
percorre = 0

for i in range(len(v)):  # o i percorre a lista e vai virando 0,1,2,3,4.....
    percorre += v[i] * w[i]  # a variavel percorre armazena o resultado pq ela vai tento o valor da multiplicação e vai somando 

print(percorre)"""


#matrizes e obj multidimensional
#Esses tipos de dados nos permitem armazenar informações mais complexas em uma única variável

#matrizes
#Uma matriz é um objeto bidimensional, formada por listas, todas do mesmo tamanho
"""Exemplo de declaração de uma matriz 2 × 2"""
"""matriz = [
    [1, 2], # linha 1
    [3, 4] # linha 2
]"""
#exemplo
"""l = int(input("Entre com o número de linhas: "))  #pedindo para o usuario as informações de linhas e colunas
c = int(input("Entre com o número de colunas: "))
matriz = []  #criando a "lista" onde ficara a matriz
for i in range(l): #esse for roda uma vez e cria as linhas // Cada vez que começa a criar uma linha nova, você cria uma lista vazia chamada linha
    linha = []
    for j in range(c):  #percorre a coluna
        linha.append(int(input("Digite os números: "))) # recebendo os dados
    matriz.append(linha)
print(matriz)"""


#EX1 - Inicialize uma matriz de dimensões l x c atribuindo valores de 1 até l x c para os elementos da matriz.
"""l = 3
c = 3
matriz = []

for i in range(l):
    lista = []
    for j in range(c):
        lista.append(int(input("Digite os números que gostaria de adicionar: ")))
    matriz.append(lista)
print(matriz)"""

#Acessando elementos de uma matriz
#Note que uma matriz é uma lista de listas.
#Podemos acessar um elemento de uma matriz, localizado em uma determinada linha e coluna
"""matriz[linha][coluna]""" #igual matriz[i][i]

#caso tente acessar uma posição inexistente, um erro é gerado

#Alterando elementos de uma matriz
#podemos alterar elementos de uma matriz, localizado em uma determinada linha e coluna.
"""matriz[linha][coluna] = valor""" #ou seja, estamos passando as "coordenadas" do local que gostariamos de alterar, para isso precisamos passar a linha e a coluna


#Criando uma copia de uma Matriz
#Para criar uma cópia de uma matriz, precisamos criar uma nova matriz com as cópias de cada uma das linhas da matriz original
"""A = [[1, 2], [3, 4]]
B = A.copy() """ # colocamos a matriz que gostariamos de copiar .copy()
#desse modo, tudo que alterarmos dentro da matriz b, será alterado na a tambem, isso acontece por que:
# Você está copiando a lista "de fora", mas as listas de dentro continuam as mesmas.
#Ou seja:
#A e B compartilham as mesmas listas internas ([1, 2] e [3, 4]).
#Se você mudar algo dentro dessas listas, vai afetar as duas matrizes.

#Criando uma cópia de uma Matriz separadas
"""A = [[1, 2], [3, 4]]
B = [linha.copy() for linha in A]"""  #A linha é apenas uma variavel criada para copiar cada indice percorrido da lista, podemos atribuir qualquer nome a ele // O for percorre a lista e é add no B
#Podemos copíar de varias formas, segue exemplos:

"""A = [[1, 2], [3, 4]]
B = [linha[:] for linha in A]"""

"""A = [[1, 2], [3, 4]]
B = [list(linha) for linha in A]"""

#linha é uma variavel de apoio, usamos para representar cada item da lista (ou seja, cada linha da matriz). Essa variável não existe antes do código rodar, ela é criada automaticamente durante o processo de iteração (o for)


#Objetos multidimensionais
#Até agora criamos matrizes bidimensionais, mas podemos criar objetos com mais dimensões.
#Podemos criar objetos com d dimensões utilizando a mesma ideia de listas de listas

#Exemplo de um objeto com dimensões 2 × 2 × 2:
"""obj = [
    [[1, 2], [3, 4]], #ou seja, duas linhas, duas "Listas" dentro de uma e duas colunas em cada 
    [[5, 6], [7, 8]]
]"""

#Podemos acessar um elemento em um objeto com dimensões da seguinte forma
#objeto[i][i]...[i]

#Podemos alterar um elemento em um objeto com dimensões
#objeto[i][i]...[i] = valor

#EX 1 - Usando o matplotlib faça a imagem de um tabuleiro de xadrez

#import matplotlib.pyplot as plt
#Esse comando importa a biblioteca matplotlib.pyplot, que é usada para criar gráficos, imagens e visualizações em Python.
#A gente está dando o apelido de plt pra facilitar quando for chamar as funções dessa biblioteca depois

# Coordenadas rgb de x e y
"""matriz_rgb = [
    [[rx1y1, gx1y1, bx1y1], [rx1y2, gx1y2, bx1y2], [rx1y3, gx1y3, bx1y3]],
    [[rx2y1, gx2y1, bx2y1], [rx2y2, gx2y2, bx2y2], [rx2y3, gx2y3, bx2y3]],
    [[rx3y1, gx3y1, bx3y1], [rx3y2, gx3y2, bx3y2], [rx3y3, gx3y3, bx3y3]],
]"""

#Cada par de colchetes interno [[r, g, b], [r, g, b], ...] representa um pixel da imagem. A cor desse pixel é dada pelos valores r, g, b:
#r → quantidade de vermelho (Red)
#g → quantidade de verde (Green)
#b → quantidade de azul (Blue)

"""plt.imshow(matriz_rgb)"""
#A função imshow() exibe uma imagem a partir de uma matriz de pixels.
#No caso, ela pega a matriz_rgb e transforma em uma imagem colorida, onde cada pixel tem a cor que você definiu com RGB.

"""plt.axis('off')"""
#Remove os eixos X e Y que normalmente aparecem em um gráfico.
#Isso deixa a imagem mais limpa, sem números ou marcações de eixo

"""plt.show()"""
#Manda o matplotlib mostrar a imagem na tela.
#Tudo que foi configurado antes (imshow, axis, etc.) vai aparecer agora

#EXEMPLO:
"""import matplotlib.pyplot as plt  #para instalar usamos o comando pip install matplotlib no terminal 
import numpy as np  # biblioteca para trabalhar com arrays mais fácil

# Cria uma matriz 8x8, alternando 0 e 1
tabuleiro = np.zeros((8, 8, 3))  # 8 linhas, 8 colunas, 3 cores (R,G,B)

# Preenche os quadrados
for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            cor = [1, 1, 1]  # Branco (RGB = 1,1,1)
        else:
            cor = [0, 0, 0]  # Preto (RGB = 0,0,0)
        tabuleiro[linha, coluna] = cor  # Define a cor do quadrado

# Exibe o tabuleiro
plt.imshow(tabuleiro)
plt.axis('off')
plt.show()"""

#EX1 - Printe somente as colunas pares da matriz

"""l = int(input("Digite a qtde de linhas que gostaria de ter na matriz: "))
c = int(input("Digite a qtde de colunas que gostaria de ter na matriz: "))

matriz = []
def criando_matriz():
    global l
    global c
    global matriz
    for i in range(l):
        lista = []
        for j in range(c):
            lista.append(int(input("Digite os valores dentro da matriz: ")))
        matriz.append(lista)
    return matriz

print(criando_matriz())


def get_colunas_pares(matriz):
    colunas_pares = []

    for i in range(len(matriz)):
        linha_pares = []
        for j in range(len(matriz[0])):
            if j % 2 == 0:
                linha_pares.append(matriz[i][j])  #atribui o resultado dentro de uma lista para retornar
        colunas_pares.append(linha_pares) #atribui a lista do resultado para trazer o retorno da variavel 

    return colunas_pares"""

#EX2 - Printe somente as linhas impares da matriz
"""l = int(input("Digite a qtde de linhas que gostaria de ter na matriz: "))
c = int(input("Digite a qtde de colunas que gostaria de ter na matriz: "))
matriz = []
def criando_matriz():
    global l
    global c
    global matriz
    for i in range(l):
        lista = []
        for j in range(c):
            lista.append(int(input("Digite os valores dentro da matriz: ")))
        matriz.append(lista)
    return matriz

print(criando_matriz())

linhas_impares = []
def impares(matriz):
    global linhas_impares
    for i in range(len(matriz)):
        if i % 2 != 0:  # Se a linha for ímpar
            linhas_impares.append(matriz[i])  # Adiciona a linha inteira
    return linhas_impares
print(impares(matriz))"""

#EX4 - Printe somente a diagonal da matriz

"""matriz = [[1,2,3],
          [3,5,4],
          [6,7,5]
]

for i in range(len(matriz)):  #leio a matriz para contar a qtd de vezes que preciso realizar o for
    print(matriz[i][i]) #printo o primeiro i da diagonal
    matriz[i][i] += 1 #somo o primeiro i com o primeiro i + 1 para "pular" para o proximo i """


#EX5 - Faça um programa que calcule o traço de uma matriz
"""matriz = [[1,2,3],
          [3,5,4],
          [6,7,5]
]

def soma_traço(matriz):
    soma = 0  #soma para realizar o calculo
    for i in range(len(matriz)):  #for para percorrer a matriz e len matriz para passar quantas vezes precisa relaizar o for
        soma += matriz[i][i]  #o i como parametro porque ele começa igual a 0, ou seja, ele vai percorrer o [0][0] da matriz, depois ele vira 1, emtão ele vai para o [1][1] da matriz, que a proxima linha e proxima coluna
    return soma
print(soma_traço(matriz))"""


#EX6 - Faça um programa que calcule a soma de duas matrizes
# EX6 - Faça um programa que calcule a soma de duas matrizes
# calculando a soma de duas matrizes // a somas

"""matriza = [[1,2],
           [4,5]]
matrizb = [[1,2],
           [4,5]]

def somamatriz(matriza, matrizb):

    if len(matriza) == len(matrizb) and len(matriza[0]) == len(matrizb[0]): # para somar duas matrizes a qtd de linhas e colunas precisam ser iguais, por isso a condição if
        matrizc= []

        for i in range(len(matriza)):
            linha = []
            for j in range(len(matriza[0])):
                linha.append(matriza[i][j] + matrizb[i][j])
                matrizc.append(linha)
        return matrizc
    return - 1  #retorna caso não entre dentrodo if, pode retornar qualquer coisa"""


#EX7 - Faça um programa que lhe dê a transposta de uma matriz
"""matriza = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriza[0])):  # colunas da matriz original
    for j in range(len(matriza)):  # linhas da matriz original
        print(matriza[j][i], end=" ")  # troca o índice
    print()  # pula pra próxima linha da transposta"""


#EX 8 - Faça um programa que calcule a multiplicação entre duas matrizes
"""matriza = [[1,2],
           [4,5]]
matrizb = [[1,2],
           [4,5]]

def somamatriz(matriza, matrizb):

    if len(matriza) == len(matrizb) and len(matriza[0]) == len(matrizb[0]): # para somar duas matrizes a qtd de linhas e colunas precisam ser iguais, por isso a condição if
        matrizc= []

        for i in range(len(matriza)):
            linha = []
            for j in range(len(matriza[0])):
                linha.append(matriza[i][j] * matrizb[i][j])
                matrizc.append(linha)
        return matrizc
print(somamatriz(matriza,matrizb))
"""






