# COLETA DE INSETOS
    
# USAR especiesIONÁRIOS
especies = {}

    # quantas espécies foram coletadas?
qtd_sp = int(input("Quantas espécies foram coletadas: "))

    # armazenando em uma estrutura de dados (dicionário)
for sp in range(0, qtd_sp):
    nome_sp = input("Digite o nome da espécie: ")
    especies[nome_sp] = int(input("quantidade: "))

print(especies)

    # obtendo média de coleta por espécie
total_sp = 0
for value in especies.values():
    total_sp += value
    
print(total_sp)

    # mostrando as informações
print('Espécie:\tQuantidade:')

for key, valor in especies.items():
    print(f'{key}\t\t{valor}')

    # média
print(f'A média por espécie é de {total_sp/qtd_sp}')