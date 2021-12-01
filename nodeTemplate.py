"""
TODO
"""
from tkinter import *

class NodeTemplate(Frame):
    
    def __init__(self, master) -> None:
        """
        Template de noeud qui sera placé dans master en fonction de : 
            - de si c'est le graphe ou bien l'arbre 
            - de sa position
        """
        super().__init__(master)
        self.master = master
