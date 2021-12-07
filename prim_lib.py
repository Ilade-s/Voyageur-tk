"""
Class with will be used as an API for the PRIM algorithm and upgrade
"""
from rich import print

MATRIX = [ # matrice des distances
    [0,376,555,377,475,632,536,594,424,639,334,263,157,300,558,630,230,428,593,716,822,402],
    [376,0,185,245,646,803,347,466,586,800,649,652,307,462,719,945,221,662,685,693,651,187],
    [555,185,0,300,693,850,532,651,770,985,828,788,486,647,903,1124,406,847,870,877,830,371],
    [377,245,300,0,404,561,588,705,680,896,651,192,255,556,814,947,291,758,849,931,883,425],
    [457,646,693,404,0,207,986,1052,775,1000,506,214,422,758,798,801,691,688,962,1121,1280,824],
    [632,803,850,561,207,0,1144,1210,933,1148,663,372,580,916,956,785,849,846,1120,1279,1441,982],
    [536,347,532,588,986,1144,0,113,385,600,639,781,493,335,518,865,325,517,385,340,298,142],
    [594,466,651,705,1052,1210,113,0,349,564,617,834,614,302,483,830,446,482,279,234,242,263],
    [424,586,770,680,775,933,385,349,0,219,315,563,572,132,144,491,392,178,197,356,591,412],
    [639,800,985,896,1000,1148,600,564,219,0,501,789,788,348,206,525,608,329,318,509,760,627],
    [334,649,828,651,506,663,639,617,315,501,0,294,482,314,299,331,434,189,505,664,860,594],
    [263,652,788,192,214,372,781,834,563,789,294,0,278,555,595,598,516,484,759,918,1077,656],
    [157,307,486,255,422,580,493,614,572,788,482,278,0,448,705,778,168,575,740,779,791,333],
    [300,462,647,556,758,916,335,302,132,348,314,555,448,0,266,588,268,210,302,430,544,290],
    [558,719,903,814,798,956,518,483,144,206,299,595,705,266,0,351,526,126,352,503,725,545],
    [630,945,1124,947,801,785,865,830,491,525,331,598,778,588,351,0,731,387,700,851,1072,866],
    [230,221,406,291,691,849,325,446,392,608,434,516,168,268,526,731,0,471,562,616,622,164],
    [428,662,847,758,688,846,517,482,178,329,189,484,575,210,126,387,471,0,375,534,730,494],
    [593,685,870,849,962,1120,385,279,197,318,505,759,740,302,352,700,562,375,0,216,466,485],
    [716,693,877,931,1121,1279,340,234,356,509,664,918,779,430,503,851,616,534,216,0,421,489],
    [822,651,830,883,1280,1441,298,242,591,760,860,1077,791,544,725,1072,622,730,466,421,0,439],
    [402,187,371,425,824,982,142,263,412,627,594,656,333,290,545,866,164,494,485,489,439,0]
]

VILLES = (
    "clermond ferrand", "bordeaux", "bayonne", "toulouse", "marseille", "nice", "nantes",
    "rennes", "paris", "lille", "dijon", "valences", "aurillac", "orleans", "reims", "starsbourg",
    "limoges", "troyes", "le havre", "cherbourg", "brest", "niort"
)

class PRIM:
    """
    Class for use of the prim algorithm

    Attributes :
    ------------
        - .matrix : matrice des poids (distances)
        - .villes : liste des noms des sommets dans l'ordre (les noms de villes)
        - .nstart : nom du sommet de départ (ville)
        - .path : list of the names of the nodes, result from .execute()
        - .path_upgraded : same of .path, but is the result of .upgrade()
    """

    def __init__(self, matrix=MATRIX, villes=VILLES) -> None:
        self.matrix = matrix
        self.villes = villes
        self.executed = False
        self._path = []
    
    def execute(self, nstart: int) -> tuple[list[list[int]], list, list]:
        """
        Executes the prim algorithm for the specified starting point (its index) :
            - The matrix of the tree will be stocked in .tree_matrix
            - The index path will be stocked in ._path
            - The list of predecessors will be stocked in .pred
        
        PARAMETER :
        -----------
            - nstart : int
                - index of the starting node in self.villes
        
        RETURN :
        -----------
            - None
        """
        self.executed = True
        G = self.matrix
        self.nstart = nstart

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

        self._A = A 
        self._path = [*A] + [nstart]
        self.pred = [*pred]
        self.tree_matrix = [*S] 
    
    def upgrade(self):
        """
        Upgrades the result of the prim algorithm (of the path)
        The newfound path will be stocked in .path_upgraded
        """
        assert self.executed, "please use .execute() before attempting to upgrade the result"
        path = [*self._path]

        path[0] = self.nstart
        path[1] = self.nstart
        for i in range(1, len(self._A)):
            ii = i
            while path[ii] != self.pred[i - 1]:
                path[ii + 1] = path[ii]
                ii -= 1
            path[ii + 1] = path[ii]
            path[ii] = self._A[i]
        
        self._path_upgraded = [*path]
    
    @property
    def path(self):
        return [
            self.villes[i]
            for i in self._path
        ]
        
    @property
    def path_upgraded(self):
        return [
            self.villes[i]
            for i in self._path_upgraded
        ]
    
    @property
    def npath_upgraded(self):
        return self._path_upgraded
    
    @property
    def npath(self):
        return self._path
        

if __name__ == '__main__':
    p = PRIM()

    p.execute(0)

    print(p.path)

    p.upgrade()

    print(p.path_upgraded)

