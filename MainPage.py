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

        Label(self.page, text='查看你的当前留言').grid(row=1, stick=W, pady=10) # leave notes
        Label(self.page, text='查看他人留言').grid(row=2, stick=W, pady=10) # check notes
        Label(self.page, text='修改密码').grid(row=3, stick=W, pady=10) # change password
        Label(self.page, text='删除本用户').grid(row=4, stick=W, pady=10) # delete user
        Label(self.page, text='登出').grid(row=5, stick=W, pady=10) # log out 