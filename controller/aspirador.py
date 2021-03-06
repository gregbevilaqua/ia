from N1.model.largura import Largura
from N1.model.profundidade import Profundidade
from N1.model.profundidadeVisitado import ProfundidadeVisitado
from N1.model.profundidadeIterativo import ProfundidadeIterativo
from N1.model.profundidadeLimitada import ProfundidadeLimitada
from N1.model.gulosaV import gulosa,sucessor
from N1.model.aEstrela import sucessorStar, aStar

if __name__ == '__main__':
    print("\nMétodos configurados: Largura, Profundidade, ProfundidadeVisitado, ProfundidadeIterativo, ProfundidadeLimitada, Gula pela melhor Escolha e A*\n")
    metodo = (str(input('Por qual metodo você quer resolver o problema?:')).title())

    dic = {0: 'Ess', 1: 'Dss', 2: 'Els', 3: 'Dls',
           4: 'Esl', 5: 'Dsl', 6: 'Ell', 7: 'Dll'}
    listdic = list(dic.values())
    definido = False
    node = []

    if metodo == 'Largura':
        g = Largura(8)
        g.add_aresta(0, 1)
        g.add_aresta(0, 2)
        g.add_aresta(1, 5)
        g.add_aresta(2, 3)
        g.add_aresta(3, 7)
        g.add_aresta(4, 5)
        g.add_aresta(4, 6)
        g.add_aresta(6, 7)
        a, b = g.definirProblema(definido, listdic)
        lista = g.sucessor(a, b)
        lista.reverse()
        res = g.caminho(lista)
        res.reverse()
        print(res)
        g.destino(res, dic)

    elif metodo == "Profundidade":

        g = Profundidade(8)
        g.add_aresta(0, 1)
        g.add_aresta(0, 2)
        g.add_aresta(1, 5)
        g.add_aresta(2, 3)
        g.add_aresta(3, 7)
        g.add_aresta(4, 5)
        g.add_aresta(4, 6)
        g.add_aresta(6, 7)
        # t = g.expandir(0,7)
        x, y = g.definirProblema(definido, listdic)
        g.destino(x, y, dic)
        # g.mostrar()

    elif metodo == "Profundidadevisitado":
        g = ProfundidadeVisitado(22)
        g.add_aresta(0, 15)
        g.add_aresta(0, 16)
        g.add_aresta(0, 19)
        g.add_aresta(1, 5)
        g.add_aresta(1, 6)
        g.add_aresta(1, 13)
        g.add_aresta(1, 17)
        g.add_aresta(2, 3)
        g.add_aresta(2, 14)
        g.add_aresta(2, 13)
        g.add_aresta(3, 2)
        g.add_aresta(3, 10)
        g.add_aresta(4, 7)
        g.add_aresta(5, 15)
        g.add_aresta(5, 1)
        g.add_aresta(6, 1)
        g.add_aresta(7, 4)
        g.add_aresta(7, 17)
        g.add_aresta(8, 11)
        g.add_aresta(8, 18)
        g.add_aresta(9, 10)
        g.add_aresta(9, 16)
        g.add_aresta(10, 3)
        g.add_aresta(10, 9)
        g.add_aresta(11, 8)
        g.add_aresta(12, 19)
        g.add_aresta(12, 15)
        g.add_aresta(13, 1)
        g.add_aresta(13, 2)
        g.add_aresta(13, 14)
        g.add_aresta(14, 13)
        g.add_aresta(14, 2)
        g.add_aresta(14, 15)
        g.add_aresta(15, 5)
        g.add_aresta(15, 14)
        g.add_aresta(15, 12)
        g.add_aresta(15, 0)
        g.add_aresta(16, 0)
        g.add_aresta(16, 9)
        g.add_aresta(17, 18)
        g.add_aresta(17, 7)
        g.add_aresta(17, 1)
        g.add_aresta(18, 8)
        g.add_aresta(18, 17)
        g.add_aresta(19, 0)
        g.add_aresta(19, 12)
        x, y = g.definirProblema(definido, listdic)
        g.destino(x, y, dic)
        # g.mostrar()

    elif metodo == "Profundidadeiterativo":
        g = ProfundidadeIterativo(8)
        g.add_aresta(0, 1)
        g.add_aresta(0, 2)
        g.add_aresta(1, 5)
        g.add_aresta(2, 3)
        g.add_aresta(3, 7)
        g.add_aresta(4, 5)
        g.add_aresta(4, 6)
        g.add_aresta(6, 7)
        x, y, l = g.definirProblema(definido, listdic)
        if g.IDDFS(x, y, l, node, dic) == True:
            nodes = list(reversed(node))
            print([dic[0]] + nodes)
        else:
            print('Não Alcançado!')

    elif metodo == "Profundidadelimitada":
        g = ProfundidadeLimitada(8)
        g.add_aresta(0, 1)
        g.add_aresta(0, 2)
        g.add_aresta(1, 5)
        g.add_aresta(2, 3)
        g.add_aresta(3, 7)
        g.add_aresta(4, 5)
        g.add_aresta(4, 6)
        g.add_aresta(6, 7)
        x, y, l = g.definirProblema(definido, listdic)
        g.destino(x, y, l, dic)

    elif metodo == "Gulosa":
        mfronteira=sucessor()
        origem = (str(input('Origem:')).title())
        destino = (str(input('Destino:')).title())
        GS = gulosa(origem.upper(),destino.upper())
        print('Busca Gulosa:', GS)

    elif metodo == "A*":
        #lerAspirador()
        sucessorStar()
        origem = (str(input('Origem:')).title())
        destino = (str(input('Destino:')).title())
        aEstrela = aStar(origem.upper(), destino.upper())
        print('A*:', aEstrela)

    else:
        print("Você não selecionou nenhuma opção válida")