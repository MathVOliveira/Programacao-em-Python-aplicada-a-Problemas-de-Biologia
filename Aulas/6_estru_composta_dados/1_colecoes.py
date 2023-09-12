# COLEÇÕES

# TUPLAS
tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')

    # imprimindo todos os elementos
print(tupla)

    # imprimindo através do índice dos elementos
print(tupla[0])

    # imprimindo o índice através do elemento
print(tupla.index('Canis familiaris'))

    # percorrendo a tupla
for elemento in tupla:
    print(elemento)



# LISTAS
lista1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
lista2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
  
    # juntando as duas em uma única lista
lista3 = lista1 + lista2
print(lista3)
  
    # operações
lista2_2 = lista2 * 2   # duplicando
print(lista2_2)
  
    # acessando elementos através do índice
print(lista1[0])
  
    # adicionando elementos
lista2.append('Gorila gorila')
print(lista2)
  
    # removendo elementos 
lista1.remove('Felis catus')
print(lista1)
  
    # apagando uma lista por completo
del(lista2_2)
# print(lista2_2) >>> gera um erro pois a lista foi apagada, não existe mais essa var
  
    # varrendo os dados de uma lista
for item in lista3:
    print(item)



# DICIONÁRIOS
  
    # definimos o nome e valor (chave e valor, respectivamente)
coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
  
    # imprimindo a chave, é mostrado o valor dela
print(coleta['Aedes aegypt'])
  
    # adicionando elementos
coleta['Rhodnius montenegrensis'] = 11
print(coleta)
  
    # apagando elementos
# del(coleta) >>> apaga todo o dicionário dessa forma
del(coleta)['Aedes albopictus']
print(coleta)
  
    # visualizando todo o dicionário
print(coleta.items())
    # visualizando as chaves
print(coleta.keys())
    # visualizando os valores
print(coleta.values())

    # juntando dois dicionários
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
coleta.update(coleta2)
print(coleta)

    # percorrendo um dicionário
coleta.items()
for especie, num_especie in coleta.items():
    print(f'Espécie: {especie}\nQuantidade: {num_especie}')
    


# CONJUNTOS <class 'set'>

    # imprimindo apenas elementos que não se repetem em uma tupla
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo', 'ácidos nucleicos', 'carboidrato', 'lipídeo')
print(biomoleculas)
print(set(biomoleculas))

    # intersecção entre dois conjuntos traz apenas os elementos repetidos (dicionários)
c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c3 = c1.intersection(c2)
print(c3)

    # pode-se chegar a diferença entre os conjuntos (os que só aparecem no conjunto que chama a função)
print(c1.difference(c2))
print(c2.difference(c1))

