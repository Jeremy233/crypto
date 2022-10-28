from tkinter import *
from tkinter.messagebox import *
import pymongo
from pymongo import MongoClient
import time


client = pymongo.MongoClient("mongodb+srv://cassiehe221:1234@cluster0.jt2g2.mongodb.net/?retryWrites=true&w=majority")
db = client['Encryption']
message_collection = db['Messages']

# message_collection.insert_one({'message': 'jz message 3', 'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})
# message_collection.insert_one({'message': 'jz message 4', 'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})


class OthersMessagePage(object):
	global message_collection

	def __init__(self, master=None):
		self.root = master
		self.root.geometry("300x200")
		self.others_user_name = StringVar()
		self.current_page_idx = 0


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


	def goBack(self):
		self.page.destroy()
		MainPage(self.root)

	def getMessagesFromOthers(self):
		others_name = self.others_user_name.get()
		messages = list(message_collection.find({'user_name': others_name}))
		for item in messages:
			print(item['time'])
		
		if messages != None:
			others_message_window = Toplevel(self.root)
			others_message_window.geometry('500x400')
			page_numbers = int(len(messages)/3)
			print(page_numbers)
			# current_message = [x * current_page_idx for x in [0,1,2]]
			current_message = [0, 1, 2]

			def forward():
				if self.current_page_idx < page_numbers:
					self.current_page_idx += 1
					backward_button['state'] = 'enable'
				else:
					forward_button['state'] = 'disabled'

			def backward():
				if self.current_page_idx != 0:
					self.current_page_idx -= 1
				else:
					backward_button['state'] = 'disabled'


			Label(others_message_window, text=others_name+'的留言').grid(row=0, column=1)
			backward_button = Button(others_message_window, text='<<', command=backward, state=DISABLED).grid(row=2)
			if page_numbers != 0:
				forward_button = Button(others_message_window, text='>>', command=forward).grid(row=2, column=4)
			else:
				forward_button = Button(others_message_window, text='>>', state=DISABLED).grid(row=2, column=4)

			try:
				Label(others_message_window, text=messages[current_message[0]]['time'], bg='blue', width=40, height=5).grid(row=1, column=1)
				Button(others_message_window, text='查看').grid(row=1, column=2, stick=E)
			except IndexError:
				Label(others_message_window, text='没有其他留言了', bg='green', width=40, height=5).grid(row=1, column=1)
				Button(others_message_window, text='查看', state=DISABLED).grid(row=1, column=2, stick=E)
			try:
				Label(others_message_window, text=messages[current_message[1]]['time'], bg='blue', width=40, height=5).grid(row=2, column=1)
				Button(others_message_window, text='查看').grid(row=2, column=2, stick=E)
			except IndexError:
				Label(others_message_window, text='没有其他留言了', bg='green', width=40, height=5).grid(row=2, column=1)
				Button(others_message_window, text='查看', state=DISABLED).grid(row=2, column=2, stick=E)
			try:
				Label(others_message_window, text=messages[current_message[2]]['time'], bg='blue', width=40, height=5).grid(row=3, column=1)
				Button(others_message_window, text='查看').grid(row=3, column=2, stick=E)
			except:
				Label(others_message_window, text='没有其他留言了', bg='green', width=40, height=5).grid(row=3, column=1)
				Button(others_message_window, text='查看', state=DISABLED).grid(row=3, column=2, stick=E)



		else:
			showinfo(title='错误', message='该用户没有任何消息')


		pass


root = Tk()
root.title('Secrets')
OthersMessagePage(root)
root.mainloop()