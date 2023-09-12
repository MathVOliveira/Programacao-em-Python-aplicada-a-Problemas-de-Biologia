# Fórmula de Ki
ic50 = float(input("Valor de IC50: "))
s = float(input("Valor da concentração do substrato: "))
km = float(input("Valor da Constante de Michaellis: "))

ki = ic50/(1+(s/km))
print(f'{ki:.4f}')



# Fórmula da taxa de recombinação
gen1_rec = int(input("Genótipo Recombinante 1: "))
gen2_rec = int(input("Genótipo Recombinante 2: "))
gen1_nao_rec = int(input("Genótipo não Recombinante 1: "))
gen2_nao_rec = int(input("Genótipo não Recombinante 2: "))

taxa = ((gen1_rec+gen2_rec)/(gen1_rec+gen2_rec+gen1_nao_rec+gen2_nao_rec))*100
print(f"{taxa:.2f}")



# Coleta de insetos
sp_coletados = int(input("quantidade de espécimes coletados: "))
dias_coleta = int(input("Quantidade de dias de coleta: "))

coletas_por_dia = sp_coletados/dias_coleta
print(f"{coletas_por_dia:.2f}")