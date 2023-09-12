# Comparação entre número de coletas e espécies
sp_a = int(input("Número de sp coletados na seção A: "))
ind_a = int(input("Número de indivíduos coletados na seção A: "))

ind_por_sp_a = ind_a/sp_a
print(ind_por_sp_a)

sp_b = int(input("Número de sp coletados na seção B: "))
ind_b = int(input("Número de indivíduos coletados na seção B: "))

ind_por_sp_b = ind_b/sp_b
print(ind_por_sp_b)

# a
print(ind_a >= ind_b)

# b
print(ind_a != ind_b)

# c
print((ind_a > ind_b) or (ind_por_sp_a > ind_por_sp_b))

# d
print((ind_a != ind_b) and (ind_por_sp_a != ind_por_sp_b))