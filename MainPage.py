import collections
from tkinter import *
from tkinter.messagebox import *
# import pymongo
# from pymongo import MongoClient

class MainPage(object):
    global collection

    def __init__(self, master=None):
        self.root = master
        self.root.geometry("450x450")
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)

        Label(self.page, text='').grid(row=1, stick=W, pady=10) # leave notes
        Label(self.page, text='').grid(row=1, stick=W, pady=10) # check notes
        Label(self.page, text='').grid(row=1, stick=W, pady=10) # change password
        Label(self.page, text='').grid(row=1, stick=W, pady=10) # delete user
        Label(self.page, text='').grid(row=1, stick=W, pady=10) # log out 