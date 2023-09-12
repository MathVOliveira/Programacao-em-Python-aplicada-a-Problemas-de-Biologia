# Chave de identificação

import validacao as vd

p1 = vd.valida("Todas as folhas recompostas:\n[1] Sim\n[2] Não\n")

# FOLHAS RECOMPOSTAS
if p1 == 1:
    #ESPINHOS
    p2 = vd.valida("Espinhos:\n[1] Sim\n[2] Não\n")
    if p2 == 1:
        print("A. karroo")
    else:
        # GLÂNDULAS
        p3 = vd.valida("Glândulas:\n[1] Glândulas na base das pínulas\n[2] Glândulas distribuídas ao acaso\n")
        if p3 == 1:
            print("A. dealbata")
        else:
            print("A. mearnsii")
else:
    # FILÓDIOS
    p4 = vd.valida("Filódios:\n[1] Folhas recompostas e filódios, em indivíduos jovens\n[2] Só filódios\n")
    if p4 == 1:
        print("A. melanoxylon")
    else:
        # NERVURAS
        p5 = vd.valida("Nervuras:\n[1] Várias nervuras longitudinais\n[2] Uma nervura longitudinal\n")
        if p5 == 1:
            p6 = vd.valida("Simetria dos filódios:\n[1] Filódios quase todos simétricos\n[2] Filódios não-simétricos\n")
            if p6 == 2:
                print("A. melanoxylon")
            else:
                p7 = vd.valida("Flores:\n[1] Flores reunidas em espiga\n[2] Flores reunidas em capítulos\n")
                if p7 == 1:
                    print("A. longifolia")
                else:
                    print("A. cyclops")
        else:
            p8 = vd.valida("Simetria dos filódios:\n[1] Filódios simétricos\n[2] Filódios não-simétricos\n")
            if p8 == 2:
                print("A. pycnantha")
            else:
                p9 = vd.valida("Cor e forma dos filódios:\n[1] Filódios verde-claros estreitos\n[2] Filódios verde-glaucos mais largos\n")
                if p9 == 1:
                    print("A. retinoides")
                else:
                    print("A. saligna")