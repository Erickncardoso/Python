#em matriz cada elemento precisa ter a mesma quantidade, precisa ter a mesma quantidade de colunas
#3x4 - 3 linhas e 4 colunas
#matriz é quadrada - linha = coluna
#matriz diagonal - é tudo zero com execeção da diagonal

#ex 0
#Faça um porgrama que o usuário entra com a qtd de colunas de uma lista e depois entre com os elementos
"""coluna = int(input("Digite a quantidade de colunas: "))
lista = []
contador = 0
while contador < coluna:
    elementos =input("Digite os elementos para adicionar: ")
    contador = contador + 1
    lista.append(elementos)
print(lista)"""

"""ou
c = int(input("Digitea qtde de colunas da matriz: "))
linha = []
for i in range(c):
    linha.append(int(input("Digite o valor: ")))
print(linha)"""

#ex1
#Faça um programa que leia a qtde de linhas e colunas e os elementos e forme a matriz

"""c = int(input("Digite a qtde de colunas: "))
l = int(input("Digite a qtde de linhas: "))
matriz = [] #precisamos colocar a matriz fora do codigo para adicionar
for i in range(l):
    lista = [] #a lista que vou add precisa estar dentro da repetição
    for g in range(c):
        elementos = int(input("Digite os elementos para adicionar: "))
        lista.append(elementos)
    matriz.append(lista)
    print(matriz)
"""

#ex2
#faça uma função que print a matriz bonitinha
"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7],
          ]
for i in matriz:
    for j in i:
        print(f"{j:2d}", end="")
    print()"""


#print matriz na diagonal
"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7],
          ]
a = 0
b = 0
for i in range(len(matriz)):
    print(matriz[a][b])
    a = a + 1
    b = b + 1"""

#printando por indice arrumado
"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7],
          ]
for i in range(len(matriz)):
    for j in range(len(matriz[0])): #pegamos qualquer linha da matriz para saber as colunas
        print(matriz[i][j], end='')
    print()"""


#consguimos alterar o vaor da matriz passando as coordenadas e atribuindo o outro valor
#por ex
"""        1    2   3
matriz =   1    2   3
           1    2   3

matriz[1][1]= 3 
o valor será substituido por 3"""


#tudo que eu altero em uma lista ele fica
"""a = [ 1,7,3]
b = a[:] #ou a.copy  //para copiar exatamente a lista, precisamos colocar essas informações 
a[0] = 2
print(a)
print(b)"""


#como printar matrizes
"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7]
          ]
ma = matriz.copy()
matriz[0]= 0 #desse jeito ele muda um e não outro 
print(ma)
print(matriz)"""
#para copiar todas as listas da matriz, precisamos percorrer a lista e copiar todos os elementos
"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7]
          ]
a = [i[:] for i in matriz] """ #se tenho uma lista que tem mais lista, precisamos percorrer e copiar tudo da lista

"""c = int(input("Digite a qtde de colunas: "))

m = [0 for i in range(c)]  #precisa passar a informação que quer na lista no primeiro i
print(m)"""




"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7],
          ]
for i in matriz:
        for j in i:
            j+= 1    #somando um em cada elemento da matriz
            print(f"{j:2d}", end="")
        print()"""

#print apenas as colunas pares da matriz
"""matriz = [[1,2,3],
          [2,3,4],
          [5,6,7],
          ]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i%2==0:
            print(matriz[i][j], end='')
        print()
    
"""