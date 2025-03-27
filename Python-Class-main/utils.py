#para contar a quantidade de vogais dentro de uma string
def contar_vogais(palavra):
    qtde = 0
    for i in palavra   :
        if i =="a" or i =="e" or i == "i" or i == "o" or i == "u":
            qtde += 1
    return qtde

print(contar_vogais("gabrielly"))

#para reverter uma string
def reverter(palavra):
    return palavra[::-1]#::começo- fim -1 olhar ao contrario
print(reverter("joão"))


#contar a quantidade de palavras em um texto
def contar_palavras(texto):
    qtde = 1
    for i in texto:
        if i == " ":
            qtde+=1
    return qtde
print(contar_palavras("oi tudo bem com você"))

#para puxar de outra arquivo: export nome do arquivo / printa o nome do arquivo.função e coloca entre () / ultil.conta()




