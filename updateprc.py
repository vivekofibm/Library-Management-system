import pymysql
from tkinter import *
import ttk
from tkinter import messagebox

# def update():
#     update=Tk()
#     update.geometry('500x500')
#     idbook_label = Label(update, text="idbook")
#     idbook_label.place(x=10,y=10)
#     idbook_entry_value = StringVar(update, value="")
#     idbook_entry = ttk.Entry(update, textvariable=idbook_entry_value)
#     idbook_entry.grid(row=0, column=1, padx=10, pady=10)
#     search_button = ttk.Button(update, text="Search")
#     search_button.grid(row=1, column=2, padx=10, pady=10)
#
#     Title_label = Label(update, text="Title")
#     Title_label.place(x=10,y=50)
#     Title_entry_value = StringVar(update, value="")
#     Title_entry = ttk.Entry(update,textvariable=Title_entry_value)
#     Title_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)
#
#
#     Author_label = Label(update, text="Author")
#     Author_label.place(x=10,y=90)
#     Author_entry_value = StringVar(update, value="")
#     Author_entry = ttk.Entry(update, textvariable=Author_entry_value)
#     Author_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
#
#
#     Year_label = Label(update, text="Year")
#     Year_label.place(x=10,y=130)
#     Year_entry = ttk.Entry(update, textvariable=Title_entry_value)
#     Year_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)
#
#
#     Subject_label = Label(update, text="Subject")
#     Subject_label.place(x=10,y=170)
#     Subject_entry_value = StringVar(update, value="")
#     Subject_entry = ttk.Entry(update,textvariable=Subject_entry_value)
#     Subject_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)
#
#
#     AvailableCopies_label = Label(update, text="Available")
#     AvailableCopies_label.place(x=10,y=210)
#     AvailableCopies_entry = ttk.Entry(update,textvariable=Title_entry_value)
#     AvailableCopies_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)
#
#
#     TotalCopies_label = Label(update, text="TotalCopies")
#     TotalCopies_label.place(x=10,y=250)
#     TotalCopies_entry = ttk.Entry(update,textvariable=Title_entry_value)
#     TotalCopies_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)
#
#
#     submit_button = ttk.Button(update,text="Submit")
#
#     submit_button.grid(row=7, column=0,padx=10, pady=10, sticky=W)
#
#     update_button = ttk.Button(update, text="Update")
#
#     update_button.grid(row=7, column=1,padx=10, pady=10)
#
#     btn = Button(update, text='fetch', command=update).place(x=400, y=350)
#     update.mainloop()

def search():
    try:
        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
        cursor = db.cursor()
        find_user = "select * from test.book_tbl where BookId = '%s'" %idbook.get()
        # find_user = "select * from test.book_tbl where BookId = 1"
        cursor.execute(find_user)
        result=cursor.fetchone()
        Title.set(result[1])
        Author.set(result[2])
        Year.set(result[3])
        Subject.set(result[4])
        AvailableCopies.set(result[5])
        TotalCopies.set(result[6])
        e1.configure(state = 'disabled')
        db.commit()
        db.close()
    except:
        messagebox.showinfo('no data')
        clear()


def updatebook():
    try:
        ubid = e1.get()
        ubtitle=e2.get()
        ubauthor=e3.get()
        ubyear=e4.get()
        ubsubject=e5.get()
        ubavailable=e6.get()
        ubtot=e7.get()

        print(ubid)
        print(ubtitle)
        print(ubauthor)
        print(ubyear)
        print(ubsubject)
        print(ubavailable)
        print(ubtot)

        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
        cursor = db.cursor()


        find_user = "UPDATE test.book_tbl SET Title = '"+ubtitle+"', Author = '"+ubauthor+"', Year = "+ubyear+", Subject = '"+ubsubject+"', AvailableCopies = "+ubavailable+", TotalCopies = "+ubtot+" WHERE BookId = "+ubid+";"


        # find_user = "UPDATE sample.book set Title = '%s', Author = '%s', Year = '%s', Subject = '%s', AvailableCopies = '%s', TotalCopies = '%s'," \
        #             %(Title.get(), Author.get() ,Year.get() ,Subject.get() ,AvailableCopies.get() ,TotalCopies.get())
        cursor.execute(find_user)
        db.commit()
        db.close()
        messagebox.showinfo("success",'ho gya')
    except:
        messagebox.showinfo('error','nhi hua')
    finally:
        clear()

def clear():
    idbook.set('')
    Title.set('')
    Author.set('')
    Year.set('')
    Subject.set('')
    AvailableCopies.set('')
    TotalCopies.set('')
    e1.configure(State = 'normal')


def showbook():
    def showallrecords():
        data = readfromdatabase()
        for index, dat in enumerate(data):
            Label(master, text=dat[0]).grid(row=index + 1, column=0)
            Label(master, text=dat[1]).grid(row=index + 1, column=1)
            Label(master, text=dat[2]).grid(row=index + 1, column=2)
            Label(master, text=dat[3]).grid(row=index + 1, column=3)
            Label(master, text=dat[4]).grid(row=index + 1, column=4)
            Label(master, text=dat[5]).grid(row=index + 1, column=5)
            Label(master, text=dat[6]).grid(row=index + 1, column=6)

    def readfromdatabase():
        cur.execute("SELECT * FROM test.book_tbl")
        return cur.fetchall()

    master = Tk()
    master.geometry('700x650')
    master.configure(bg='#ffb900')
    master.title('Records of all books')
    connection = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
    cur = connection.cursor()
    idbookLabel = Label(master, text="idbook", width=13)
    idbookLabel.grid(row=0, column=0)
    TitleLabel = Label(master, text="title", width=13)
    TitleLabel.grid(row=0, column=1)
    AuthorLabel = Label(master, text="Author", width=13)
    AuthorLabel.grid(row=0, column=2)
    YearLabel = Label(master, text="Year", width=13)
    YearLabel.grid(row=0, column=3)
    SubjectLabel = Label(master, text="Subject", width=13)
    SubjectLabel.grid(row=0, column=4)
    AvailableCopiesLabel = Label(master, text="Available Copies", width=15)
    AvailableCopiesLabel.grid(row=0, column=5)
    TotalCopiesLabel = Label(master, text="Total Copies", width=15)
    TotalCopiesLabel.grid(row=0, column=6)

    btn = Button(master, text='fetch', command=showallrecords).place(x=400, y=350)
    master = mainloop()











# def showbook():
#     def showallrecords():
#         data = readfromdatabase()
#         for index, dat in enumerate(data):
#             Label(master, text=dat[0]).grid(row=index + 1, column=0)
#             Label(master, text=dat[1]).grid(row=index + 1, column=1)
#             Label(master, text=dat[2]).grid(row=index + 1, column=2)
#             Label(master, text=dat[3]).grid(row=index + 1, column=3)
#             Label(master, text=dat[4]).grid(row=index + 1, column=4)
#             Label(master, text=dat[5]).grid(row=index + 1, column=5)
#             Label(master, text=dat[6]).grid(row=index + 1, column=6)
#
#     def readfromdatabase():
#         cur.execute("SELECT * FROM test.book_tbl")
#         return cur.fetchall()
#
#     master = Tk()
#     master.geometry('700x650')
#     master.configure(bg='#ffb900')
#     master.title('Records of all books')
#     connection = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
#     cur = connection.cursor()
#     idbookLabel = Label(master, text="idbook", width=13)
#     idbookLabel.grid(row=0, column=0)
#     TitleLabel = Label(master, text="title", width=13)
#     TitleLabel.grid(row=0, column=1)
#     AuthorLabel = Label(master, text="Author", width=13)
#     AuthorLabel.grid(row=0, column=2)
#     YearLabel = Label(master, text="Year", width=13)
#     YearLabel.grid(row=0, column=3)
#     SubjectLabel = Label(master, text="Subject", width=13)
#     SubjectLabel.grid(row=0, column=4)
#     AvailableCopiesLabel = Label(master, text="Available Copies", width=15)
#     AvailableCopiesLabel.grid(row=0, column=5)
#     TotalCopiesLabel = Label(master, text="Total Copies", width=15)
#     TotalCopiesLabel.grid(row=0, column=6)
#
#     btn = Button(master, text='fetch', command=showallrecords).place(x=400, y=350)
#     master = mainloop()
#
#
# boook = Tk()
# boook.title("Book")
#
# boook.geometry("250x250")
# boook.configure(bg='#ffb900')
# btnaddbook = Button(boook, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Update Books',command=updatebook)
# btnaddbook.place(x=50, y=100)
# btnaddbook = Button(boook, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Show all Books',command=showbook)
# btnaddbook.place(x=50, y=200)
# boook.mainloop()


w1 = Tk()
w1.title('update')
w1.geometry('700x600')
# ptitle = Label(w1,text = 'update')
# ptitle.grid(row = 0, coloumn = 0)
idbook = StringVar()
Title = StringVar()
Author = StringVar()
Year = StringVar()
Subject= StringVar()
AvailableCopies= StringVar()
TotalCopies = StringVar()

l1 = Label(w1, text='idbook')
e1 = Entry(w1, textvariable = idbook)
l2 = Label(w1, text='Title')
e2 = Entry(w1, textvariable = Title)
l3 = Label(w1, text='Author')
e3 = Entry(w1, textvariable = Author)
l4 = Label(w1, text='Year')
e4 = Entry(w1, textvariable = Year)
l5 = Label(w1, text='Subject')
e5 = Entry(w1, textvariable = Subject)
l6 = Label(w1, text='AvailableCopies')
e6 = Entry(w1, textvariable = AvailableCopies)
l7 = Label(w1, text='TotalCopies')
e7 = Entry(w1, textvariable = TotalCopies)


b = Button(w1, text ='Show', command = showbook)
b.place(x=250,y=10)
b1 = Button(w1, text ='Search', command = search)
b1.place(x=250,y=50)
b2 = Button(w1, text = 'Update', command = updatebook)
b2.place(x=250,y=90)
b3 = Button(w1, text = 'Clear', command = clear)
b3.place(x=250,y=130)

l1.grid(row = 1, column = 0)
e1.grid(row = 1, column = 1)


l2.grid(row = 2, column = 0)
e2.grid(row = 2, column = 1)

l3.grid(row = 3, column = 0)
e3.grid(row = 3, column = 1)

l4.grid(row = 4, column = 0)
e4.grid(row = 4, column = 1)

l5.grid(row = 5, column = 0)
e5.grid(row = 5, column = 1)

l6.grid(row = 6, column = 0)
e6.grid(row = 6, column = 1)

l7.grid(row = 7, column = 0)
e7.grid(row = 7, column = 1)



w1.mainloop()
