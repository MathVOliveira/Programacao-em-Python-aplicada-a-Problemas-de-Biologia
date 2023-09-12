# Manipulação arquivos de texto

    # lendo o arquivo de texto
with open('13_manipulacao_arq_texto/Nova pasta/frase.txt') as texto:
    for linha in texto:
        print(linha)

    # mandando o conteúdo para uma lista
with open("13_manipulacao_arq_texto/Nova pasta/frase.txt") as texto:
    r = texto.readlines()
    print(r)
    
    # escrevendo novo arquivo de texto
with open('13_manipulacao_arq_texto/Nova pasta/texto2.txt', 'w') as texto2:
    texto2.write("Ola a todos")

with open('13_manipulacao_arq_texto/Nova pasta/texto2.txt') as texto2:
    for linha in texto2:
        print(linha)
    