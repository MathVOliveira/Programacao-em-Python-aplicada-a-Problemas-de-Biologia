import novo_modulo_dna as mdna
import novo_módulo_validação as mv

sequencia_fasta = ''
contador = 1
with open('14_projeto4\sequence copy.fasta', 'r') as sequencia:
    for linha in sequencia:
        if contador > 1:
            sequencia_fasta += linha
        contador += 1

sequencia_dna = sequencia_fasta.replace('\n', '')
# print(sequencia_dna)        

print('MENU DE OPÇÕES')
opcao = mv.valida('[1] Gerar a sequência comlementar\n[2] Gerar a sequência transcrita\n[3] Retornar a proporção de G-C (%)\n[4] Retornar a proporção de A-T (%)\nDigite a opção desejada: ')

if opcao == 1:
    with open('14_projeto4\sequence complementar.txt', 'w') as txt1:
        txt1.write(mdna.seq_dna_complementar(sequencia_dna))
    print('Sequência complementar gerada!')
elif opcao == 2:
    with open('14_projeto4\sequence transcrita.txt', 'w') as txt2:
        txt2.write(mdna.transcricao_dna(sequencia_dna))
    print('Sequência transcrita!')
elif opcao == 3:
    genes_GC = mdna.porcentagem_GC(sequencia_dna)
    print(f'A proporção de GC na sequência é de {genes_GC[0]:.2f}%')
elif opcao == 4:
    genes_AT = mdna.porcentagem_AT(sequencia_dna)
    print(f'A proporção de AT na sequência é de {genes_AT[0]:.2f}%')