# TRANSCIÇÃO DE SEQUÊNCIA DE DNA
dna = 'CGCGTAGCTAGCTGTAC'
rna = []
seqRNA = ''

# nesse laço se tem o rna em formato de lista e de str
for nucleotideo in dna:
    
    if nucleotideo == 'A':
        rna.append('U')
        seqRNA += 'U'
            
    if nucleotideo == 'T':
        rna.append('A')
        seqRNA += 'A'
    
    if nucleotideo == 'C':
        rna.append('G')
        seqRNA += 'G'
    
    if nucleotideo == 'G':
        rna.append('C')
        seqRNA += 'C'
      
print(f'sequência de RNA: {seqRNA}')
# pegando a lista e imprimindo 'junto'
print(f"Sequência de RNA, em formato de lista:\n{rna}")
for n in rna:
    print(n, end="")
