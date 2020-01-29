'''
Grupo 3
Cache de 8 linhas com 6 bits de endereço, sendo 3 para index e 3 para tag

arquivos:
- m3
- Prog3.1
- Prog3.2
- Prog3.3
- Prog3.4
- Prog3.5
'''

def progs():
    print('Escolha o programa a ser executado: ')
    print('[1] 3_1')
    print('[2] 3_2')
    print('[3] 3_3')
    print('[4] 3_4')
    print('[5] 3_5')
    opcao = int(input(''))

    if opcao == 1:
        prog = "../prog3_1.txt"
    elif opcao == 2:
        prog = "../prog3_2.txt"
    elif opcao == 3:
        prog = "../prog3_3.txt"
    elif opcao == 4:
        prog = "../prog3_4.txt"
    elif opcao == 5:
        prog = "../prog3_5.txt"
    return prog


with open('../m3.txt', 'r') as m3:  # abrindo arquivo de memoria m2
    endMem = m3.readlines()           # armazenando valores em uma lista endMem
endMem = [x.strip() for x in endMem]  # tirando espaços vazios da lista

with open(progs(), 'r') as prog:  # abrindo arquivo do programa prog1
    endProg = prog.readlines()
endProg = [x.strip() for x in endProg]

endCache = ['0', '0','0', '0', '0', '0','0', '0']  # lista de endereços de cache iniciados vazios

'''
endCache[0] -> bit de validade
endCache[4:] -> index
endCache[1:3] -> tag

procura-se o endereço dado pelo processador (programas) na memória cache
'''

miss = 0
hit = 0

for linha in endProg:
    if linha[3:] == '000':  # verifica o ultimo bit do end memoria (index da cache = 000)
        if endCache[0][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[0][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[0][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '001':  # verifica o ultimo bit do end memoria (index da cache = 001)
        if endCache[1][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[1][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[1][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[2][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[2][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[2][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[3][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[3][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[3][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[4][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[4] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[4][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[4][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[4] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[5][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[5] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[5][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[5][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[5] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[6][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[6] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[6][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[6][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[6] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[3:] == '111':  # verifica o ultimo bit do end memoria (index da cache = 111)
        if endCache[7][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[7] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[7][0] == '1':  # bit de validade = 1
            if linha[0:2] == endCache[7][1:3]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[7] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    print(endCache)





print('\nHit: {}'.format(hit))
print('Miss: {}'.format(miss))


# fechando os 2 arquivos abertos

m3.close()
prog.close()

