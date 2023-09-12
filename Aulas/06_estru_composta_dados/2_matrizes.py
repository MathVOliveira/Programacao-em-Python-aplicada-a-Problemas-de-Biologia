# MATRIZES
    # outro tipo de estruturas de dados que permite armazenar mais valores

# numpy >>> biblioteca muito usada para processamento científico, análise de dados, IA, estatísticas... 
import numpy as np

# criando uma matriz
    # array = lista melhorada... (estudar mais)
matriz = np.array([[2, 3, 1], [4, 5, 7]])
print(matriz)

    # acessando uma matriz pelo índice (também começa em 0, assim como os demais)
print(matriz.shape) # .shape >>> mostra o número de linhas e colunas, respectivamente
    
    # retornando uma linha (o pemeiro [] sempre retorna a linha, se apenas ele, retorna toda a linha)
print(matriz[0])

    # retornando uma coluna (precisa de dois [], com o segundo sempre sendo a coluna)
print(matriz[0][0])

    # percorrendo todos os elementos de uma matriz
for i in range(matriz.shape[0]):    # percorrendo as linhas
    print(matriz[i])
    
    for j in range(matriz.shape[1]):    # percorrendo as colunas
        print(matriz[i][j])