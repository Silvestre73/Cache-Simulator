'''
Grupo 4
Cache de 16 linhas com 6 bits de endereço, sendo 4 para index e 2 para tag

arquivos:
- m3
- Prog4.1
- Prog4.2
- Prog4.3
- Prog4.4
- Prog4.5
'''

def progs():
    print('Escolha o programa a ser executado: ')
    print('[1] 4_1')
    print('[2] 4_2')
    print('[3] 4_3')
    print('[4] 4_4')
    print('[5] 4_5')
    opcao = int(input(''))

    if opcao == 1:
        prog = "../prog4_1.txt"
    elif opcao == 2:
        prog = "../prog4_2.txt"
    elif opcao == 3:
        prog = "../prog4_3.txt"
    elif opcao == 4:
        prog = "../prog4_4.txt"
    elif opcao == 5:
        prog = "../prog4_5.txt"
    return prog


with open('../m4.txt', 'r') as m4:  # abrindo arquivo de memoria m4
    endMem = m4.readlines()           # armazenando valores em uma lista endMem
endMem = [x.strip() for x in endMem]  # tirando espaços vazios da lista

with open(progs(), 'r') as prog:  # abrindo arquivo do programa prog1
    endProg = prog.readlines()
endProg = [x.strip() for x in endProg]

endCache = ['0', '0','0', '0', '0', '0','0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0']  # lista de endereços de cache iniciados vazios

'''
endCache[0] -> bit de validade
endCache[3:] -> index
endCache[1:2] -> tag

procura-se o endereço dado pelo processador (programas) na memória cache
'''

miss = 0
hit = 0

for linha in endProg:
    if linha[2:] == '0000':  # verifica o ultimo bit do end memoria (index da cache = 0000)
        if endCache[0][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[0][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[0][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0001':  # verifica o ultimo bit do end memoria (index da cache = 0001)
        if endCache[1][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[1][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[1][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[2][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[2][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[2][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[3][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[3][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[3][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[4][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[4] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[4][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[4][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[4] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[5][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[5] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[5][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[5][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[5] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[6][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[6] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[6][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[6][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[6] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '0111':  # verifica o ultimo bit do end memoria (index da cache = 111)
        if endCache[7][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[7] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[7][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[7][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[7] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1000':  # verifica o ultimo bit do end memoria (index da cache = 000)
        if endCache[8][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[8] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[8][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[8][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[8] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1001':  # verifica o ultimo bit do end memoria (index da cache = 001)
        if endCache[9][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[9] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[9][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[9][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[9] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[10][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[10] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[10][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[10][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[10] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[11][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[11] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[11][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[11][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[11] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[12][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[12] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[12][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[12][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[12] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[13][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[13] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[13][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[13][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[13] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[14][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[14] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[14][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[14][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[14] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[2:] == '1111':  # verifica o ultimo bit do end memoria (index da cache = 111)
        if endCache[15][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[15] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[15][0] == '1':  # bit de validade = 1
            if linha[0:1] == endCache[15][1:2]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[15] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    print(endCache)





print('\nHit: {}'.format(hit))
print('Miss: {}'.format(miss))


# fechando os 2 arquivos abertos

m4.close()
prog.close()

