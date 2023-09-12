# Classe DNA

class DNA:
    def __init__(self, sequencia, organismo, tipo_de_fita):
        self.sequencia = sequencia
        self.organismo = organismo
        self.tipo_de_fita = tipo_de_fita
        
    def fita_complementar(self):
        dna = self.sequencia
        comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        complementar = ''
        
        for nucleotideo in dna:
            complementar += comp[nucleotideo]
        
        return complementar
    
    def transcicao(self):
        dna = self.sequencia
        comp = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
        rna = ''

        for nucleotideo in dna:
            rna += comp[nucleotideo]
        
        return rna

seq1 = DNA('CGCATCGCATATATCGATACGATCG', 'Homo sapiens', 'dupla')
print(seq1.sequencia, seq1.organismo, seq1.tipo_de_fita)

print(seq1.fita_complementar())
print(seq1.transcicao())