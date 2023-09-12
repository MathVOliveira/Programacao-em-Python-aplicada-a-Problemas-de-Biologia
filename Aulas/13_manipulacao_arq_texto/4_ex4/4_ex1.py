# Lendo seq .fasta

import modulo_dna as mdna

sequencia = ''
contador = 1
with open("13_manipulacao_arq_texto/Nova pasta/sequence.fasta") as seq:
    for linha in seq:
        if contador > 1:
            sequencia += linha
        contador += 1

seq_toda = sequencia.replace('\n', '')
print(seq_toda)

porcentagem = mdna.porcentagem_genes('G', 'C', seq_toda)
print(f'''Porcentagem: {porcentagem[0]:.2f}%; Total de genes: {porcentagem[1]}''')