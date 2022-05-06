'''
CT Final Project

author: charlotte komrosky-licata, eric jones

'''


import tkinter
from tkinter import *
from PIL import Image, ImageTk

import utilities as a


class AllTkinterWidgets:
      def __init__(self, master):
        frame = Frame(master, width=600, height=200)
        frame.place(x=0, y=0)

        # -------------------- Menu Creation ------------------------
        self.mbar = Frame(frame, relief = 'raised', width=600, bd = 2)
        self.mbar.pack(expand = 0, fill = X, side = TOP)

        # ------------------- Create image adjustment menu -----------
        self.fgbutton = Menubutton(self.mbar, text = 'Display Data')
        self.fgbutton.pack(side = LEFT)
        self.fgmenu = Menu(self.fgbutton, tearoff=0)
        self.fgbutton['menu'] = self.fgmenu

        # Populate image adjustment menu
        self.fgmenu.add('command', label = 'Release Dates', command = self.dates)
        self.fgmenu.add('command', label = 'TV Shows vs Movies', command = self.mediatype)
        self.fgmenu.add('command', label = 'Countries Released', command = self.countries)
        self.fgmenu.add('command', label = 'Popular Ratings', command = self.ratings)
        
       # -------------------- Entry box frame ---------------------
        self.t = StringVar()
        self.ef = Frame(frame, bd=2, relief='groove')
        self.ef.pack(expand=0, fill=BOTH, pady=5, side = BOTTOM)

        #--------------------- Listbox frame ------------------------
        self.lf = Frame(frame, bd=2, relief='groove')
        self.lb = Label(self.lf, text='Log:')
        self.bt1 = Button(self.lf, text = 'Clear', command = self.clear)
        self.listbox = Listbox(self.lf, height=4)
        self.sbl = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.sbl.set)
        self.lb.pack(side=LEFT, padx=20)
        self.bt1.pack(side = BOTTOM)
        self.sbl.pack(side=RIGHT, fill=Y)
        self.listbox.pack(padx=5, fill = X)
        self.lf.pack(expand=0, fill=X, pady=5, before = self.ef, side = BOTTOM)

      # -------------------- Function defs ------------------------

      def clear(self):
          self.listbox.delete(0, END)
          self.lblImage.config(image='')

          
      def dates(self):
          a.getCountofDates()
          try:             
             self.image1 = Image.open('datesplot.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=0)
             self.listbox.insert(END, 'Loaded datesplot.png')
          except:
             self.listbox.insert(END, 'Error getting datesplot.png' )
             
      def mediatype(self):
          a.getCountMoviesTV()
          try:             
             self.image1 = Image.open('moviestvcount.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=0)
             self.listbox.insert(END, 'Loaded moviestvcount.png')
          except:
             self.listbox.insert(END, 'Error getting moviestvcount.png' )

      def countries(self):
          a.getCountriesCount()
          try:             
             self.image1 = Image.open('countrieschart.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=0)
             self.listbox.insert(END, 'Loaded countrieschart.png')
          except:
             self.listbox.insert(END, 'Error getting countrieschart.png' )
             
      def ratings(self):
          a.getRatingsCount()
          try:             
             self.image1 = Image.open('ratingschart.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=0)
             self.listbox.insert(END, 'Loaded ratingschart.png')
          except:
             self.listbox.insert(END, 'Error getting ratingschart.png' )


# main--tk object, tk class and display all functions
root = Tk()
root.geometry('1500x1200')
root.configure(bg='black')
all = AllTkinterWidgets(root)
root.title('CT Final Project')
root.pack_propagate(0)
root.mainloop()







