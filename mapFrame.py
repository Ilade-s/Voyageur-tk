"""
TODO
Frame principale avec l'image de la carte, ou sera ajouté le chemin à parcourir
"""
from random import randrange
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw, ImageFont
from time import sleep
from threading import Thread # Permet de faire tourner des fonctions en meme temps (async)
from prim_lib import PRIM # class to interact with the prim algorithm

PATH_TO_MAP = 'assets/map.png'
PATH_TO_BTN = 'assets/search.png'

POS_VILLES = ( # format (x, y), same order as villes list
    (602, 638), (340, 730),(270, 875),(481, 864),(765, 894),(905, 850),(260, 484),(259, 390),(548, 305),
    (595, 95),(737, 473),(730, 719),(549, 725),(514, 416),(667, 255),(935, 334),(470, 627),
    (670, 363),(385, 235),(258, 213),(49, 355),(342, 579)
)

class MapFrame(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.choice = None
        self.path_showed = False
        self.prim = PRIM()
        self.__path_colors = {0:"#000000"}
        self._selection_widgets = {}
        # =======================================
        # IMAGES
        # map image
        self.mapImg = Image.open(PATH_TO_MAP)
        self.mapImgTk = ImageTk.PhotoImage(self.mapImg)
        # search icon for button
        img_btn = Image.open(PATH_TO_BTN)
        self.btnImg = ImageTk.PhotoImage(img_btn)
        # =======================================
        self.__create_widgets()
        self.pack()
    
    def __create_widgets(self):
        def scale_changed():
            if self.path_showed:
                self.__reset_image()
                self.show_path()

        self.mapLabel = Label(self, text='map', image=self.mapImgTk)
        self.mapLabel.pack()
        self.primBtn = ttk.Button(self, text='Search path...', command=self.show_path, 
            image=self.btnImg, state=DISABLED)
        self.primBtn.place(relx=.05, rely=.6)
        self.scale_voyageur = ttk.Spinbox(self, width=5, background=self["background"], 
                                from_=1, to=len(POS_VILLES), increment=1.0, font=20, command=scale_changed)
        self.scale_voyageur.set(1)
        self.scale_voyageur.place(relx=.05, rely=.75)

    def __reset_image(self):
        self.mapImg = Image.open(PATH_TO_MAP)
        win_size = self.master.size
        img = self.mapImg.resize(tuple(win_size))
        self.mapImgTk = ImageTk.PhotoImage(img)
        self.mapLabel['image'] = self.mapImgTk
        self.path_showed = False
    
    def show_selection(self, x: int, y: int):
        def on_click(event):
            name = event.widget['text'].split('\n')[0]
            index_ville = self.master.villes.index(name)
            if self.choice == index_ville:
                self.choice = None
                event.widget['text'] = name
                event.widget['background'] = '#A8B8FF'
                self.primBtn['state'] = DISABLED
            else:
                self.choice = index_ville
                event.widget['text'] += '\n(départ)'
                event.widget['background'] = '#FF5858'
                self.primBtn['state'] = NORMAL
            # reset the map image
            self.__reset_image()
            event.widget.update()

        width, height = self.master.size
        x_factor = 1000 / width
        y_factor = 1000 / height
        for (xv, yv), i in zip(POS_VILLES, range(len(POS_VILLES))):
            name = self.master.villes[i]
            if abs(xv / x_factor - x) < 50 / x_factor and abs(yv / y_factor - y) < 50 / x_factor: # close to the city 
                if not i in self._selection_widgets.keys():
                    w = Label(self, text=name, background='#A8B8FF', font=('Arial', int(10 + 6 / x_factor)), name=name)
                    w.bind('<1>', on_click)
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
        name = self._selection_widgets[i][0]['text'].split('\n')[0]
        index_ville = self.master.villes.index(name)
        while self.choice == index_ville:
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
            if win_size != pred_size: # size changed
                # resize the image in the available space
                img = self.mapImg.resize(tuple(win_size))
                # reset the image to update the map label
                self.mapImgTk = ImageTk.PhotoImage(img)
                self.mapLabel['image'] = self.mapImgTk
            pred_size = [*win_size]
            sleep(.1)

    def show_path(self):
        # execute the algorithm to find the path
        self.prim.execute(self.choice, int(self.scale_voyageur.get()))
        self.prim.upgrade()
        paths = self.prim.npaths
        # add the order to the cities
        draw = ImageDraw.Draw(self.mapImg) # drawing object
        # add the lines between each city and the order numbers
        for i, path in paths.items():
            if i in self.__path_colors.keys():
                color = self.__path_colors[i]
            else:
                color = '#{}{}{}'.format(*[
                    hex(randrange(0, 200))[2:].zfill(2)
                    for _ in range(3)])
                self.__path_colors[i] = color

            for D, A in zip(path, path[1:]):
                draw.line((POS_VILLES[D], POS_VILLES[A]), color, 5)
            for n, j in zip(path[:-1], range(len(path))):
                fnt = ImageFont.truetype("assets/arial.ttf", 30)
                draw.rectangle((POS_VILLES[n], tuple([pos + 30 for pos in POS_VILLES[n]])), fill='white')
                draw.text(POS_VILLES[n], f'{j}', fill=color, font=fnt)
        # update the map image
        win_size = self.master.size
        img = self.mapImg.resize(tuple(win_size))
        self.mapImgTk = ImageTk.PhotoImage(img)
        self.mapLabel['image'] = self.mapImgTk
        self.primBtn['state'] = DISABLED
        self.path_showed = True


