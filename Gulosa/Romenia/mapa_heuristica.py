from collections import defaultdict

class MapaHeuritica:
    def __init__(self):
        self._filho = []
        self._mapa = {}
        self._lista = []
        self._distancia=[]
        self.count = 0

    def mapa_chaves(self, b):
        self._mapa = defaultdict(list)
        while self.count < (len(b)):
            self._filho.append(b[self.count::len(b)])
            d = (self._filho[self.count][0]).split()
            a = d.pop(0)
            c = list(d)
            for k in range(len(c)):
                    self._mapa[a].append(c[k])
            self.count += 1
        for i in self._mapa:
            self._mapa[i][0] = int(self._mapa[i][0])

        return self._mapa



