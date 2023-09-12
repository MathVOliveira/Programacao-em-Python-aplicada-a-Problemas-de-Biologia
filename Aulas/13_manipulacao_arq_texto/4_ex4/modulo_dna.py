def porcentagem_genes(b1, b2, seq):
    comprimento_seq = len(seq)
    b1_quant = 0
    b2_quant = 0
    
    for aa in seq:
        if aa == b1:
            b1_quant += 1
        elif aa == b2:
            b2_quant += 1
    
    return (((b1_quant + b2_quant) / comprimento_seq) * 100), comprimento_seq

