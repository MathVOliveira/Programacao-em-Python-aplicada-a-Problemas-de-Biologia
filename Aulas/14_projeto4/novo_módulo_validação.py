def valida_int(pergunta):
    while True:
        try:
            x = int(input(f'{pergunta}'))
        except ValueError:
            print("Valor inserido inválido, tente novamente")
        else:
            print("Valor válido, continuando.")
            break
    return x
    
def valida(pergunta):
    while True:
        try:
            num = int(input(f'{pergunta}'))
        except ValueError:
            print("Valor inválido, tente novamente")
        else:
            if num in range(1, 5):
                break
            else:
                print("Digite uma das alternativas.")              
    return num
