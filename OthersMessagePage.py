from tkinter import *
from tkinter.messagebox import *
import pymongo
from pymongo import MongoClient
import time


client = pymongo.MongoClient("mongodb+srv://cassiehe221:1234@cluster0.jt2g2.mongodb.net/?retryWrites=true&w=majority")
db = client['Encryption']
message_collection = db['Messages']



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

		
		if len(messages) != 0:
			others_message_window = Toplevel(self.root)
			others_message_window.geometry('500x400')
			page_numbers = int(len(messages)/3)

			def change_text_button(): # message is a list
				nonlocal messages, m1, m1_button, m2, m2_button, m3, m3_button
				msg0 = messages[self.current_page_idx * 3]
				m1['text'] = msg0['time']
				m1_button['state'] = 'active'
				
				try:
					msg1 = messages[self.current_page_idx * 3 + 1]
					m2['text'] = ['time']
					m2_button['state'] = 'active'
				except IndexError:
					m2['text'] = '没有其他留言了'
					m2_button['state'] = 'disabled'
				try:
					msg2 = messages[self.current_page_idx * 3 + 2]
					m3['text'] = msg2['time']
					m3_button['state'] = 'active'
				except IndexError:
					m3['text'] = '没有其他留言了'
					m3_button['state'] = 'disabled'
				

			def forward():
				if self.current_page_idx < page_numbers:
					self.current_page_idx += 1
					if self.current_page_idx == page_numbers:
						nonlocal forward_button
						forward_button['state'] = 'disabled'
					nonlocal m1, m2, m3, backward_button
					backward_button['state'] = 'active'
					change_text_button()
					


			def backward():
				if self.current_page_idx != 0:
					self.current_page_idx -= 1
					if self.current_page_idx == 0:
						nonlocal backward_button
						backward_button['state'] = 'disabled'
					nonlocal m1, m2, m3, forward_button
					forward_button['state'] = 'active'
					change_text_button()

			def showKeyWindow(msg_idx):
				needKeyWindow = Toplevel(others_message_window)
				needKeyWindow.geometry('200x150')
				needKeyWindowFrame = Frame(needKeyWindow)
				needKeyWindowFrame.pack()
				key = StringVar()
				Label(needKeyWindowFrame, text='输入本条消息的密钥', justify=CENTER).grid(row=0, stick=W, padx=15, pady=15)
				Entry(needKeyWindowFrame, textvariable=key, justify=CENTER, show='*').grid(row=1, stick=W, padx=15, pady=15)
				Button(needKeyWindowFrame, text='确定', justify=CENTER, command=lambda: get_msg(msg_idx)).grid(row=2, stick=W, padx=15, pady=15)

				def dec(message):
					nonlocal key
					localKey = str(key)
					key_length = len(localKey)
					result_list = []
					for counter, char in enumerate(message):
						loc = counter % key_length
						char_ascii_decoded = chr(ord(char) - ord(localKey[loc]))
						result_list.append(char_ascii_decoded)
					result = ''.join(result_list)
					return result


				def get_msg(msg_idx):
					nonlocal messages, needKeyWindowFrame
					needKeyWindowFrame.destroy()
					msg = messages[msg_idx]
					Label(needKeyWindow, text=dec(msg['message']), justify=CENTER).grid(row=0)
				

			Label(others_message_window, text=others_name+'的留言').grid(row=0, column=1)
			backward_button = Button(others_message_window, text='<<', command=backward, state=DISABLED)
			backward_button.grid(row=2)
			forward_button = Button(others_message_window, text='>>', command=forward)
			forward_button.grid(row=2, column=4)


			msg0 = messages[0]
			m1 = Label(others_message_window, text=msg0['time'], bg='white', width=40, height=5)
			m1.grid(row=1, column=1)
			m1_button = Button(others_message_window, text='查看', command=lambda: showKeyWindow(0))
			m1_button.grid(row=1, column=2, stick=E)

			try:
				msg1 = messages[1]
				m2 = Label(others_message_window, text=msg1['time'], bg='white', width=40, height=5)
				m2.grid(row=2, column=1)
				m2_button = Button(others_message_window, text='查看', command=lambda: showKeyWindow(1))
				m2_button.grid(row=2, column=2, stick=E)
			except IndexError:
				m2 = Label(others_message_window, text='没有其他留言了', bg='white', width=40, height=5)
				m2.grid(row=2, column=1)
				m2_button = Button(others_message_window, text='查看', state=DISABLED, command=lambda: showKeyWindow(1))
				m2_button.grid(row=2, column=2, stick=E)
			try:
				msg2 = messages[2]
				m3 = Label(others_message_window, text=msg2['time'], bg='white', width=40, height=5)
				m3.grid(row=3, column=1)
				m3_button = Button(others_message_window, text='查看', command=lambda: showKeyWindow(2))
				m3_button.grid(row=3, column=2, stick=E)
			except:
				m3 = Label(others_message_window, text='没有其他留言了', bg='white', width=40, height=5)
				m3.grid(row=3, column=1)
				m3_button = Button(others_message_window, text='查看', state=DISABLED, command=lambda: showKeyWindow(2))
				m3_button.grid(row=3, column=2, stick=E)



		else:
			showinfo(title='错误', message='该用户没有任何消息')



root = Tk()
root.title('Secrets')
OthersMessagePage(root)
root.mainloop()