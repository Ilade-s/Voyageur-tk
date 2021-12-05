"""
TODO
Frame qui sera placée en dessous de l'image
Contiendra l'action à effectuer (choisir ville...) et un bouton pour démarrer l'algo PRIM
"""
from tkinter import *
from tkinter import ttk

class InfoFrame(LabelFrame):

    def __init__(self, master) -> None:
        """
        Frame qui sera placée en dessous de l'image
        Contiendra l'action à effectuer (choisir ville...) et un bouton pour démarrer l'algo PRIM
        """
        super().__init__(master, text='Informations et contrôles', foreground='white', background='#424864')
        self.master = master
        self.__create_widgets()
        self.place(relx=0, rely=0, relwidth=.2, relheight=1)
    
    def __create_widgets(self):
        pass

