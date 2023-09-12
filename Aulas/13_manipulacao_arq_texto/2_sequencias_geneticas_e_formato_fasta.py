sequencia = ''
contador = 1
with open("13_manipulacao_arq_texto\Nova pasta\sequence.fasta") as seq:
    for linha in seq:
        if contador > 1:
            print(linha)
            sequencia += linha
        contador += 1

print(sequencia.replace('\n', ''))