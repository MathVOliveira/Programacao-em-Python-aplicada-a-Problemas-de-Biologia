# TRANSCRIÇÃO DE SEQUÊNCIA DE DNA

rna = ''
dna = {
    'A' : 'U',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C',
}

while True:
    seq = str(input('Digite a sequência de aminoácidos: ')).upper()
    invalida = False
    
    for a in seq:
    
      if a not in dna.keys():
        invalida = True
    
    if invalida == True:
      print('Sequência inválida')
    else:
      break
        
for aa in seq:
    rna += dna[aa]

print(rna)
        


# OUTRO MODO DE FAZER, MAIS FEIO

    # seq = input("Digite a sequência de dna a ser transcrita: ").upper()
          
    # print("C" in dna.keys()) 
          
    # for a in seq:
      
    #     if a not in dna.keys():
    #         print('sequência inválida')
    #         exit()
      
    #     if a in dna.keys():
    #         rna += dna[a]
