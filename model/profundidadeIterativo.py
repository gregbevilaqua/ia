from collections import deque
import random as rnd

class ProfundidadeIterativo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]
        self.visitados = [False] * vertices

    def definirProblema(self, definido, listdic):
        while definido == False:
            origem = (str(input('Origem:')).title())
            if origem in listdic and origem.isalpha():
                x = listdic.index(origem)
                destino = (str(input('Destino:')).title())
                if destino in listdic and destino.isalpha():
                    y = listdic.index(destino)
                    lim = (int(input('Limite:')))
                    return x, y, lim

    def add_aresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def DLS(self, u, v, limite,node,dic): # Busca Limitada
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

    def IDDFS(self, u, v, limite,node,dic): # Busca Aprofundamento Iterativo
        for i in range(limite):
            if (self.DLS(u, v, i,node,dic)):
                return True
        return False
