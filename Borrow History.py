from tkinter import *
import pymysql
from tkinter import messagebox as ms
from tkinter import messagebox

###########################ISSUE BOOK##############################
def issuebook():

    def issue():
        i = BorrowidE.get()
        ia = StuidE.get()
        ib = BookIdE.get()
        ic = BorrowDE.get()
        id = DuedateE.get()
        ie = ReturndateE.get()
        ig = NotesE.get()
        ih= StatusE.get()

        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
        cursor = db.cursor()

        issue_book = ("INSERT  INTO test.borrow_history(BorrowId,StudentId,BookId,BorrowDate,DueDate,ReturnDate,Notes,Status) VALUES(" + i + "," + ia + " , " + ib + " , " + ic + " , '" + id + " ','" + ie + "','" + ig + "','"+ih+"');")

        cursor.execute(issue_book)

        result = cursor.fetchall()

        ms._show(" Issue Book", "Successfully Added")

        db.commit()
        db.close()

        if result:
            print("successfull")

        else:
            print("nhi hua")

    roots = Tk()

    roots.title("issue book")

    roots.geometry("255x450")
    roots.configure(bg='#ffb900')

    BorrowidL = Label(roots, text="Borrow Id", )
    BorrowidL.place(x=20, y=0)

    BorrowidE = Entry(roots, bg="powder blue")
    BorrowidE.place(x=100, y=0)


    StuidL = Label(roots, text="Student Id", )
    StuidL.place(x=20, y=40)

    StuidE = Entry(roots, bg="powder blue")
    StuidE.place(x=100, y=40)

    BookIdL = Label(roots, text="Book Id", )
    BookIdL.place(x=20, y=90)

    BookIdE = Entry(roots, bg="powder blue")
    BookIdE.place(x=100, y=90)

    BorrowDL = Label(roots, text="Borrow Date", )
    BorrowDL.place(x=20, y=140)

    BorrowDE = Entry(roots, bg="powder blue")
    BorrowDE.place(x=100, y=140)

    DuedateL = Label(roots, text="Due Date", )
    DuedateL.place(x=20, y=190)

    DuedateE = Entry(roots, bg="powder blue")
    DuedateE.place(x=100, y=190)

    ReturndateL = Label(roots, text="Return Date", )
    ReturndateL.place(x=20, y=240)

    ReturndateE = Entry(roots, bg="powder blue")
    ReturndateE.place(x=100, y=240)

    Notesl = Label(roots, text="Notes", )
    Notesl.place(x=20, y=290)

    NotesE = Entry(roots, bg="powder blue")
    NotesE.place(x=100, y=290)

    Statusl = Label(roots, text="Status", )
    Statusl.place(x=20, y=340)

    StatusE = Entry(roots, bg="powder blue")
    StatusE.place(x=100, y=340)

    btnissue = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Issue',command=issue)
    btnissue.place(x=40, y=400)

    btncancel = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit')
    btncancel.place(x=150, y=400)
    roots.mainloop()

###############################RETURN BOOK#####################################################

def returnbook():
    roots = Tk()

    roots.title("LOGIN")

    roots.geometry("255x450")
    roots.configure(bg='#ffb900')

    StuidL = Label(roots, text="Student Id", )
    StuidL.place(x=20, y=40)

    StuidE = Entry(roots, bg="powder blue")
    StuidE.place(x=100, y=40)

    BookIdL = Label(roots, text="Book Id", )
    BookIdL.place(x=20, y=90)

    BookIdE = Entry(roots, bg="powder blue")
    BookIdE.place(x=100, y=90)

    BorrowDL = Label(roots, text="Borrow Date", )
    BorrowDL.place(x=20, y=140)

    BorrowDE = Entry(roots, bg="powder blue")
    BorrowDE.place(x=100, y=140)

    DuedateL = Label(roots, text="Due Date", )
    DuedateL.place(x=20, y=190)

    DuedateE = Entry(roots, bg="powder blue")
    DuedateE.place(x=100, y=190)

    ReturndateL = Label(roots, text="Return Date", )
    ReturndateL.place(x=20, y=240)

    ReturndateE = Entry(roots, bg="powder blue")
    ReturndateE.place(x=100, y=240)

    Notesl = Label(roots, text="Notes", )
    Notesl.place(x=20, y=290)

    NotesE = Entry(roots, bg="powder blue")
    NotesE.place(x=100, y=290)

    Statusl = Label(roots, text="Notes", )
    Statusl.place(x=20, y=340)

    StatusE = Entry(roots, bg="powder blue")
    StatusE.place(x=100, y=340)

    btnissue = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Issue')
    btnissue.place(x=40, y=400)

    btncancel = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit')
    btncancel.place(x=150, y=400)
    roots.mainloop()

r=Tk()
r.geometry('100x100')
btn=Button(r,text='issue',command=issuebook).place(x=10,y=10)
btn2=Button(r,text='return',command=returnbook).place(x=10,y=50)

r.mainloop()