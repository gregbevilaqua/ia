from collections import deque
from A_star.Romenia.mapa_fronteira import MapaFronteira
from A_star.Romenia.mapa_heuristica import MapaHeuritica
from N1.model.mapa_aestrela import MapaEstrela

arq=open('C:/Users/gregb/PycharmProjects/IA/N1/arquivos/estados.txt', 'r')
arq_h = open('C:/Users/gregb/PycharmProjects/IA/N1/arquivos/heuristica.txt', 'r')
arq_e = open('C:/Users/gregb/PycharmProjects/IA/N1/arquivos/ucs.txt', 'r')

arquivo = arq.read()
linhaTexto = arquivo.splitlines()
linhaTexto.pop(0)  # eliminar o espaço

arquivo_h = arq_h.read()
linhaTexto_h = arquivo_h.splitlines()
linhaTexto_h.pop(0)  # eliminar o espaço
linhaTexto_h.pop()

arquivo_e = arq_e.read()
linhaTexto_e = arquivo_e.splitlines()
linhaTexto_e.pop(0)  # eliminar o espaço

m = MapaFronteira()
mh = MapaHeuritica()
me = MapaEstrela()

mfronteira = m.mapa_chaves(linhaTexto)
mheurist = mh.mapa_chaves(linhaTexto_h)
mestrela = me.mapa_chaves(linhaTexto_e)

lista = []
node = deque()
node_1 = []

def sucessorStar():
    for i in mheurist.keys():
        lista.append(i)
    count = 0
    for i in lista:
        for j in range(len(mfronteira[i])):
            if mfronteira[i][j][0] in lista:
                mfronteira[i][j].insert(1, mheurist[mfronteira[i][j][0]][0])
    #print(mfronteira)
    #print(mestrela)
    for i in lista:
        for j in range(len(mfronteira[i])):
            if mfronteira[i][j][0] in lista:
                a = (mestrela[i][j][1]) + (mfronteira[i][j][1])
                mfronteira[i][j].insert(1,a)
    #print(mfronteira)
    return mfronteira

def aStar(v, u):
    a = v
    b = u
    while a != b:
        node.appendleft(a)
        for j in range(len(mfronteira[a])):
            node_1.append(mfronteira[a][j])
        node_1.sort(key=lambda x: x[1])
        a = (node_1.pop(0)).pop(0)
        if a == b:
            node.appendleft(b)
            node.reverse()
            return node
        else:
            return aStar(a, b)

arq.close()
arq_h.close()