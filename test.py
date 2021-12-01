from graph_lib import Graph
from rich import print

def prim(G: list[list[int]], nstart: int) -> tuple[list[list[int]], list]:
    """
    Algo PRIM, needs a starting point number and a matrix of a graph
    Returns another matrix, with represents the tree to walkthrough the graph, as well as the list of points in order
    """
    A = [nstart]
    B = [n for n in range(len(G)) if n != nstart]
    S = [[0 for _ in range(len(G))] for __ in range(len(G))]
    pred = []

    while B:
        min_weight = ""
        for i in A:
            for j in B:
                if G[i][j] and (not min_weight or G[i][j] < min_weight):
                    min_weight = G[i][j]
                    j_min, i_min = j, i

        A.append(j_min)
        B.remove(j_min)
        pred.append(i_min)
        S[i_min][j_min] = min_weight
        S[j_min][i_min] = min_weight
    
    print('pred :', pred)
    
    return S, A

def main():
    g = Graph()

    # sommets = [0, 1, 2, 3, 4, 5, 6]

    g.ajouter_arete(0, 1, 2)
    g.ajouter_arete(0, 2, 3)
    g.ajouter_arete(0, 3, 4)
    g.ajouter_arete(0, 4, 4)
    g.ajouter_arete(0, 5, 3)
    g.ajouter_arete(0, 6, 3)

    g.ajouter_arete(1, 2, 3)
    g.ajouter_arete(1, 3, 2)
    g.ajouter_arete(1, 4, 2)
    g.ajouter_arete(1, 5, 4)
    g.ajouter_arete(1, 6, 3)

    g.ajouter_arete(2, 3, 3)
    g.ajouter_arete(2, 4, 1)
    g.ajouter_arete(2, 5, 6)
    g.ajouter_arete(2, 6, 4)

    g.ajouter_arete(3, 4, 2)
    g.ajouter_arete(3, 5, 3)
    g.ajouter_arete(3, 6, 1)

    g.ajouter_arete(4, 5, 5)
    g.ajouter_arete(4, 6, 3)

    g.ajouter_arete(5, 6, 2)

    #g.matrice()

    print(g.get_matrice())

    (S, A) = prim(g.get_matrice(), 6)

    print('prim matrix :', S)

    print('path :', A)

if __name__ == '__main__':
    main()





