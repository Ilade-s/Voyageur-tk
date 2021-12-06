"""
TODO
Barre de menus déroulants située en haut de la fenêtre
"""
from tkinter import *
from tkinter import messagebox as msgbox

class MenuBar(Menu):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.add_command(
            label="About", command=lambda: msgbox.showinfo("About",
                    f"Voyageur v{self.master.version}\nMade by {self.master.authors}, 2021 \
                    \nSource : https://github.com/Ilade-s/Voyageur-tk \
                    \nAssets : https://feathericons.com/"))