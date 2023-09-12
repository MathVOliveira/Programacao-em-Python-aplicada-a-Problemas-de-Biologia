from questões import *

respostas = []
nota = 0

for q in questoes:
    
    while True:
        invalida = False
        print(q)
        resposta = input('resposta: ').upper()
       
        if resposta not in alternativas:
            print("Resposta inválida, tente novamente.")
            invalida = True
        else:
            respostas.append(resposta)
            break

for indice in range(len(respostas)):
    
    if respostas_corretas[indice] == respostas[indice]:
        print(f"Questão {indice+1}º: correta")
        nota += 1
    else:
        print(f"Questão {indice+1}º: errada >>> correta: letra {respostas_corretas[indice]}")
        
print(f"Sua nota foi de {nota} pontos.")