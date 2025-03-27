#traço é a soma da diagonal
#transposta pe quando a linha vira coluna
# no CP vai precisar deixar tudo dentro de função, estudar como encaixar dentro da função



#faça um programa que calcule o traço de uma matriz
matriz = [[1,2,3],
          [2,3,4],
          [5,6,7],
          ]

"""def soma_diagonal(matriz):
    soma = 0  #a variavel da soma precisa estar fora do for, se não ela volta a ser 0 sempre
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

print(soma_diagonal(matriz))


#printar as colunas pares da matriz
def linhas_pares(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j%2==0:  #se trocar o j pelo i ele printa as linhas pares e coloca em baixo do for i a condição
                print(matriz[i][j], end='')
            print()


#printar as linhas impares da matriz
def linhas_impáres(matriz):
    for i in range(len(matriz)):
        if i % 2 != 0:
            for j in range(len(matriz[0])):
                      print(matriz[i][j], end=' ')
            print()
"""


#calculando a soma de duas matrizes // a somas
#para somar duas matrizes a qtd de linhas e colunas precisam ser iguais
"""matriza = [[1,2],
           [4,5]]
matrizb = [[1,2],
           [4,5]]

def somamatriz(matriza, matrizb):

    if len(matriza) == len(matrizb) and len(matriza[0]) == len(matrizb[0]):
        matrizc= []
    
        for i in range(len(matriza)):
            linha = []
            for j in range(len(matriza[0])):
                linha.append(matriza[i][j] + matrizb[i][j])
                matrizc.append(linha)
        return matrizc
    return - 1  #retorna caso não entre dentrodo if, pode retornar qualquer coisa """



#multiplicar dos elemnetos de cadalista

"""def prdt(a,b):
    soma = 0
    if len(a) == len(b):
        for i in range(len(a)):
            soma += a[i]*b[i]
    return soma
print(soma)"""




