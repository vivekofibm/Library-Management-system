# from tkinter import *
# import pymysql
#
#
# class main:
#     def __init__(self, master):
#         # Window
#         self.master = master
#         # Some Usefull variables
#         self.e1 = StringVar()
#         self.e2 = StringVar()
#
#         # Create Widgets
#         self.widgets()
#
#     def signupp(self):
#
#
#
#         db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
#         cursor = db.cursor()
#
#     # find_user = ("INSERT  INTO test.login(username,passwords) VALUES('ruchika',123456);")
#
#         insert = 'INSERT INTO test.login(username,passwords) VALUES(?,?)'
#         cursor.execute(insert, [(self.username.get()), (self.password.get())])
#
#     # find_user = ("UPDATE test.login set passwords = 123456789 where username = 'ruchika';")
#
#     # cursor.execute(find_user)
#
#         db.commit()
#         db.close()
#
#
#
#
#     def log(self):
#         self.username.set('')
#         self.password.set('')
#         # self.crf.pack_forget()
#         self.head['text'] = 'LOGIN'
#         self.logf.pack()
#
#
#
#     def widgets(self):
#         # R = Tk()
#         # R.geometry('1280x720')
#         # R.title('Sign up')
#
#         self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
#         self.head.pack()
#         self.logf = Frame(self.master, padx=10, pady=10)
#
#         Entry(self.logf, width=20, font=("bold", 15),textvariable=self.username, highlightthickness=2, relief=SUNKEN).place(x=920, y=120)
#         Entry(self.logf, width=20, font=("bold", 15),textvariable=self.password, highlightthickness=2, relief=SUNKEN).place(x=920, y=165)
#         Button(self.logf, text="Sign Up", width=25, height=2, fg="Black", font="5", relief=RAISED, overrelief=RIDGE,command=self.signupp()).place(x=858, y=600)
#
#         self.logf.pack()
#
#         # R.mainloop()
#
#
#
# if __name__ == '__main__':
#     # Create Object
#     # and setup window
#     root = Tk()
#     root.title('Login Form')
#     root.geometry('1280x720')
#     main(root)
#     root.mainloop()
#



# Python Tkinter and Sqlite3 Login Form
# Made By Namah Jain Form Youtube Channel All About Code
# Please Subscribe To Our Youtube Channel.
# https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber

# imports




from tkinter import *
import pymysql
from tkinter import messagebox as ms
# make database and users (if not exists already) table at programme start up


# main Class
class main:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection

        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
        cursor = db.cursor()
        # with sqlite3.connect('quit.db') as db:
        #     c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        cursor.execute(find_user, [(self.username.get()), (self.password.get())])
        result = cursor.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
        cursor = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        cursor.execute(find_user, [(self.username.get())])
        if cursor.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        cursor.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Login Form')
    # root.geometry('400x350+300+300')
    main(root)
    root.mainloop()





