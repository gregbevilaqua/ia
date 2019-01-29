from collections import deque
import random as rnd

class ProfundidadeLimitada:
    def __init__(self, numvert):
        self.numvert = numvert
        self.grafo = [[0] * numvert for i in range(numvert)]
        self.node = deque()
        self.borda = deque()
        self.caminho = deque()
        self.node_final = []
        self.visitados = [False]*numvert
        self.origem = []
        self.cont = 0
        self.conteiner = []

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

    def add_aresta(self,u,v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def mostrar(self):
        for i in self.grafo:
            for j in i:
                print(j, end=' ')
            print('')

    def atualizar(self,aux):
        rnd.shuffle(aux)
        for i in range(len(aux)):
            self.borda.popleft()
        for i in range(len(aux)):
            self.borda.appendleft(aux[i])
        return self.borda

    def expandir(self,u,v,limite):
        aux = []
        self.origem.append(u)
        self.visitados[u] = True
        while self.cont < limite:
            for i in range(self.numvert):
                if self.grafo[u][i] == 1 and self.visitados[i] == False:
                    aux.append(i)
                    self.borda.appendleft(i)
                    if i == v:
                        self.node.append(v)
                        break
            self.borda = self.atualizar(aux)
            self.cont += 1
            if len(self.borda) > 0:
                self.removido = self.borda.popleft()
                if self.removido != v:
                    self.node.append(self.removido)
                    if limite == self.cont:
                        a = self.origem[0]
                        b = self.node[0]
                        self.conteiner.append(b)
                        for i in self.conteiner:
                            self.visitados[i] = True
                        self.origem.clear()
                        self.node.clear()
                        self.borda.clear()
                        self.cont = 0
                        self.expandir(a,v,limite)
                    else:
                        self.expandir(self.removido,v,limite)
            return self.node

    def destino(self,u,v,limite, dic):
        self.caminho = self.expandir(u, v, limite)
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
