# Manipulação de Strings 2

# pulando uma linha na str
frase = 'eu gosto\nmuito de\nPython'
print(frase)
# OU utilando aspas triplas no começo e fim da str
frase2 = '''eu gosto
muito de
Python'''
print(frase2)
# também dá para usar direto no print, sem usar uma var
print('''eu nem sei se 
o que estou fazendo
está certo''')

# MEMBERSHIP de strings
# busca de fragmentos, pesquisa se tem certa parte de um texto em outro texto
print('cas' in 'casa') # retorna True pq tem
print('caa' in 'casa') # retorna False pois não há essa sequência em casa
print('x' in 'casa') # retorna False pois não há também

# Indexação negativa
palavra = 'paralelepipedo'
print(palavra[0:7])
print(palavra[-1]) # aparece o último
print(palavra[-2]) # aparece a antepenúltima e assim por sequência

# Tabulação
print(f'''Espécimes coletados   espécies coletadas
56  12''') # forma errada de fazer isso
print(f'''Espécimes coletados\tespécies coletadas
56\t\t\t12''') # forma certa de fazer isso, use o '\t' até a tebela ficar alinhada





