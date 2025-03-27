"""def string(*frases):
    texto=""
    for i in range(len(frases)):
        if  i < len(frases) - 1:
            texto+=frases[i]+"-"
        else:
            texto+= frases[i] +' '
    return texto

a= string("OI","Tudo bem?", "oi")

print(a)"""

"""def media(*valores):
    s=0
    for i in valores:
        s += i
    return s/len(valores)
a=media(1,2,2,2)
print(a)"""

#ou
"""def media(*valores):
    s=0
    for i in valores:
        s += i
    return s/len(valores)
l=[1,2,2,2,2]
a=media(*l)
print(a)"""

#variaveis locais e globais

#as variaveis podem ter o mesmo nome e ser coisas diferentes caso uma delas seja global e a outra local


sacar= 1
depositar= 2
"""extrato= 3"""
sair= 0
saldo = 1000


def sacar(valor):
    global saldo
    saldo = saldo - valor
    print("O seu saldo atual é de", saldo, "e você sacou" , escolher_valor)

def depositar(valor):
    global saldo
    saldo = saldo + escolher_valor
    print("O seu saldo atual é de", saldo, "e você depositou" , escolher_valor)


"""def extrato():
    global trans
    print(extrato)"""

def sair():
        print("Você saiu")


while True:
    escolher_op = float(input("Escolha a opção que gostaria de seguir:"))

    if escolher_op == 1:
        escolher_valor = float(input("Escolha o valor que gostaria de depositar/sacar:"))
        sacar(escolher_valor)
    elif escolher_op == 2:
        escolher_valor = float(input("Escolha o valor que gostaria de depositar/sacar:"))
        depositar(escolher_valor)
"""    elif escolher_op == 3:
        extrato(trans)"""
    else:
        sair()
        break








