"""
Interface graphique pour utilser algo PRIM dans le cadre du probleme du voyageur de commerce
"""
from tkinter import * # GUI module
from tkinter import ttk, messagebox as msgbox # addons for GUI
# Frames individuelles TODO

__AUTHORS__ = 'Raphaël, Elisa and Grégoire'
__VERSION__ = '0.1'

X = 1000
Y = 600

class TopLevel(Tk):
    """
    Représente le client (l'interface)
    """
    def __init__(self, x=X, y=Y) -> None:
        super().__init__()
        self.version = __VERSION__
        self.authors = __AUTHORS__
        self.iconphoto(True, PhotoImage(file="assets/logo.png"))
        self.title(
            f"Voyageur v{__VERSION__}")
        self.geometry("{}x{}".format(x, y))
        self.__setup_frames()

    def __setup_frames(self):
        """
        Place les Frames dans la grille
        """       

def main():
    print("===============================================================")
    print(f"Voyageur v{__VERSION__}")
    print(f"Made by {__AUTHORS__}")
    print("Source : https://github.com/Ilade-s/Voyageur-tk")
    print("Assets : https://feathericons.com/")
    print("===============================================================")

    client = TopLevel()
    client.mainloop()


if __name__ == '__main__':
    main()