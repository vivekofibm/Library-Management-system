from tkinter import *
import pymysql
# root = Tk()
#
# db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
# cursor = db.cursor()
#
# find_user = ("SELECT * FROM test.login")
#
# cursor.execute(find_user)
#
# result = cursor.fetchall()
#
#
# height = 5
# width = 5
# for row in result: #Rows
#
#     print(row)
#     for i in range(height):
#         for j in range(width): #Columns
#             b = Entry(root, text="")
#             b.grid(row=i, column=j)
#
#
# db.commit()
# db.close()
# mainloop()

#################################################3


# from tkinter import *
#
# rows = []
# for i in range(5):
#     cols = []
#     for j in range(4):
#         e = Entry(relief=RIDGE)
#         e.grid(row=i, column=j, sticky=NSEW)
#         e.insert(END, '%d.%d' % (i, j))
#         cols.append(e)
#     rows.append(cols)
#
# def onPress():
#     for row in rows:
#         for col in row:
#             print (col.get()),
#         print
#
# Button(text='Fetch', command=onPress).grid()
# mainloop()

####################################################3

# from tkinter import *
#
# rows = []
# for i in range(5):
#     cols = []
#     for j in range(4):
#         e = Entry(relief=RIDGE)
#         e.grid(row=i, column=j, sticky=NSEW)
#         e.insert(END, '%d.%d' % (i, j))
#         cols.append(e)
#     rows.append(cols)
#
# def onPress():
#     db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
#     cursor = db.cursor()
#
#     find_user = ("SELECT * FROM test.login")
#
#     cursor.execute(find_user)
#
#     result = cursor.fetchall()
#     for row in result:
#         for col in row:
#             print (col.get()),
#         print
#
# Button(text='Fetch', command=onPress).grid()
# mainloop()
#
#
# #######################################################################
#
# from tkinter import *
#
# def speak():
#     print("kaise ho")
# #create windows object
# windows=Tk()
# windows.title('Book menu')
#
# #here create lebels
#
# l1=Label(windows,text="title")
# l1.grid(row=0,column=0)
#
# l2=Label(windows,text="Author")
# l2.grid(row=0,column=3)
#
# l1=Label(windows,text="Year")
# l1.grid(row=1,column=0)
#
# l2=Label(windows,text="isbn")
# l2.grid(row=1,column=3)
#
# #here is the textbox entry code
# title_text=StringVar()
# e1=Entry(windows,textvariable=title_text)
# e1.grid(row=0,column=1)
#
# Author_text=StringVar()
# e2=Entry(windows,textvariable=Author_text)
# e2.grid(row=0,column=4)
#
# Year_text=StringVar()
# e3=Entry(windows,textvariable=Year_text)
# e3.grid(row=1,column=1)
#
# isbn_text=StringVar()
# e4=Entry(windows,textvariable=isbn_text)
# e4.grid(row=1,column=4)
#
# #here your listbox code
# list1=Listbox(windows,height=6,width=35)
# list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#
# #here attach Scrollbar
# sb1=Scrollbar(windows)
# sb1.grid(row=2,column=2,rowspan=6)
#
# #cofigur listbox
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview())
# #here your button
# Button(windows,text="view all",width =14,command=speak).grid(row=2,column=4)
# Button(windows,text="Search Entry",width =14,command=speak).grid(row=3,column=4)
# Button(windows,text="Add Entry",width =14,command=speak).grid(row=4,column=4)
# Button(windows,text="Update Selected ",width =14,command=speak).grid(row=5,column=4)
# Button(windows,text="Delete Selected",width =14,command=speak).grid(row=6,column=4)
#
#
#
# windows.mainloop()

###########################################################################

# class records():
#     # class created to see records that have been previously inputted#
#     def __init__(self, master):
#
#
#         self.master = master
#         self.master.geometry('250x200+100+200')
#         self.master.title('Records')
#         self.connection = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
#         self.cur = self.connection.cursor()
#         self.dateLabel = Label(self.master, text="Date", width=10)
#         self.dateLabel.grid(row=0, column=0)
#         self.BMILabel = Label(self.master, text="BMI", width=10)
#         self.BMILabel.grid(row=0, column=1)
#         self.stateLabel = Label(self.master, text="Status", width=10)
#         self.stateLabel.grid(row=0, column=2)
#         self.showallrecords()
#
#
#     def showallrecords(self):
#         data = self.readfromdatabase()
#         for index, dat in enumerate(data):
#             Label(self.master, text=dat[0]).grid(row=index + 1, column=0)
#             Label(self.master, text=dat[1]).grid(row=index + 1, column=1)
#             Label(self.master, text=dat[2]).grid(row=index + 1, column=2)
#
#     def readfromdatabase(self):
#         self.cur.execute("SELECT * FROM test.login")
#         return self.cur.fetchall()

######################################################################




def showallrecords():

    data = readfromdatabase()
    for index, dat in enumerate(data):
        Label(master, text=dat[0]).grid(row=index + 1, column=0)
        Label(master, text=dat[1]).grid(row=index + 1, column=1)
        # Label(master, text=dat[2]).grid(row=index + 1, column=2)


def readfromdatabase():
    cur.execute("SELECT * FROM test.login")
    return cur.fetchall()


master = Tk()
master.geometry('250x250')
master.title('Records')
connection = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
cur = connection.cursor()
usernameLabel = Label(master, text="Username", width=10)
usernameLabel.grid(row=0, column=0)
BMILabel = Label(master, text="Passwords", width=10)
BMILabel.grid(row=0, column=1)
roleLabel = Label(master, text="Role", width=10)
roleLabel.grid(row=0, column=2)
btn = Button(master,text ='fetch',command=showallrecords).place(x=120,y=200)
master = mainloop()

#################################################################

