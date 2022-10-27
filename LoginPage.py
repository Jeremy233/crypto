from tkinter import *
from tkinter.messagebox import *
# from MainPage import *
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://cassiehe221:1234@cluster0.jt2g2.mongodb.net/?retryWrites=true&w=majority")
db = client['Encryption']
user_collection = db['Users']


class LoginPage(object):
	global user_collection

	def __init__(self, master=None): #master=None?
		self.root = master
		self.root.geometry("300x300")
		self.user_name = StringVar()
		self.user_password = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W) # 不贴上边

		Label(self.page, text='用户名:').grid(row=1, stick=W, pady=10)
		Entry(self.page, textvariable=self.user_name).grid(row=1, column=1, stick=E)
		Label(self.page, text='登入密码:').grid(row=2, stick=W)
		Entry(self.page, textvariable=self.user_password, show='*').grid(row=2, column=1, stick=E)
		Button(self.page, text='登入', command=self.loginCheck).grid(row=3, stick=W, pady=10)
		Button(self.page, text='创建账号', command=self.createAccount).grid(row=3, column=1, stick=W)

	def loginCheck(self):
		name = self.user_name.get()
		pw = self.user_password.get()

		found_user = user_collection.find_one({'user_name': name})

		if found_user != None:
			if name == found_user['user_name'] and pw == found_user['user_password']:
				self.page.destroy()
				# MainPage(self.root)
			else:
				showinfo(title='错误', message='账号或密码错误')
		else:
			showinfo(title='错误', message='用户不存在')

	def createAccount(self):
		def subCreate():
			np = new_pwd.get()
			nn = new_name.get()
			if user_collection.find_one({'user_name': nn}) != None:
				showinfo(title='错误', message='用户已存在')
			else:
				showinfo(title='成功', message='创建成功')
				user_collection.insert_one({'user_name': nn, 'user_password': np})
		window_sign_up = Toplevel(self.root)
		window_sign_up.geometry('300x200')


		new_name = StringVar()
		Label(window_sign_up).grid(row=0, stick=W, padx=10, pady=10)
		Label(window_sign_up, text='新用户名：').grid(row=1, stick=W, pady=10, padx=10)
		entry_new_name = Entry(window_sign_up, textvariable=new_name)
		entry_new_name.grid(row=1, column=1, stick=E)

		new_pwd = StringVar()
		Label(window_sign_up, text='密码：').grid(row=2, padx=10, stick=W)
		entry_usr_pwd = Entry(window_sign_up, textvariable=new_pwd, show='*')
		entry_usr_pwd.grid(row=2, column=1, stick=E)

		Button(window_sign_up, text='注册', command=subCreate).grid(row=3, column=1, stick=W)


root = Tk()
root.title('Secrets')
LoginPage(root)
root.mainloop()