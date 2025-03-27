#estruturas que armazenam dados, são mapeamentos formdos por pares de chaves-valor
#para declarar
#exemplos
dicionario = {}#dicionario vazio
dicionario1 = {
    'nome': 'gabrielly',
    'idade': 19       #podemos varias os dados // podemos ter tuplas dentro das chaves
}
print(dicionario1)   #para printar o dicionario
d = {
    'lat': 23.45,
    'long': 1.34
}
print(d['lat'])     #para printar só u valor dentro do dicionario

#para verificar se uma chave está presente no dicionario
print('longa' in d)  #caso tenha, retorna true, ao contrario false

#podemos utilizar o get para oegar a chave do dicionario, a vantagem é que se a chave não existir, retorna vazio e o codigo não da erro
print(d.get('lat'))

#usar o comando if para validar se uma chave existe e só executar o codigo caso exista
#a função do len traz a qtd de parchavevalor


#para adiconar uma nova chave
d['nova_chave'] = 'novo valor '


#para alterar
d['lat'] = 127.23

#para remover valores do dicionario usamos o pop
d.pop('lat')  #se você printar a remoção. ele retorna o que será removido // se tentar remover da chave algo que não existe, é importante utilizar o if para não ocorrer erro

#podemos remover com o delet tambem
"""del d['lat']""" #mas aqui não retorna o valor removido

#atualizar um dicionario
# o que for chave igual ele substitui e o que for diferente ele adiciona
da = {
    'a':'cachorro',
    'b': 'gato',
}
db = {
    'b': 10,
    'c': 2.4
}
print(da)
print(db)
da.update(db)
print(da)

#para acessar todas as chaves ou valores do dicionario
df = {
    'a':'cachorro',
    'b': 'gato',
    'c':10,
    1.23:'teste'
}
print(df.keys())#para acessar as chaves
print(df.values())#para acessar os valores

# .items retorna uma lista tupla com cada chave valor


#exercicios

#ex1 criando os dicionarios

dicfruta = {
    'Uva': 'Roxo',
    'Laranja': 'Laranja',
    'Banana': 'Amarelo'
}

#ex2 printando um valor
print(dicfruta['Uva'])

#ex3 add novo par de valor
dicfruta['Maracuja'] = 'Amarelo'

#ex4 Atualizar valor
dicfruta['Uva'] = 'Rosa'

#ex5 remover item
dicfruta.pop('Laranja')

#ex6 imprimir apenas as chaves
print(dicfruta.keys())

#ex7 imprimir apenas os valores
print(dicfruta.values())

#ex8 verificar a existencia de uma chave

print(dicfruta.get('Banana'))

#ex9 combinar 2 dicionarios
dicfruta2 = {
    'Morango': 'Vermelho',
    'Uva': 'Roxo',
    'Laranja': 'Laranja',
    'Banana': 'Amarelo'
}

dicfruta.update(dicfruta2)

#ex10 Contar a qtd de itens
print(len(dicfruta))














