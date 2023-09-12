# Classe planta

class Planta:
    def __init__(self, familia, especie, fase_dominante):
        self.familia = familia
        self.especie = especie
        self.fase_dominante = fase_dominante
    
    def obter_genero(self):
        limite = self.especie.find(' ')
        genero = self.especie[:limite]
        return genero
    
    def obter_taxons(self):
        limite = self.especie.find(' ')
        genus = self.especie[:limite]
        taxons = (self.especie, genus, self.familia)
        return taxons
    
cycas = Planta('Cycadaceae', 'Cycas revoluta', 'esporófito')

print(cycas.obter_genero())
print(cycas.obter_taxons())
