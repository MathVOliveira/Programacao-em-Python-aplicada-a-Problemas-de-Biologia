# 1 - IDENTIFICANDO FAMÍLIAS TAXONÔMICAS
nome = input("Digite o nome da família taxonômica: ").capitalize()

if nome[-5:] == 'aceae':
    print('Família de plantas')
elif nome[-4:] == 'idae':
    print('família de animais')
else:
    print('Táxon não-identificado')
        

# ========================================================================== #
# 2 - ANALISANDO PARÂMETROS HEMATOLÓGICOS
hemacias = float(input('Hemácias(10¹²/L): '))
hemoglobina = float(input('Hemoglobina(g/dL): '))
hematocrito = float(input('Hematócrito(%): '))

if (4.5 <= hemacias <= 5.5) and (13 <= hemoglobina <= 17) and (40 <= hematocrito <= 50):
    print('tá normal')
else:
    print('está alterado')


# ========================================================================== #
# 3 - DETECTANDO CÓDOS DE INICIAÇÃO E TERMINAÇÃO
seqRNA = input("Sequência de RNA: ")


if 'AUG' in seqRNA:
    if ('UGA' or 'UAA' or 'UAG') in seqRNA:
      print('A sequência possui códon de iniciação e terminação')
    else:
      print('A sequência possui apenas códon de iniciação')
else:
    if ('UGA' or 'UAA' or 'UAG') in seqRNA:
      print('A sequência possui apenas códon de terminação')
    else:
      print('Não possui códon de iniciação nem de terminação')
            