# Cache-Simulator
Simulador de atividade da memória cache durante execução de um programa

## Introdução
O objetivo deste trabalho prático é familiarizar o aluno com os principais conceitos
estudados sobre Hierarquia de Memória. Foram estudados três tipos de projeto de
organização da cache (Mapeamento direto, associativo por conjunto e totalmente
associativo). Este trabalho destina-se a utilizar de forma prática esses projetos de cache.
Dessa forma, será necessário a implementação desses tipos de cache e a análise da
execução para grupos de entradas previamente fornecidos.

## 1. O simulador
Faça um simulador de memória cache que tenha os seguintes tipos de projeto de cache:

a) Mapeamento direto;

b) Associativo por conjunto (2 e 4 vias);

c) Totalmente associativo.

As políticas de substituição (LRU, FIFO e LFU) da cache devem ser implementadas para
os tipos de projeto que necessitarem de uma política de substituição;


## 2. O experimento
O experimento deverá conter uma análise das taxas de falha e acerto para grupo de arquivo.
A memória principal tem o mesmo tamanho para cada grupo, 64 posições, porém, ela é organizada de forma distinta para atender cada projeto de cache.

Os programas em cada grupo (exemplo: Prog1.1 = Prog2.1 = Prog3.1 = Prog4.1
= Prog5.1) são iguais sendo as instruções podendo ser organizadas de forma
diferente para atender cada grupo;

**Grupo 1**: Cache de 2 linhas com endereços de 6 bits (5 para TAG e 1 para índice)

**Grupo 2**: Cache de 4 linhas com endereços de 6 bits (4 para TAG e 2 para índice)

**Grupo 3**: Cache de 8 linhas com endereços de 6 bits (3 para TAG e 3 para índice)

**Grupo 4**: Cache de 16 linhas com endereços de 6 bits (2 para TAG e 4 para índice)

**Grupo 5**: Cache de 32 linhas com endereços de 6 bits (1 para TAG e 5 para índice)


