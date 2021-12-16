from graph_lib import *
from prim_lib import *

VILLES = (
    "clermond ferrand", "bordeaux", "bayonne", "toulouse", "marseille", "nice", "nantes",
    "rennes", "paris", "lille", "dijon", "valences", "aurillac", "orleans", "reims", "starsbourg",
    "limoges", "troyes", "le havre", "cherbourg", "brest", "niort"
)

p = PRIM()

p.execute(0)

print(p.tree_matrix)

dict_graph = mat_to_dict(p.tree_matrix, VILLES)

print(dict_graph)