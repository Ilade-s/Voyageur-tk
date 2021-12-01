"""
TODO
Frame qui sera placée à côté de celle du graphe 
Contiendra soit :
    - des infos sur le graphe (InfoFrame) 
    - les résultats de l'algo PRIM (ResultFrame : arbre + chemin)
"""
from tkinter import *
from tkinter import ttk

class SideFrame(Frame):
    
    def __init__(self, master) -> None:
        """
        Frame qui contiendra une des sub-Frames
        les variables nécessaires à InfoFrame et ResultFrame y sont associés, permettant un changement de sub-Frame sans perte de variables
        """
        super().__init__(master)
        self.master = master

class InfoFrame(LabelFrame):

    def __init__(self, master) -> None:
        """
        Sub-frame de SideFrame donnant diverses informations sur le graphe (ordre...)
        """
        super().__init__(master, text='Informations graphe')
        self.master = master

class ResultFrame(LabelFrame):

    def __init__(self, master) -> None:
        """
        Sub-frame de SideFrame permettant de visualiser les résultats de l'algo PRIM notamment l'abre recouvrant et le chemin
        """
        super().__init__(master, text='Résultats PRIM')
        self.master = master

class TreeFrame(LabelFrame):

    def __init__(self, master) -> None:
        """
        Sub-frame de ResultFrame permettant de visualiser l'arbre recouvrant
        """
        super().__init__(master, text='Arbre recouvrant')
        self.master = master

class PathFrame(LabelFrame):

    def __init__(self, master) -> None:
        """
        Sub-frame de ResultFrame permettant de visualiser le chemin a parcourir trouvé par l'algo
        """
        super().__init__(master, text='Chemin à parcourir')
        self.master = master

