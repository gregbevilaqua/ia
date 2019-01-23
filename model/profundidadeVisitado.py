from collections import deque
import random as rnd

class ProfundidadeVisitado:
    def definirProblema(self, definido, listdic):
        while definido == False:
            origem = (str(input('Cidade Origem:')).title())
            if origem in listdic and origem.isalpha():
                x = listdic.index(origem)
                destino = (str(input('Cidade Destino:')).title())
                if destino in listdic and destino.isalpha():
                    y = listdic.index(destino)
                    return x, y

    def __init__(self,numvert):
        self.numvert = numvert
        self.grafo = [[0] * numvert for i in range(numvert)]
        self.node = deque()
        self.borda = deque()
        self.bordas = deque()
        self.node_final = []
        self.visitados = [False] * numvert

    def add_aresta(self,x,y):
        self.grafo[x][y] = 1
        self.grafo[y][x] = 1

    def mostrar(self):
        for i in self.grafo:
            for j in i:
                print(j, end=' ')
            print('')

    def expandir(self,a, b):
        aux = []
        self.destino = b
        self.visitados[a] = True
        for i in range(self.numvert):
            if self.grafo[a][i] == 1 and self.visitados[i] == False:
                aux.append(i)
            print(aux)
        rnd.shuffle(aux)
        for i in range(len(aux)):
            if aux[i] not in self.borda:
                self.borda.appendleft(aux[i])
            else:
                self.borda.remove(aux[i])
                self.borda.appendleft(aux[i])
        if len(self.borda) > 0:
            self.removido = self.borda.popleft()
            if a != b:
                self.node.append(self.removido)
                # print(self.node)
                self.expandir(self.removido,self.destino)
        return self.node

    def destino(self,x,y, dic):
        self.caminho = self.expandir(x,y)
        if x > y:
            self.caminho.appendleft(y)
            self.caminho.reverse()
        else:
            self.caminho.appendleft(x)
        for i in self.caminho:
            for j in dic:
                if i == j:
                    self.node_final.append(dic[j])
        print(self.node_final)
