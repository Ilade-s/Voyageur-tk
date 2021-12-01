"""
TODO
Barre de menus déroulants située en haut de la fenêtre
"""
from tkinter import *

class MenuBar(Menu):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master