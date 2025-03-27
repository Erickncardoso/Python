#calcular média anual

def check(n1,n2,n3):  #pegando as duas maiores notas do check point
    if n1 < n2 and n1 < n3:
        return n2 + n3
    elif n2 < n1 and n2 < n3:
        return n1+ n3
    else:
        return n1 + n2

def nota_sem(n1, n2, n3, sp1,sp2, gs):
    return check(n1, n2, n3) + sp1 + sp2 + gs*0.6   #calculando nota do semestre

def nf(sem1, sem2):     #calculando média final do semestre
    return 0.4*sem1 + 0.6*sem2

nota_final= nf(nota_sem(10, 10, 10, 10, 10, 100) , nota_sem(10, 10, 10, 10, 10, 100))  #calculando a média anual sem a divisão por 10
#nf(nota_sem(n1_1, n2_1, n3_1, sp1_1, sp2_1.gs_1) , nota_sem(n1_2, n2_2, n3_2, sp1_2, sp2_2, gs_2))


print(nota_final/10)



#Achando valor de pi
n=10
soma = 0
def pin(n):
    n = 10
    soma = 0

    for i in range(10000):
        soma += (-1)**(i)*4/(2*i+1)
    return soma
print(pin(10000000000))


#empacotamento de parâmetros

def soma(a,b):  #caso queira colocar mais um parametro, precisamos adicionar na lista ou colocar o valor
    print(a + b)
l=[1,2]
soma(*l)

#a função print pode receber quantos parametros você passar

def soma(*args):  #args = lista porem não podemos usar append/pop e etc
    print(args)
soma(1,2,3)

#construa uma função que realize a soma de todos os valores recebidos
def soma(*args):
    valor = 0
    for i in args:
        valor+= i
    print(valor)
soma(20,20,20)

#Função chamada média que aceita um número variável de argumentos e retorna a média
def média(*args):
    valor = 0
    for i in args:
        valor+= i
    print(valor/len(args))
média(20,20,20)


#Crie uma função que recebe várias strings e as junta em uma única string separada por espaço

def string(*args):
    final= ""
    for i in args:
        final+=i + " "
        print(final)

string("r","t")
