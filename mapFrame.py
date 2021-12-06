"""
TODO
Frame principale avec l'image de la carte, ou sera ajouté le chemin à parcourir
"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import sleep
from threading import Thread # Permet de faire tourner des fonctions en meme temps (async)

matrix = [ # matrice des distances
    [0,376,555,377,475,632,536,594,424,639,334,263,157,300,558,630,230,428,593,716,822,402],
    [376,0,185,245,646,803,347,466,586,800,649,652,307,462,719,945,221,662,685,693,651,187],
    [555,185,0,300,693,850,532,651,770,985,828,788,486,647,903,1124,406,847,870,877,830,371],
    [377,245,300,0,404,561,588,705,680,896,651,192,255,556,814,947,291,758,849,931,883,425],
    [457,646,693,404,0,207,986,1052,775,1000,506,214,422,758,798,801,691,688,962,1121,1280,824],
    [632,803,850,561,207,0,1144,1210,933,1148,663,372,580,916,956,785,849,846,1120,1279,1441,982],
    [536,347,532,588,986,1144,0,113,385,600,639,781,493,335,518,865,325,517,385,340,298,142],
    [594,466,651,705,1052,1210,113,0,349,564,617,834,614,302,483,830,446,482,279,234,242,263],
    [424,586,770,680,775,933,385,349,0,219,315,563,572,132,144,491,392,178,197,356,591,412],
    [639,800,985,896,1000,1148,600,564,219,0,501,789,788,348,206,525,608,329,318,509,760,627],
    [334,649,828,651,506,663,639,617,315,501,0,294,482,314,299,331,434,189,505,664,860,594],
    [263,652,788,192,214,372,781,834,563,789,294,0,278,555,595,598,516,484,759,918,1077,656],
    [157,307,486,255,422,580,493,614,572,788,482,278,0,448,705,778,168,575,740,779,791,333],
    [300,462,647,556,758,916,335,302,132,348,314,555,448,0,266,588,268,210,302,430,544,290],
    [558,719,903,814,798,956,518,483,144,206,299,595,705,266,0,351,526,126,352,503,725,545],
    [630,945,1124,947,801,785,865,830,491,525,331,598,778,588,351,0,731,387,700,851,1072,866],
    [230,221,406,291,691,849,325,446,392,608,434,516,168,268,526,731,0,471,562,616,622,164],
    [428,662,847,758,688,846,517,482,178,329,189,484,575,210,126,387,471,0,375,534,730,494],
    [593,685,870,849,962,1120,385,279,197,318,505,759,740,302,352,700,562,375,0,216,466,485],
    [716,693,877,931,1121,1279,340,234,356,509,664,918,779,430,503,851,616,534,216,0,421,489],
    [822,651,830,883,1280,1441,298,242,591,760,860,1077,791,544,725,1072,622,730,466,421,0,439],
    [402,187,371,425,824,982,142,263,412,627,594,656,333,290,545,866,164,494,485,489,439,0]
]

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
                    if not self._selection_widgets[i][1]: # there is no active remove thread for this widget
                        remove_thread = Thread(target=self.__remove_name_widget, args=(i,))
                        remove_thread.setDaemon(True) # to prevent error when closing main program
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
            sleep(.1)

    def show_path(self, path: list):
        pass