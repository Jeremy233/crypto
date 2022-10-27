from tkinter import *
from tkinter.messagebox import *
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://cassiehe221:1234@cluster0.jt2g2.mongodb.net/?retryWrites=true&w=majority")
db = client['Encryption']
message_collection = db['Messages']

class OthersMessagePage(object):
	global message_collection
	global user_collection

	def __init__(self, master=None):
		self.root = master
		self.root.geometry("300x200")
		self.others_user_name = StringVar()


		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()

		Button(self.page, text='返回', command=self.goBack).grid(row=0, stick=W)
		Label(self.page).grid(row=1, stick=W)
		Label(self.page, text='你想查看谁的留言？').grid(row=2, column=1, pady=10)

		Label(self.page, text='输入他的用户名').grid(row=3, stick=W)
		Entry(self.page, textvariable=self.others_user_name).grid(row=3, column=1, stick=E, pady=10)

		Button(self.page, text='查看', command=self.getMessagesFromOthers).grid(row=4, column=1)

	def searchOthers(self):
		pass

	def goBack(self):
		pass

	def getMessagesFromOthers(self):
		others_name = self.others_user_name.get()
		if user_collection.find_one({'user_name': nn}) != None:

		else:
			


		pass

root = Tk()
OthersMessagePage(root)
root.mainloop()