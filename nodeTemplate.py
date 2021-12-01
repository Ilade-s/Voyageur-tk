"""
TODO
"""
from tkinter import *

class NodeTemplate(Frame):
    
    def __init__(self, master, relx, rely) -> None:
        """
        Template de noeud qui sera placé dans master en fonction de : 
            - de si c'est le graphe ou bien l'arbre 
            - de sa position (relx, rely)
        """
        super().__init__(master)
        self.master = master

class TreeNodeTemplate(NodeTemplate):

    def __init__(self, master) -> None:
        """
        Template de noeud d'arbre qui sera placé dans master en fonction de sa position dans l'arbre
        """
        super().__init__(master)

class GraphNodeTemplate(NodeTemplate):

    def __init__(self, master) -> None:
        """
        Template de noeud du graphe qui sera placé dans master en fonction de son statut dans l'affichage dans GraphFrame
        """
        super().__init__(master)

