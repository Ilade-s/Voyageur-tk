from graph_lib import Graph
from rich import print

def prim(G: list[list[int]], nstart: int) -> tuple[list[list[int]], list, list]:
    """
    Algo PRIM, needs a starting point number and a matrix of a graph
    Returns another matrix, with represents the tree to walkthrough the graph, as well as the path, and the list of predecessors of each node in the path
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
    
    return S, A, pred

def upgrade_prim(start, circuit, A, pred):
    circuit[0] = start
    circuit[1] = start
    for i in range(1, len(A)):
        ii = i
        while circuit[ii] != pred[i - 1]:
            circuit[ii + 1] = circuit[ii]
            ii -= 1
        circuit[ii + 1] = circuit[ii]
        circuit[ii] = A[i]
    
    return circuit




def main():
    g = Graph()

    # sommets = [0, 1, 2, 3, 4, 5, 6]

    g.ajouter_arete("a", 1, 2) # a is node 0
    g.ajouter_arete("a", 2, 3)
    g.ajouter_arete("a", 3, 4)
    g.ajouter_arete("a", 4, 4)
    g.ajouter_arete("a", 5, 3)
    g.ajouter_arete("a", 6, 3)

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

    (S, A, pred) = prim(g.get_matrice(), 6)

    print('prim matrix :', S)

    circuit = A + [A[0]]

    print(circuit[:-1])

    dict_sommets = g.get_dict_sommets()

    circuit_names = [dict_sommets[n] for n in circuit]

    print('path before upgrade :', circuit_names)

    circuit = upgrade_prim(6, circuit, A, pred)

    circuit_names = [dict_sommets[n] for n in circuit]

    print('path after upgrade :', circuit_names)

if __name__ == '__main__':
    main()





