# Cálculo de Ki

def Ki(ic50, s, Km):
    result = ic50/(1+(s/Km))
    return result

constante_Ki = Ki(3.22, 0.0045, 0.03)
print(f'o valor de Ki é de {constante_Ki:.2f}')