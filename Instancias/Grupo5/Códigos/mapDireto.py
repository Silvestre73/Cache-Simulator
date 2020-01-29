'''
Grupo 5
Cache de 32 linhas com 6 bits de endereço, sendo 5 para index e 1 para tag

arquivos:
- m5
- Prog5.1
- Prog5.2
- Prog5.3
- Prog5.4
- Prog5.5
'''

def progs():
    print('Escolha o programa a ser executado: ')
    print('[1] 5_1')
    print('[2] 5_2')
    print('[3] 5_3')
    print('[4] 5_4')
    print('[5] 5_5')
    opcao = int(input(''))

    if opcao == 1:
        prog = "../prog5_1.txt"
    elif opcao == 2:
        prog = "../prog5_2.txt"
    elif opcao == 3:
        prog = "../prog5_3.txt"
    elif opcao == 4:
        prog = "../prog5_4.txt"
    elif opcao == 5:
        prog = "../prog5_5.txt"
    return prog


with open('../m5.txt', 'r') as m5:  # abrindo arquivo de memoria m5
    endMem = m5.readlines()           # armazenando valores em uma lista endMem
endMem = [x.strip() for x in endMem]  # tirando espaços vazios da lista

with open(progs(), 'r') as prog:  # abrindo arquivo do programa prog1
    endProg = prog.readlines()
endProg = [x.strip() for x in endProg]

endCache = ['0', '0','0', '0', '0', '0','0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0'
            '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0']  # lista de endereços de cache iniciados vazios

'''
endCache[n][0] -> bit de validade
endCache[n][2:] -> index
endCache[n][1] -> tag

procura-se o endereço dado pelo processador (programas) na memória cache
'''

miss = 0
hit = 0

for linha in endProg:
    if linha[1:] == '00000':  # verifica o ultimo bit do end memoria (index da cache = 0000)
        if endCache[0][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[0][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[0][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00001':  # verifica o ultimo bit do end memoria (index da cache = 0001)
        if endCache[1][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[1][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[1][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[2][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[2][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[2][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[3][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[3][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[3][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[4][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[4] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[4][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[4][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[4] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[5][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[5] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[5][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[5][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[5] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[6][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[6] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[6][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[6][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[6] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '00111':  # verifica o ultimo bit do end memoria (index da cache = 111)
        if endCache[7][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[7] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[7][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[7][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[7] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01000':  # verifica o ultimo bit do end memoria (index da cache = 000)
        if endCache[8][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[8] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[8][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[8][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[8] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01001':  # verifica o ultimo bit do end memoria (index da cache = 001)
        if endCache[9][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[9] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[9][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[9][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[9] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[10][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[10] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[10][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[10][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[10] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[11][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[11] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[11][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[11][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[11] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[12][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[12] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[12][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[12][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[12] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[13][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[13] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[13][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[13][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[13] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[14][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[14] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[14][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[14][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[14] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '01111':  # verifica o ultimo bit do end memoria (index da cache = 111)
        if endCache[15][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[15] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[15][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[15][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[15] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10000':  # verifica o ultimo bit do end memoria (index da cache = 0000)
        if endCache[16][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[16] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[16][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[16][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[16] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10001':  # verifica o ultimo bit do end memoria (index da cache = 0001)
        if endCache[17][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[17] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[17][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[17][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[17] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[18][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[18] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[18][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[18][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[18] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[19][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[19] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[19][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[19][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[19] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[20][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[20] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[20][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[20][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[20] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[21][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[21] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[21][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[21][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[21] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[22][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[22] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[22][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[22][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[22] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '10111':  # verifica o ultimo bit do end memoria (index da cache = 111)
        if endCache[23][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[23] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[23][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[23][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[23] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11000':  # verifica o ultimo bit do end memoria (index da cache = 000)
        if endCache[24][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[24] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[24][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[24][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[24] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11001':  # verifica o ultimo bit do end memoria (index da cache = 001)
        if endCache[25][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[25] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[25][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[25][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[25] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11010':  # verifica o ultimo bit do end memoria (index da cache = 010)
        if endCache[26][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[26] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[26][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[26][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[26] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11011':  # verifica o ultimo bit do end memoria (index da cache = 011)
        if endCache[27][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[27] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[27][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[27][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[27] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11100':  # verifica o ultimo bit do end memoria (index da cache = 100)
        if endCache[28][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[28] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[28][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[28][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[28] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11101':  # verifica o ultimo bit do end memoria (index da cache = 101)
        if endCache[29][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[29] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[29][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[29][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[29] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11110':  # verifica o ultimo bit do end memoria (index da cache = 110)
        if endCache[30][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[30] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[30][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[30][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[30] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[1:] == '11111':  # verifica o ultimo bit do end memoria (index da cache = 11111)
        if endCache[len(endCache) - 1][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[len(endCache) - 1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[len(endCache) - 1][0] == '1':  # bit de validade = 1
            if linha[0] == endCache[len(endCache) - 1][1]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[len(endCache) - 1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    print(endCache)

print('\nHit: {}'.format(hit))
print('Miss: {}'.format(miss))


# fechando os 2 arquivos abertos

m5.close()
prog.close()
