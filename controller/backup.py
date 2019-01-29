from collections import deque
import random as ra


class Largura:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]

    def definirProblema(self, definido, listdic):
        while definido == False:
            origem = (str(input('Cidade Origem:')).title())
            if origem in listdic and origem.isalpha():
                x = listdic.index(origem)
                destino = (str(input('Cidade Destino:')).title())
                if destino in listdic and destino.isalpha():
                    y = listdic.index(destino)
                    return x, y

    def add_aresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def mostrar(self):
        for i in self.grafo:
            for j in i:
                print(j, end=' ')
            print('')

    def sucessor(self, no):
        vizinhos = []

        return vizinhos

    def bfs(self, u, v):
        borda = [u]
        node = []

        while len(borda) > 0 and u != v:
            u = borda[0]
            for i in range(self.vertices):
                if self.grafo[u][i] == 1:
                    borda.append(i)  # Adiciona no final
            a = borda.pop(0)  # Retira o primeiro (Fila FIFO)
            node.append(a)
        return node

    # Fornece o caminho completo da Origem ao Destino
    def caminho(self, lista):
        cont = 0
        listaA = []
        x = lista[0]
        listaA.append(x)
        while len(lista) > cont:
            for i in lista:
                if self.grafo[x][i] == 1 and x != lista[-1]:
                    x = i
                    listaA.append(x)
            cont += 1
        return (listaA)

    def destino(self, lista, dic):
        listaB = []
        for j in lista:
            for i in dic:
                if i == j:
                    listaB.append(dic[i])
        print(listaB)