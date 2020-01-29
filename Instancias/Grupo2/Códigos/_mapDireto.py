'''
Grupo 2
Cache de 4 linhas com 6 bits de endereço, sendo 2 para index e 4 para tag

arquivos:
- m2
- Prog2.1
- Prog2.2
- Prog2.3
- Prog2.4
- Prog2.5
'''

def progs():
    print('Escolha o programa a ser executado: ')
    print('[1] 2_1')
    print('[2] 2_2')
    print('[3] 2_3')
    print('[4] 2_4')
    print('[5] 2_5')
    opcao = int(input(''))

    if opcao == 1:
        prog = "../prog2_1.txt"
    elif opcao == 2:
        prog = "../prog2_2.txt"
    elif opcao == 3:
        prog = "../prog2_3.txt"
    elif opcao == 4:
        prog = "../prog2_4.txt"
    elif opcao == 5:
        prog = "../prog2_5.txt"
    return prog


with open('../m2.txt', 'r') as m2:  # abrindo arquivo de memoria m2
    endMem = m2.readlines()           # armazenando valores em uma lista endMem
endMem = [x.strip() for x in endMem]  # tirando espaços vazios da lista

with open(progs(), 'r') as prog:  # abrindo arquivo do programa prog1
    endProg = prog.readlines()
endProg = [x.strip() for x in endProg]

endCache = ['0', '0','0', '0']  # lista de endereços de cache iniciados vazios

'''
endCache[0] -> bit de validade
endCache[5:] -> index
endCache[1:4] -> tag

procura-se o endereço dado pelo processador (programas) na memória cache
'''

miss = 0
hit = 0

for linha in endProg:
    if linha[4:] == '00':  # verifica o ultimo bit do end memoria (index da cache = 00)
        if endCache[0][0] == '0':  # bit de validade da primeira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[0][0] == '1':  # bit de validade = 1
            if linha[0:3] == endCache[0][1:4]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[0] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[4:] == '01':  # verifica o ultimo bit do end memoria (index da cache = 01)
        if endCache[1][0] == '0':  # bit de validade da segunda posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[1][0] == '1':  # bit de validade = 1
            if linha[0:3] == endCache[1][1:4]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[1] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[4:] == '10':  # verifica o ultimo bit do end memoria (index da cache = 10)
        if endCache[2][0] == '0':  # bit de validade da terceira posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[2][0] == '1':  # bit de validade = 1
            if linha[0:3] == endCache[2][1:4]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[2] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    elif linha[4:] == '11':  # verifica o ultimo bit do end memoria (index da cache = 11)
        if endCache[3][0] == '0':  # bit de validade da quarta posição da cache
            print('Miss\n')
            for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                if linhaM1 == linha:
                    endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
            miss += 1
        elif endCache[3][0] == '1':  # bit de validade = 1
            if linha[0:3] == endCache[3][1:4]:  # comparando a tag
                print('Hit\n')
                hit += 1
            else:
                print('Miss\n')
                for linhaM1 in endMem:  # procura endereço dado pelo programa na memoria principal
                    if linhaM1 == linha:
                        endCache[3] = '1' + linhaM1  # substitui a linha da cache com o novo valor da memoria
                miss += 1
    print(endCache)





print('\nHit: {}'.format(hit))
print('Miss: {}'.format(miss))


# fechando os 2 arquivos abertos

m2.close()
prog.close()
