from collections import deque
import random as ra

class Profundidade:
    def __init__(self, numvert):
        self.numvert = numvert
        self.grafo = [[0] * numvert for i in range(numvert)]
        self.node = deque()
        self.borda = deque()
        self.bordas = deque()
        self.node_final = []

    def definirProblema(self, definido, listdic):
        while definido == False:
            origem = (str(input('Origem:')).title())
            if origem in listdic and origem.isalpha():
                x = listdic.index(origem)
                destino = (str(input('Destino:')).title())
                if destino in listdic and destino.isalpha():
                    y = listdic.index(destino)
                    return x, y

    def add_aresta(self, x, y):
        self.grafo[x][y] = 1
        self.grafo[y][x] = 1

    def mostrar(self):
        for i in self.grafo:
            for j in i:
                print(j, end=' ')
            print('')

    #Expandindo todos os nós até o objetivo (PODENDO HAVER loops)
    def sucessor(self, x, y):
        self.node.append(x)
        self.cont = 0
        while x != y:
            for i in range(self.numvert):
                if self.grafo[x][i] == 1:
                    self.borda.appendleft(i)
            ra.shuffle(self.borda)
            if len(self.borda) > 0:
                for i in self.borda:
                    self.bordas.appendleft(i)
            self.borda.clear()
            x = self.bordas.popleft()
            self.node.append(x)
        return self.node

    def destino(self, u, v, dic):
        self.caminho = self.sucessor(u, v)
        if u > v:
            self.caminho.appendleft(v)
            self.caminho.reverse()
        else:
            self.caminho.appendleft(u)
        if self.caminho[-1] == v:
            for i in self.caminho:
                for j in dic:
                    if i == j:
                        self.node_final.append(dic[j])
            print(self.node_final)
        else:
            print('Nó Não Alcançado!')
