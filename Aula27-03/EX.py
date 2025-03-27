# 1
def f(x):
    if x <= -2:
        return x**2 + 3*x - 4
    elif x < 0:
        return 2*x + 5
    elif x < 4:
        return x**(1/2)
    elif x < 6:
        return x**3 - 3*x**2 - 10*x
    elif x < 8:
        return x**2 - 4*x - 20
    else:
        return 10

# 2

def le_matriz(l, c):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(float(input(f'm[{i}][{j}]:')))
        m.append(linha)

    return m

# 3

def tam(m):
    return [len(m), len(m[0])]

# 4

def sub(a, b):
    if tam(a) == tam(b):
        c = []
        for i in range(tam(a)[0]):
            linha = []
            for j in range(tam(a)[1]):
                linha.append(b[i][j]-a[i][j])
            c.append(linha)
        return c

# 5

def esparsa(m):
    qtde = len(m)*len(m[0])
    cont = 0
    for i in m:
        for j in i:
            if j == 0:
                cont += 1
    if cont > qtde/2:
        return True
    return False



def quad_magico(m):
    # diagonal
    valor = 0
    for i in range(len(m)):
        valor += m[i][i]
    # diagonal secudaria
    soma = 0
    for i in range(len(m)):
        soma += m[i][len(m)-1-i]
    if soma != valor:
        return False
    # soma cada linha
    for j in range(len(m)):
        soma = 0
        for i in range(len(m)):
            soma += m[j][i]
        if soma != valor:
            return False
    # soma cada coluna
    for j in range(len(m)):
        soma = 0
        for i in range(len(m)):
            soma += m[i][j]
        if soma != valor:
            return False
    return valor




a = [[2,9,4],
    [7,5,3],
    [6,1,8]]
print(quad_magico(a))