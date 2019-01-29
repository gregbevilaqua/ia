from collections import deque

class Gulosa():
    def __init__(self):
        self.node_l = []
        self.node = deque()
        self.lista = []

    def add_aresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def sucessor(self, u, v, limite,node,dic): # Busca Limitada
        if u == v: return True
        if limite <= 0: return False
        lista = []
        for i in range(len(self.grafo[u])):
            if self.grafo[u][i]:
                lista.append(i)
        for j in lista:
            if (self.DLS(j, v, limite-1, node, dic)):
                node.append(dic[j])
                return True
        return False

    def gulosa(self,v,u):
        a=v
        b=u
        while a!=b:
            node.appendleft(a)
            for j in range(len(mfronteira[a])):
                node_1.append(mfronteira[a][j])
            #Vamos ordernar a lista pela distancia
            node_1.sort(key=lambda x: x[1])
            a=(node_1.pop(0)).pop(0)
            node_1.clear()
            if a==b:
                node.appendleft(b)
                node.reverse()
                return node
            else:
                return gulosa(a,b)