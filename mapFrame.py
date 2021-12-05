"""
TODO
Frame principale avec l'image de la carte, ou sera ajouté le chemin à parcourir
"""
from os import remove
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import sleep
from threading import Thread # Permet de faire tourner des fonctions en meme temps (async)

PATH_TO_MAP = 'assets/map.png'

pos_villes = ( # format (x, y), same order as villes list
    (602, 638), (345, 718),(284, 845),(481, 834),(749, 864),(881, 825),(277, 484),(269, 393),(544, 317),
    (592, 127),(727, 473),(719, 709),(549, 708),(514, 416),(657, 275),(913, 344),(470, 622),
    (660, 373),(390, 250),(258, 213),(49, 355),(342, 579)
)

class MapFrame(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self._selection_widgets = {}
        img = Image.open(PATH_TO_MAP)
        self.mapImg = ImageTk.PhotoImage(img)
        self.__create_map()
        self.place(relx=.2, rely=0, relwidth=.8, relheight=1)
    
    def __create_map(self):
        self.mapLabel = Label(self, text='map', image=self.mapImg)
        self.mapLabel.pack()
    
    def show_selection(self, x: int, y: int):
        width, height = self.master.size
        x_factor = 1000 / (width * .8)
        y_factor = 1000 / height
        for (xv, yv), i in zip(pos_villes, range(len(pos_villes))):
            name = self.master.villes[i]
            if abs(xv / x_factor - x) < 50 / x_factor and abs(yv / y_factor - y) < 50 / x_factor: # close to the city 
                if not i in self._selection_widgets.keys():
                    w = Label(self, text=name, background='#A8B8FF', font=('Arial', int(10 + 6 / x_factor)))
                    w.place(x=xv / x_factor - 5 * len(name), y=yv / y_factor)
                    self._selection_widgets[i] = [w, ()]
            else: 
                if i in self._selection_widgets.keys():
                    if not self._selection_widgets[i][1]:# there is no active remove thread
                        remove_thread = Thread(target=self.__remove_name_widget, args=(i,))
                        remove_thread.start()
                        self._selection_widgets[i][1] = remove_thread                   
    
    def __remove_name_widget(self, i):
        sleep(.5)
        self._selection_widgets[i][0].destroy()
        self._selection_widgets.pop(i)

    def resize_map(self):
        pred_size = []
        while 1:
            img = Image.open(PATH_TO_MAP)
            # get the MapFrame size
            self.master.size = () # update the size
            win_size = list(self.master.size)
            win_size[0] = int(win_size[0] * .8)
            if win_size != pred_size: # size changed
                # resize the image in the available space
                img = img.resize(tuple(win_size))
                # reset the image to update the map label
                self.mapImg = ImageTk.PhotoImage(img)
                self.mapLabel['image'] = self.mapImg
            pred_size = [*win_size]
            sleep(.5)

    def show_path(self, path: list):
        pass