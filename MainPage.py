from tkinter import *
from tkinter.messagebox import *
# import pymongo
# from pymongo import MongoClient

class MainPage(object):

    def __init__(self, master=None):
        self.root = master
        self.root.geometry("250x300")
        self.createPage()

    def createPage(self):
        # self.leaveNotesPage = LeaveNotesPageFrame(self.root)
        # self.checkNotesPage = CheckNotesPageFrame(self.root)
        # self.changePasswordPage = ChangePasswordPageFrame(self.root)
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)

        Button(self.page,command=self.enterLeaveMsgPage, text='查看你的当前留言',height= 1, width=15, justify=CENTER).grid(row=1, stick=W, pady=10) # leave notes
        Button(self.page,command=self.enterCheckMsgPage, text='查看他人留言', height= 1, width=15, justify=CENTER).grid(row=2, stick=W, pady=10) # check notes
        Button(self.page,command=self.enterChangePasswordPage, text='修改密码', height= 1, width=15, justify=CENTER).grid(row=3, stick=W, pady=10) # change password
        Button(self.page,command=self.enterDeleteUserPage, text='删除本用户', height= 1, width=15, justify=CENTER).grid(row=4, stick=W, pady=10) # delete user
        Button(self.page,command=self.enterLogOutPage, text='登出', height= 1, width=15, justify=CENTER).grid(row=5, stick=W, pady=10) # log out 

    def enterLeaveMsgPage(self):
        LeaveMsgPage(self.root)

    def enterCheckMsgPage(self):
        CheckMsgPage(self.root)
        
    def enterChangePasswordPage(self):
        ChangePasswordPage(self.root)

    def enterDeleteUserPage(self):
        DeleteUserPage(self.root)

    def enterLogOutPage(self):
        LogOutPage(self.root)

if __name__ == "__main__":
    root = Tk()
    root.title('主页面') # name the window as main page
    MainPage(root)
    root.mainloop()