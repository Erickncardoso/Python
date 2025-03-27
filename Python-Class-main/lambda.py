#Função Lambda
#podem ser definidas sem rotulo
#ex
"""a= lambda x,y: x-y
print(a(2,3))"""

#criar a função lambda que some 3 numeros
a = lambda x,y,z: x + y + z
print(a(1,2,3))

#Crie uma função lambda para inverter string
b=lambda palavra : palavra[::-1]
print(b("hello"))

#Crie uma função lambda que verifica se a string é um palíndrimo
igual = lambda palavra2: palavra2[:] == palavra2[::-1]
print(igual("arara"))




