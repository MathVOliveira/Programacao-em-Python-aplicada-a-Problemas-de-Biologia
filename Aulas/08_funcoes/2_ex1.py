# Porcentagem AT em seq de DNA

def porcentagem_A_T(seq):
    comprimento_seq = len(seq)
    aa_A = 0
    aa_T = 0
    
    for aa in seq:
        if aa == 'a':
            aa_A += 1
        elif aa == 't':
            aa_T += 1
    
    return (((aa_A + aa_T) / comprimento_seq) * 100)

porcentagem = porcentagem_A_T(input('Digite a sequência: '))
print(porcentagem, '%')


# OU TAMBÉM PODE SER FEITO DESSA FORMA
def at(seq2):
    comp_seq = len(seq2)
    a = seq2.count('a')
    t = seq2.count('t')
    
    return (((a + t) / comp_seq) * 100)

p = at('atatrrrrrr')
print(p)    
