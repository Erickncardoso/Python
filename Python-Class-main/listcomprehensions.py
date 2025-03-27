#list comprehensions
import random

a = [1,2,3,4,5,6,7,8,9,10]
b = [i for i in a if i%2==0]  #para pegar os pares da lista
print(b)

#ou podemos passaar as condições com range
b = [i for i in range(1,101) if i%2==0]  #para pegar os pares da lista
print(b)

#para printar numeros aleatorios
a= [random.uniform(-1,1) for i in range(1,11)]
print(a)

#crie uma lista com os quadrados dos números 1 a 10

a = [i*i for i in range(1,11)]
print(a)

#gere uma lista contendo apenas os numeros pares de 1 a 20

b=[i for i in range(1,21) if i%2==0]
print(b)

#crie uma lista contendo o comprimento de cada palavra na lista

c = ["Python", "List", "Comprehension", "Exercícios"]

d = [len(i) for i in c]
print(d)


#Converta uma lista de temperatura em celsius para fahrenheit usand formula f=c*9/5 +32

celsius = [0,10,20,30,40]
convercao = [i*9/5 +32 for i in celsius]
print(convercao)

#Gere uma lista de números de 1 a 20, substiuindo os múltiplos de 3 por fizz

e = ['fizz' if i%3==0 else i for i in range(1,21) if i%2!=0]  #caso eu queira colocar mais uma condição, se coloca no final da lista, caso queira deixar os multilos de 6 color or i%3==0
print(e)


#imprima apenas palavras maiores que 5
e = ["maça","banana","uva","morango", "abacaxi"]
f = [i for i in e if len(i)>5]
print(f)


#gere uma lista de representando as coordenadas [x,y] para um grid 3x3

g = [[x,y] for x in range(4) for y in range(4)]
print(g)
