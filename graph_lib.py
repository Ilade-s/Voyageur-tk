from rich import print

class Graph:
    """graph = { "a" : {"b":2,"c":1},  ...        
        }
        graphe orienté ou non
    """
    def __init__(self, graphe={}, oriente=False) -> None:
        self.graphe = graphe
        self.oriente = oriente
    
    def ajouter_sommet(self, sommet: str) -> None:
        self.graphe[sommet] = {}
    
    def get_dict_sommets(self) -> list:
        return {
            n: s for n, s in
            zip(range(len(self.get_matrice())), list(self.graphe.keys()))
        }

    def degre(self, sommet) -> int:
        return len(self.graphe[sommet])

    def ajouter_arete(self, sommet1, sommet2, poids=1) -> None:
        if sommet1 not in self.graphe.keys():
            self.ajouter_sommet(sommet1)
        if sommet2 not in self.graphe.keys():
            self.ajouter_sommet(sommet2)
        self.graphe[sommet1][sommet2] = poids
        if not self.oriente:    
            self.graphe[sommet2][sommet1] = poids

    def afficher(self) -> None:
        print(self.graphe)

    def ordre(self) -> int:
        return len(self.graphe)

    def get_matrice(self) -> list[list]:
        mat = [
            [
                self.graphe[s][s2] if s2 in self.graphe[s].keys()
                else 0
                for s2 in self.graphe.keys()
            ]
            for s in self.graphe.keys()
        ]
        
        return mat

    def matrice(self) -> None:
        for l in self.get_matrice():
            print(l)

def mat_to_dict(matrix: list[list[int]], nodeList: list[str]) -> dict[str: dict[dict[str: int]]]:
    """
    converts a list of node and their matrix in a dict usable for the Graph class
    """
    assert len(matrix) == len(nodeList) and len(matrix[0]) == len(nodeList), "matrix doesn't correspond to slist"

    return {
        node: {nodeList[i]: w
            for w, i in zip(wList, range(len(wList)))
            if nodeList[i] != node
        }
        for wList, node in zip(matrix, nodeList)
    }




def main():
    graphe = Graph()
    graphe.ajouter_arete('a', 'b', 3)
    graphe.ajouter_arete('a', 'c', 4)
    graphe.ajouter_arete('c', 'd')
    graphe.ajouter_arete('b', 'd')
    graphe.ajouter_arete('b', 'e')
    graphe.ajouter_arete('d', 'e')
    graphe.ajouter_arete('e', 'f')
    graphe.ajouter_arete('e', 'f')
    graphe.ajouter_arete('g', 'h')
    graphe.ajouter_arete('f', 'g')

    graphe.afficher()
    graphe.matrice()

if __name__ == '__main__': # test
    main()
