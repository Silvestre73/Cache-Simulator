#!usr/bin/env python
# -*- coding: utf8 -*-


def progs():
    print('Escolha o programa a ser executado: ')
    print('[1] 1_1')
    print('[2] 1_2')
    print('[3] 1_3')
    print('[4] 1_4')
    print('[5] 1_5')
    opcao = int(input(''))
    prog = ""
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


with open('../m1.txt', 'r') as m1:
    endMem = m1.readlines()
endMem = [x.strip() for x in endMem]

with open(progs(), 'r') as prog:
    endProg = prog.readlines()
endProg = [x.strip() for x in endProg]

endCache = ['0', '0']

miss = 0
hit = 0

for linhaP in endProg:
    for linhaC in endCache:
        if linhaP == linhaC:
            print('Hit')
            hit += 1
        else:
            print('Miss')
            miss += 1
            for linhaM in endMem:
                if linhaP == linhaM and len(endCache) < 2:
                    endCache.append(linhaP)
                elif linhaP == linhaM and len(endCache) == 2:
                    endCache.pop(0)
                    endCache.append(linhaM)
    print(endCache)

print('Hit: {}'.format(hit))
print('Miss: {}'.format(miss))

m1.close()
prog.close()
