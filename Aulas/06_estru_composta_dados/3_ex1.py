# MASSA DE SEQUÊNCIA DE AMINOÁCIDOS
    # calcular a massa de uma sequencia de peptídeos de acordo com cada aminoácido
   
seq = 'ABHYVQRESHABCDEH'
massa = 0
    
pep = {
    'A' : 71.08,
    'R' : 156.19,
    'N' : 114.11,
    'D' : 115.09,
    'C' : 103.15,
    'E' : 129.12,
    'Q' : 128.13,
    'G' : 57.05,
    'H' : 137.14,
    'I' : 113.16,
    'L' : 113.16,
    'K' : 128.18,
    'M' : 131.20,
    'F' : 147.18,
    'P' : 97.12,
    'S' : 87.08,
    'T' : 101.11,
    'W' : 186.22,
    'Y' : 163.18,
    'V' : 99.13
}

for pp in seq:
    
    if pp in pep:
        massa += pep[pp]
        print(f"Massa total até {pp}: {massa:.2f}")
    elif pp not in pep:
        print(f'Não foi encontrado o peptídio {pp}')