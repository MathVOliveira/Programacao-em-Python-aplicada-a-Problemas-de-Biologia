# Função - Frequência de recombinação

def recombinacao(g1r, g2r, g1nr, g2nr):
    '''
    Parâmetros:
        g1r = genótipo recombinante 1
        g2r = genótipo recombinante 2
        g1nr = genótipo não recombinante 1
        g2nr = genótipo não recombinante 2
    '''
    freq = (g1r + g2r)/(g1r + g2r + g1nr + g2nr)
    return round(freq, 2)

frequencia = recombinacao(211, 200, 564, 610)
print(frequencia)