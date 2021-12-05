"""
TODO
Frame principale avec l'image de la carte, ou sera ajouté le chemin à parcourir
"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import sleep

PATH_TO_MAP = 'assets/map.png'

villes = (
    "clermond ferrand", "bordeaux", "bayonne", "toulouse", "marseille", "nice", "nantes",
    "rennes", "paris", "lille", "dijon", "valences", "aurillac", "orleans", "reims", "starsbourg",
    "limoges", "troyes", "le havre", "cherbourg", "brest", "niort"
)

tab_pos_villes = ( # format (x, y), same order as villes list
    (77, 364), (345, 718),(284, 845),(481, 834),(749, 864),(881, 825),(277, 484),(269, 393),(544, 317),
    (592, 127),(727, 473),(719, 709),(549, 708),(514, 416),(657, 275),(913, 344),(470, 622),
    (660, 373),(390, 250),(258, 213),(49, 355),(342, 579)
)

class MapFrame(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        img = Image.open(PATH_TO_MAP)
        self.mapImg = ImageTk.PhotoImage(img)
        self.__create_map()
        self.place(relx=.2, rely=0, relwidth=.8, relheight=1)
    
    def __create_map(self):
        self.mapLabel = Label(self, text='map', image=self.mapImg)
        self.mapLabel.pack()
    
    def show_selection(self, pos: tuple[int, int]):
        print(f'pos : {pos}')
    
    def resize_map(self):
        pred_size = []
        while 1:
            img = Image.open(PATH_TO_MAP)
            # get the MapFrame size
            self.master.size = () # update the size
            win_size = list(self.master.size)
            win_size[0] = int(win_size[0] * .8)
            if win_size != pred_size: # size changed
                print("size changed")
                # resize the image in the available space
                img = img.resize(tuple(win_size))
                # reset the image to update the map label
                self.mapImg = ImageTk.PhotoImage(img)
                self.mapLabel['image'] = self.mapImg
            pred_size = [*win_size]
            sleep(.5)

    def show_path(self, path: list):
        pass