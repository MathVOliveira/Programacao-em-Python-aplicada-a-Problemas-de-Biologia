# Avaliando execução de algoritmo de geração de sequência

import time as tm
import random


import random

def dna():
    antes = tm.time()
    tamanho = int(input("Qual o tamanho da seq de DNA desejada: "))
    bases = ['A', 'T', 'C', 'G']
    seq = ''
    
    for n in range(tamanho):
        seq += random.choice(bases)
    
    depois = tm.time()
    tempo_geracao = depois - antes
    
    # dessa forma, retorna uma lista
    return seq, tempo_geracao
        
x = dna()
print(f'Sequência de DNA: {len(x[0])}\t\t\tTempo de geração: {x[1]}')
