'''
Grupo 1
Cache de 2 linhas com 6 bits de endereço, sendo 1 para index e 5 para tag

arquivos:
- m1
- Prog1.1
- Prog1.2
- Prog1.3
- Prog1.4
- Prog1.5
'''

def progs():
    print('Escolha o programa a ser executado: ')
    print('[1] 1_1')
    print('[2] 1_2')
    print('[3] 1_3')
    print('[4] 1_4')
    print('[5] 1_5')
    opcao = int(input(''))

    if opcao == 1:
        prog = "../prog1_1.txt"
    elif opcao == 2:
        prog = "../prog1_2.txt"
    elif opcao == 3:
        prog = "../prog1_3.txt"
    elif opcao == 4:
        prog = "../prog1_4.txt"
    elif opcao == 5:
        prog = "../prog1_5.txt"
    return prog


with open('../m1.txt', 'r') as m1:  # abrindo arquivo de memoria m1
    endMem = m1.readlines()           # armazenando valores em uma lista endMem
endMem = [x.strip() for x in endMem]  # tirando espaços vazios da lista

with open(progs(), 'r') as prog:  # abrindo arquivo do programa prog1
    endProg = prog.readlines()
endProg = [x.strip() for x in endProg]

endCache = ['0', '0']  # lista de endereços de cache iniciados vazios

'''
endCache[0] -> bit de validade
endCache[6] -> index
endCache[1:5] -> tag

procura-se o endereço dado pelo processador (programas) na memória cache
'''

miss = 0
hit = 0

for linha in endProg:
    if linha[5] == '0':  # verifica o ultimo bit do end memoria (index da cache = 0)
        if endCache[0][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[0][0] == '1':  # bit de validade = 1
            if linha[0:4] == endCache[0][1:5]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[5] == '1':  # verifica o ultimo bit do end memoria (index da cache = 1)
        if endCache[1][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[1][0] == '1':  # bit de validade = 1
            if linha[0:4] == endCache[1][1:5]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    print(endCache)






print('\nHit: {}'.format(hit))
print('Miss: {}'.format(miss))


# fechando os 2 arquivos abertos

m1.close()
prog.close()
