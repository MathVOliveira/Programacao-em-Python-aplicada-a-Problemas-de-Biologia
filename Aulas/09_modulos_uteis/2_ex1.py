# Função que gera sequência aleatória de DNA

import random

def dna():
    tamanho = int(input("Qual o tamanho da seq de DNA desejada: "))
    bases = ['A', 'T', 'C', 'G']
    seq = ''
    
    for n in range(tamanho):
        seq += random.choice(bases)
    
    return seq
        
x = dna()
print(x)
print(len(x))