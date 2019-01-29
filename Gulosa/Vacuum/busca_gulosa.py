from collections import deque
from N1.Gulosa.Vacuum.mapa_fronteira import MapaFronteira
from N1.Gulosa.Vacuum.mapa_heuristica import MapaHeuritica

arq = open('estados.txt', 'r')
arquivo = arq.read()
linhaTexto = arquivo.splitlines()
linhaTexto.pop(0)  # eliminar o espaço

arq_h = open('heuristica.txt', 'r')
arquivo_h = arq_h.read()
linhaTexto_h = arquivo_h.splitlines()
linhaTexto_h.pop(0)  # eliminar o espaço

m = MapaFronteira()
mh = MapaHeuritica()

mfronteira = m.mapa_chaves(linhaTexto)
mheurist = mh.mapa_chaves(linhaTexto_h)
#mheurist['DLL']=1

lista = []
node = deque()
node_1 = []

def sucessor():
    # Laço para adicionar lista de vizinhos
    for i in mheurist.keys():
        lista.append(i)
    count = 0
    # Laço para adioionar h(x) a variável mfronteira
    for i in lista:
        for j in range(len(mfronteira[i])):
            if mfronteira[i][j][0] in lista:
                mfronteira[i][j].insert(1, mheurist[mfronteira[i][j][0]][0])

    return mfronteira

def gulosa(v,u):
    a=v
    b=u
    while a!=b:
        node.appendleft(a)
        for j in range(len(mfronteira[a])):
            node_1.append(mfronteira[a][j])
        #Vamos ordernar a lista pela distancia
        node_1.sort(key=lambda x: x[1])

        #Impressoes para teste
        #print(node_1)
        #for i in range(len(node_1)):
        #    print(node_1[i][1])
        a=(node_1.pop(0)).pop(0)
        node_1.clear()
        if a==b:
            node.appendleft(b)
            node.reverse()
            return node
        else:
            return gulosa(a,b)


########## FAZENDO A BUSCA GULOSA PARA A ROMENIA #############
mfronteira = sucessor()
GS=gulosa('ESS','DLL')
print('Busca Gulosa:',GS)
##############################################################

arq.close()
arq_h.close()