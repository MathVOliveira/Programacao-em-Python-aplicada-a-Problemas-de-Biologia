# 1 - ABREVIANDO NOMES DE ESPÉCIES

# digitar um nome
nome = input("Digite o nome da espécie: ")

# transformar nome em letras capitalizadas
nome_cap = nome.capitalize()
print(nome_cap)

# abreviar o nome
fim_nome = nome_cap.find(' ') # posição do final da primeira palavra
nome_retirado = nome_cap[1:fim_nome] # pegando a str da primeira palavra para ser substituída
nome_abreviado = nome_cap.replace(nome_retirado, '.') # substituindo por .
print(nome_abreviado)

# ======================================================================================= #
# 2 - ANALISANDO SEQUÊNCIAS DE PROTEÍNAS
pnormal = 'MGTACHMCGYGCYGYGSHSCIOOENNFHEF'
pmutante = 'MCCFOTYOOANLGTACHMCGYGCYGYGSHSCIOOENNFHEF'

# a) quanto % a proteína mutante é maior que a normal
n = len(pnormal)
m = len(pmutante)

porcentagem = ((m*100)/n)-100
print(f"{porcentagem:.2f}")

# b) o comprimento de aa's de cada proteína
print('Proteína normal: ', len(pnormal))
print('Proteína mutante: ', len(pmutante))

# c) a % de serina (S) nas duas sequências
qtd_s_pnormal = pnormal.count('S')
qtd_aa_pnormal = len(pnormal)
porcentagem_s_pnormal = (qtd_s_pnormal/qtd_aa_pnormal)*100
qtd_s_pmutante = pmutante.count('S')
qtd_aa_pmutante = len(pmutante)
porcentagem_s_pmutante = (qtd_s_pmutante/qtd_aa_pmutante)*100

print(qtd_s_pnormal, qtd_s_pmutante)
print(f"{porcentagem_s_pnormal:.2f}")
print(f"{porcentagem_s_pmutante:.2f}")

# ===================================================================================== #
# 3 - EXTRAINDO ORF DE SEQUÊNCIA DE RNA
seqRNA='AAAUUUAUGUUCCCUUUGGGUGGGCCCGGGAAAUAGUUCUUGUUUAAAUUC'

# posição dos Códons de iniciação e terminação
pos_inicial = seqRNA.find('AUG')
pos_final = seqRNA.find('UAG')
print(pos_inicial, pos_final)

# Imprimindo a ORF
print(seqRNA[(pos_inicial):(pos_final)])
# OU
exon = seqRNA[(pos_inicial):(pos_final)]
print(exon)