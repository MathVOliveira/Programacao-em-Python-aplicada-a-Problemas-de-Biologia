import random

def seq_dna_complementar(seq):
    seq_complementar = ''
    bases = {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C',
    }
    
    for n in seq:
        seq_complementar += bases[n]
    
    return seq_complementar

def porcentagem_AT(seq):
    comprimento_seq = len(seq)
    a_quant = 0
    t_quant = 0
    
    for aa in seq:
        if aa == 'A':
            a_quant += 1
        elif aa == 'T':
            t_quant += 1
    
    return (((a_quant + t_quant) / comprimento_seq) * 100), comprimento_seq

def porcentagem_GC(seq):
    comprimento_seq = len(seq)
    g_quant = 0
    c_quant = 0
    
    for aa in seq:
        if aa == 'G':
            g_quant += 1
        elif aa == 'C':
            c_quant += 1
    
    return (((g_quant + c_quant) / comprimento_seq) * 100), comprimento_seq


def transcricao_dna(seq):
    rna = ''
    dna = {
        'A' : 'U',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C',
    }
        
    for gene in seq:
        rna += dna[gene]
    
    return rna
