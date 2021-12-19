"""
Interface graphique pour utilser algo PRIM dans le cadre du probleme du voyageur de commerce
"""
from tkinter import * # GUI module
from tkinter import ttk, messagebox as msgbox # addons for GUI
from threading import Thread # Permet de faire tourner des fonctions en meme temps (async)
# Frames individuelles
from mapFrame import MapFrame 

__AUTHORS__ = 'Raphaël, Elisa and Grégoire'
__VERSION__ = '1.1'

X = 700
Y = 700

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
        self.size = (x, y)
        self.villes = (
            "clermond ferrand", "bordeaux", "bayonne", "toulouse", "marseille", "nice", "nantes",
            "rennes", "paris", "lille", "dijon", "valences", "aurillac", "orleans", "reims", "starsbourg",
            "limoges", "troyes", "le havre", "cherbourg", "brest", "niort"
        )
        self.__setup_frames()
    
    def __setup_frames(self):
        """
        Place les Frames dans la grille
        """
        def motion(event):
            if event.widget.__dict__['master'] == self.mapFrame and not event.widget['text'] in self.villes: # the map is focused
                x, y = event.x, event.y
                self.mapFrame.show_selection(x, y)

        self.mapFrame = MapFrame(self)   
        update_map = Thread(target=self.mapFrame.resize_map) # resize image thread
        update_map.setDaemon(True) # will be closed when the main thread is closed
        update_map.start()
        self.bind('<Motion>', motion)
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value = None):
        if value:
            self._size = value
        else:
            (x, y) = (self.winfo_width(), self.winfo_height())
            self._size = (x, y)

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
