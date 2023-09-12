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
    
def valida_float(pergunta):
    while True:
        try:
            y = float(input(f"{pergunta}"))
        except ValueError:
            print("Valor inserido inválido, tente novamente")
        else:
            print("Valor válido, continuando.")
            break
    return y

def valida(pergunta):
    while True:
        try:
            num = int(input(f'{pergunta}'))
        except ValueError:
            print("Valor inválido, tente novamente")
        else:
            if num == 1 or num == 2:
                break
            else:
                print("Digite uma das alternativas.")
    return num
