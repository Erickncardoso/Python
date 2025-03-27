import somasub
import multidiv

num1= float(input("Digite o numéro 1:"))
num2= float(input("Digite o numéro 2:"))
op=input("Digite qual operação gostaria de realizar:")

if op == "+":
    print(somasub.soma(num1,num2))
elif op == "-":
    print(somasub.sub(num1,num2))
elif op == "*":
    print(multidiv.multi(num1,num2))
elif op == "/":
    print(multidiv.div(num1, num2))
else:
    print("Operação inválida")