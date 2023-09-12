# enzima de restrição

dna = 'GCCAGGTGAATTCCGATCGAGCACACTGATCGGCT'
dna2 = 'CCCATTGCCAGGTGAATTCCGATCGAGCACACTGATCGGCT'
dna3 = 'CCCGTTTGGGAGCTGCCAGGTGAATTCCGATCGAGCACACTGATCGGCT'

class Enzima_de_resticao:
    def __init__(self, nome, codigo_PDB, organismo, peso_molecular):
        self.nome = nome
        self.codigo_PDB = codigo_PDB
        self.organismo = organismo
        self.peso_molecular = peso_molecular
        
    # sequencia complementar
    def corte(self, dna):
        cdna = ''
        comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        
        for nucleotideo in dna:
            cdna += comp[nucleotideo]
        
        ds_dna = dna + '\n' + cdna
        
    #4 fragmentos de corte da enzima
        if 'GAATTC' in dna:
            posicao_corte = dna.find('GAATTC')
            fragmento1 = dna[:posicao_corte+1]
            fragmento2 = dna[posicao_corte+1:]
        if 'CTTAAG' in cdna:
            posicao_corte2 = cdna.find('CTTAAG')
            frag_complementar1 = cdna[:posicao_corte2+5]
            frag_complementar2 = cdna[posicao_corte2+5:]
        fragmentada = fragmento1+' '+fragmento2+'\n'+frag_complementar1+' '+frag_complementar2
        
        return (ds_dna, fragmentada)
        
    
    
sdal = Enzima_de_resticao('Sdal', '2IXS', 'Streptomyces diastaticus', 74.64)    
print(sdal.nome, sdal.codigo_PDB, sdal.organismo, sdal.peso_molecular)


# print(sdal.corte(dna))
print('FITA DUPLA: \n'+sdal.corte(dna)[0])
print('FITA FRAGMENTADA: \n'+sdal.corte(dna)[1])

# print(sdal.corte(dna2))
print('FITA DUPLA: \n'+sdal.corte(dna2)[0])
print('FITA FRAGMENTADA: \n'+sdal.corte(dna2)[1])

# print(sdal.corte(dna3))
print('FITA DUPLA: \n'+sdal.corte(dna3)[0])
print('FITA FRAGMENTADA: \n'+sdal.corte(dna3)[1])