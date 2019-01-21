from tkinter import *
import pymysql
from tkinter import messagebox as ms
from tkinter import messagebox


# Open database connection
# db = pymysql.connect("localhost","root","redhat","test" )
#
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
#
# # execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)
#
# # disconnect from server
# db.close()

# Connect
# db = pymysql.connect(host="localhost",user="root",passwd="redhat",db="test")
#
# cursor = db.cursor()
#
# # Execute SQL select statement
# cursor.execute("SELECT * FROM test.department")
#
# # Commit your changes if writing
# # In this case, we are only reading data
# # db.commit()
#
# # Get the number of rows in the resultset
# numrows = cursor.rowcount
#
# # Get and display one row at a time
# for x in range(0, numrows):
#     row = cursor.fetchone()
#     print (row[0], "-->", row[1], "-->", row[2])
# # Close the connection
# db.close()


def loginn():

    a = nameE.get()
    b = passwdE.get()

    print(a)
    print(b)

    db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
    cursor = db.cursor()


    # find_user = ("SELECT * FROM test.login WHERE username = '"+a+"' and passwords = "+b+" ")

    find_user = ("SELECT * FROM test.login WHERE username = 'vivek' and passwords = 123 ")

    cursor.execute(find_user)

    result = cursor.fetchone()

    if result:

            def book():

                def addbook():

                    def btnadd():
                        b= bidE.get()
                        ba = btitleE.get()
                        bb = bauthorE.get()
                        bc=byearE.get()
                        bd=bsubjectE.get()
                        be=bavicopiesE.get()
                        bf=btotalcopiesE.get()

                        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
                        cursor = db.cursor()

                        ins_book= ("INSERT  INTO test.book_tbl(BookId,Title,Author,Year,Subject,AvailableCopies,TotalCopies) VALUES("+b+",' " + ba + " ',' " + bb + " ', " + bc + " ,' " + bd + " '," + be + "," + bf + ");")

                        cursor.execute(ins_book)

                        ms._show("Book ADD", "Successfully Added")

                        db.commit()
                        db.close()



                        if result:
                            print("successfull")

                        else:
                            print ("nhi hua")


                    #########################################################################

                    baddlog = Tk()

                    baddlog.title("ADD Book")

                    baddlog.geometry("555x385")

                    #################################################

                    bidL = Label(baddlog, text="Book ID")
                    bidL.place(x=40, y=50)

                    btitleL = Label(baddlog, text="Book Title")
                    btitleL.place(x=40, y=90)

                    bauthorL = Label(baddlog, text="Book Author")
                    bauthorL.place(x=40, y=130)

                    byearL = Label(baddlog, text="Book year")
                    byearL.place(x=310, y=50)

                    bsubjectL = Label(baddlog, text="Book Subject")
                    bsubjectL.place(x=310, y=90)

                    baviecopiesL = Label(baddlog, text="Avilable Copies")
                    baviecopiesL.place(x=310, y=130)

                    btotalcopiesL = Label(baddlog,text ="Total Copies")
                    btotalcopiesL.place(x=40,y=170)


                    ###################################################

                    bidE = Entry(baddlog, bg="powder blue")
                    bidE.place(x=110, y=50)

                    btitleE = Entry(baddlog, bg="powder blue")
                    btitleE.place(x=110, y=90)

                    bauthorE = Entry(baddlog, bg="powder blue")
                    bauthorE.place(x=110, y=130)

                    byearE = Entry(baddlog, bg="powder blue")
                    byearE.place(x=395, y=50)

                    bsubjectE = Entry(baddlog, bg="powder blue")
                    bsubjectE.place(x=395, y=90)

                    bavicopiesE = Entry(baddlog, bg="powder blue")
                    bavicopiesE.place(x=395, y=130)

                    btotalcopiesE = Entry(baddlog,bg ="powder blue")
                    btotalcopiesE.place(x=110,y=170)

                    ################################################

                    btnaddbook = Button(baddlog, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='ADD',command = btnadd)
                    btnaddbook.place(x=150, y=240)

                    # btnfetchbook = Button(baddlog, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'),
                    #                       text='Fetch All Books')
                    # btnfetchbook.place(x=230, y=240)

                    btncancel = Button(baddlog, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Cancel',
                                       command=quit)
                    btncancel.place(x=380, y=240)

                    #########################################

                    baddlog.mainloop()

                def showbook():
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
                    master.geometry('385x255')
                    master.configure(bg = '#ffff00')
                    master.title('Records')
                    connection = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
                    cur = connection.cursor()
                    usernameLabel = Label(master, text="Username", width=10)
                    usernameLabel.grid(row=0, column=0)
                    BMILabel = Label(master, text="Passwords", width=10)
                    BMILabel.grid(row=0, column=1)
                    roleLabel = Label(master, text="Role", width=10)
                    roleLabel.grid(row=0, column=2)
                    btn = Button(master, text='fetch', command=showallrecords).place(x=310, y=90)
                    master = mainloop()

                def update():


                    def search():
                        try:
                            db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
                            cursor = db.cursor()
                            find_user = "select * from test.book_tbl where BookId = '%s'" % idbook.get()
                            # find_user = "select * from test.book_tbl where BookId = 1"
                            cursor.execute(find_user)
                            result = cursor.fetchone()
                            Title.set(result[1])
                            Author.set(result[2])
                            Year.set(result[3])
                            Subject.set(result[4])
                            AvailableCopies.set(result[5])
                            TotalCopies.set(result[6])
                            e1.configure(state='disabled')
                            db.commit()
                            db.close()
                        except:
                            messagebox.showinfo('no data')
                            clear()

                    def updatebook():
                        try:
                            ubid = e1.get()
                            ubtitle = e2.get()
                            ubauthor = e3.get()
                            ubyear = e4.get()
                            ubsubject = e5.get()
                            ubavailable = e6.get()
                            ubtot = e7.get()

                            print(ubid)
                            print(ubtitle)
                            print(ubauthor)
                            print(ubyear)
                            print(ubsubject)
                            print(ubavailable)
                            print(ubtot)

                            db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
                            cursor = db.cursor()

                            find_user = "UPDATE test.book_tbl SET Title = '" + ubtitle + "', Author = '" + ubauthor + "', Year = " + ubyear + ", Subject = '" + ubsubject + "', AvailableCopies = " + ubavailable + ", TotalCopies = " + ubtot + " WHERE BookId = " + ubid + ";"

                            # find_user = "UPDATE sample.book set Title = '%s', Author = '%s', Year = '%s', Subject = '%s', AvailableCopies = '%s', TotalCopies = '%s'," \
                            #             %(Title.get(), Author.get() ,Year.get() ,Subject.get() ,AvailableCopies.get() ,TotalCopies.get())
                            cursor.execute(find_user)
                            db.commit()
                            db.close()
                            messagebox.showinfo("success", 'ho gya')
                        except:
                            messagebox.showinfo('error', 'nhi hua')
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
                        e1.configure(State='normal')

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


                    w1 = Tk()
                    w1.title('update')
                    w1.geometry('300x300')
                    # ptitle = Label(w1,text = 'update')
                    # ptitle.grid(row = 0, coloumn = 0)
                    idbook = StringVar()
                    Title = StringVar()
                    Author = StringVar()
                    Year = StringVar()
                    Subject = StringVar()
                    AvailableCopies = StringVar()
                    TotalCopies = StringVar()

                    l1 = Label(w1, text='idbook')
                    e1 = Entry(w1, textvariable=idbook)
                    l2 = Label(w1, text='Title')
                    e2 = Entry(w1, textvariable=Title)
                    l3 = Label(w1, text='Author')
                    e3 = Entry(w1, textvariable=Author)
                    l4 = Label(w1, text='Year')
                    e4 = Entry(w1, textvariable=Year)
                    l5 = Label(w1, text='Subject')
                    e5 = Entry(w1, textvariable=Subject)
                    l6 = Label(w1, text='AvailableCopies')
                    e6 = Entry(w1, textvariable=AvailableCopies)
                    l7 = Label(w1, text='TotalCopies')
                    e7 = Entry(w1, textvariable=TotalCopies)

                    b = Button(w1, text='Show', command=showbook)
                    b.place(x=250, y=10)
                    b1 = Button(w1, text='Search', command=search)
                    b1.place(x=250, y=50)
                    b2 = Button(w1, text='Update', command=updatebook)
                    b2.place(x=250, y=90)
                    b3 = Button(w1, text='Clear', command=clear)
                    b3.place(x=250, y=130)

                    l1.grid(row=1, column=0)
                    e1.grid(row=1, column=1)

                    l2.grid(row=2, column=0)
                    e2.grid(row=2, column=1)

                    l3.grid(row=3, column=0)
                    e3.grid(row=3, column=1)

                    l4.grid(row=4, column=0)
                    e4.grid(row=4, column=1)

                    l5.grid(row=5, column=0)
                    e5.grid(row=5, column=1)

                    l6.grid(row=6, column=0)
                    e6.grid(row=6, column=1)

                    l7.grid(row=7, column=0)
                    e7.grid(row=7, column=1)

                    w1.mainloop()

                def borrowbook():
                    ###########################ISSUE BOOK##############################
                    def issuebook():
                        roots = Tk()

                        roots.title("ISSUE BOOK")

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

                    ############################SHOW BORROW HISTORY#####################################################

                    def borrowhist():
                        def showallrecords():
                            data = readfromdatabase()
                            for index, dat in enumerate(data):
                                Label(master, text=dat[0]).grid(row=index + 1, column=0)
                                Label(master, text=dat[1]).grid(row=index + 1, column=1)
                                # Label(master, text=dat[2]).grid(row=index + 1, column=2)

                        def readfromdatabase():
                            cur.execute("SELECT * FROM test.borrow_history")
                            return cur.fetchall()

                        master = Tk()
                        master.geometry('600x500')
                        master.title('Records')
                        connection = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
                        cur = connection.cursor()
                        BorrowidL = Label(master, text="BorrowId", width=10)
                        BorrowidL.grid(row=0, column=0)
                        StudentidL = Label(master, text="StudentId", width=10)
                        StudentidL.grid(row=0, column=1)
                        Bookidl = Label(master, text="BookId", width=10)
                        Bookidl.grid(row=0, column=2)

                        Borrowdatel = Label(master, text="Borrow Date", width=10)
                        Borrowdatel.grid(row=0, column=3)
                        Duedatel = Label(master, text="Due Date", width=10)
                        Duedatel.grid(row=0, column=4)
                        Retdatel = Label(master, text="Return Date", width=10)
                        Retdatel.grid(row=0, column=5)
                        Notesl = Label(master, text="Notes", width=10)
                        Notesl.grid(row=0, column=6)
                        Statusl = Label(master, text="Status", width=10)
                        Statusl.grid(row=0, column=7)

                        btn = Button(master, text='fetch', command=showallrecords).place(x=120, y=200)
                        master = mainloop()

                    brrw=Tk()
                    boook.withdraw()
                    brrw.geometry('250x250')
                    brrw.title("Borrow Book")

                    btnissuebook = Button(brrw,text='Issue Book',command=issuebook)
                    btnissuebook.place(x=70,y=30)

                    btnretbook = Button(brrw,text='Return Book',command=returnbook)
                    btnretbook.place(x=70,y=80)

                    btnretbook = Button(brrw, text='Show Borrow History', command=borrowhist)
                    btnretbook.place(x=70, y=130)

                    brrw.mainloop()

                boook = Tk()
                log.withdraw()
                boook.title("Book")

                boook.geometry("250x250")
                boook.configure(bg='#0000ff')

                btnaddbook = Button(boook, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Add Book',
                                    command=addbook)
                btnaddbook.place(x=50, y=50)

                btnaddbook = Button(boook, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Update Book',
                                    command=update)
                btnaddbook.place(x=50, y=100)

                btnaddbook = Button(boook, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Delete Book',
                                    command=book)
                btnaddbook.place(x=50, y=150)

                btnaddbook = Button(boook, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Borrow Book',
                                    command=borrowbook)
                btnaddbook.place(x=50, y=200)

                boook.mainloop()

            def stu():

                sup = Tk()
                sup.resizable(width=FALSE, height=FALSE)
                sup.geometry('900x700')
                sup.configure(bg='dark gray')
                sup.title('Sign up')

                lblwel = Label(sup, text="ADD NEW STUDENT RECORD", font=("bold", 20)).place(x=300, y=30)

                fnamesup = Label(sup, text="First Name", font=("bold", 15)).place(x=300, y=100)

                lnamesup = Label(sup, text="Last Name", font=("bold", 15)).place(x=300, y=160)

                dptsup = Label(sup, text="Department Name", font=("bold", 15)).place(x=300, y=220)

                branchsup = Label(sup, text="Branch", font=("bold", 15)).place(x=300, y=280)

                semestersup = Label(sup, text="Semester", font=("bold", 15)).place(x=300, y=340)

                yearsup = Label(sup, text="Year", font=("bold", 15)).place(x=300, y=400)

                Enrollsup = Label(sup, text="En.Roll", font=("bold", 15)).place(x=300, y=460)

                e1 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                e1.place(x=500, y=100)
                e2 = Entry(sup, width=20, font=("bold", 15), show="*", highlightthickness=2, bg="powder blue",
                           relief=SUNKEN)
                e2.place(x=500, y=160)
                e3 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                e3.place(x=500, y=220)
                # default = StringVar()
                e4 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                ##default.set("root")
                e4.place(x=500, y=280)
                e5 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                e5.place(x=500, y=340)

                e6 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                e6.place(x=500, y=400)

                e7 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                e7.place(x=500, y=460)

                btnadd = Button(sup, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='ADD')#, command=add)
                btnadd.place(x=400, y=550)

                btncancelsup = Button(sup, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit',
                                      command=quit)
                btncancelsup.place(x=550, y=550)

                # b1 = Button(sup, text="Sign Up", width=25, height=2, bg=g, fg="white", font="5", relief=RAISED, overrelief=RIDGE,
                #             )#command=login_database)
                # b1.place(x=858, y=600)
                ##l = Label(sup, font="10", bg=gg)
                ##l.place(x=928, y=660)
                sup.bind('<Return>')
                sup.mainloop()

            # def showusr():
            #
            #     db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
            #     cursor = db.cursor()
            #
            #     # find_user = ("SELECT * FROM test.login WHERE username = '"+a+"' and passwords = "+b+" ")
            #
            #     find_user = ("SELECT * FROM test.login")
            #
            #     cursor.execute(find_user)
            #
            #     result = cursor.fetchall()
            #
            #     for el in result:
            #
            #         print(el)
            #
            #     susr = Tk()
            #
            #
            #
            #     susr = mainloop()

            def usr():

                def delete():
                    name = e1name.get()

                    db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
                    cursor = db.cursor()

                    # find_user = ("INSERT  INTO test.login(username,passwords) VALUES(' " + name + " '," + pswd + ");")

                    find_user = ("DELETE FROM test.login WHERE username ='" + name + "' ;")

                    # find_user = ("UPDATE test.login set passwords = 123456789 where username = 'ruchika';")

                    cursor.execute(find_user)

                    ms._show("Delete", "Successfully Deleted")

                    # print("DATA DELETED")

                    # print("Data UPDATED")
                    db.commit()
                    db.close()



                remu = Tk()
                remu.resizable(width=FALSE, height=FALSE)
                remu.geometry('400x400')
                remu.configure(bg='dark gray')
                remu.title('REMOVE USER')



                fnamesup = Label(remu, text="Username", font=("bold", 15)).place(x=50, y=100)



                #######################################

                e1name= Entry(remu, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
                e1name.place(x=150, y=100)
                # e2 = Entry(sup, width=20, font=("bold", 15), show="*", highlightthickness=2, bg="powder blue",
                #            relief=SUNKEN)
                # e2.place(x=150, y=160)

                btnadd = Button(remu, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Delete', command=delete)
                btnadd.place(x=150, y=250)

                btncancelsup = Button(remu, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit',
                                      command=quit)
                btncancelsup.place(x=250, y=250)

                # b1 = Button(sup, text="Sign Up", width=25, height=2, bg=g, fg="white", font="5", relief=RAISED, overrelief=RIDGE,
                #             )#command=login_database)
                # b1.place(x=858, y=600)
                ##l = Label(sup, font="10", bg=gg)
                ##l.place(x=928, y=660)
                remu.bind('<Return>')
                remu.mainloop()


            log = Tk()

            log.title("Peoples Library")
            log.configure(bg='#870c78')

            log.geometry("235x245")

            nameL = Label(log, text="Welcome Admin")
            nameL.place(x=25, y=15)

            btnbook = Button(log, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Books', command=book)
            btnbook.place(x=90, y=60)

            btnstu = Button(log, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'),
                                  text='Student',command=stu )
            btnstu.place(x=90, y=120)

            btnusr = Button(log, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Remove User',command=usr)
            btnusr.place(x=90, y=180)

            # btnshowusr = Button(log, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'),
            #                       text='Show user', command=showusr)
            # btnshowusr.place(x=100, y=250)




            log.mainloop()

    else:
        # print("nhi hua")
        ms.showerror('Oops!', 'Username Not Found.')

    db.close()


def signupp():

    def add():

        name = e1.get()
        pswd = e2.get()

        db = pymysql.connect(host="localhost", user="root", password="redhat", db="test")
        cursor = db.cursor()

        find_user = ("INSERT  INTO test.login(username,passwords) VALUES(' " + name +  " '," + pswd + ");")

        # find_user = ("DELETE FROM test.login WHERE username = 'raj';")

       # find_user = ("UPDATE test.login set passwords = 123456789 where username = 'ruchika';")

        cursor.execute(find_user)

        ms._show("Signup","Successfully Added")



        # print("DATA DELETED")

        # print("Data UPDATED")

        db.commit()
        db.close()



    sup = Tk()
    sup.resizable(width=FALSE, height=FALSE)
    sup.geometry('400x400')
    sup.configure(bg='dark gray')
    sup.title('Sign up')

    lblwel = Label(sup,text="Enter Your Details",font=("bold", 20)).place(x=50,y=30)


    fnamesup = Label(sup, text = "Username",font=("bold", 15)).place(x=50,y=100)

    paswordsup = Label(sup, text = "Password",font=("bold", 15)).place(x=50,y= 160)

    #######################################

    e1 = Entry(sup, width=20, font=("bold", 15), highlightthickness=2, bg="powder blue", relief=SUNKEN)
    e1.place(x=150, y=100)
    e2 = Entry(sup, width=20, font=("bold", 15), show="*", highlightthickness=2, bg="powder blue", relief=SUNKEN)
    e2.place(x=150, y=160)


    btnadd = Button(sup, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='ADD',command = add)
    btnadd.place(x=150, y = 250)

    btncancelsup = Button(sup, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit',command = quit)
    btncancelsup.place(x=250, y=250)

    # b1 = Button(sup, text="Sign Up", width=25, height=2, bg=g, fg="white", font="5", relief=RAISED, overrelief=RIDGE,
    #             )#command=login_database)
    # b1.place(x=858, y=600)
    ##l = Label(sup, font="10", bg=gg)
    ##l.place(x=928, y=660)
    sup.bind('<Return>')
    sup.mainloop()


roots = Tk()



roots.title("LOGIN")

roots.geometry("250x250")
roots.configure(bg = '#ffb900')

nameL = Label(roots, text="NAME",)
nameL.place(x=10, y=30)

nameE = Entry(roots, bg="powder blue")
nameE.place(x=80, y=30)

passwdL = Label(roots, text="PASSWORD",)
passwdL.place(x=10, y=60)

passwdE = Entry(roots, bg="powder blue", show="*")
passwdE.place(x=80, y=60)

btnlogin = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Login', command=loginn)
btnlogin.place(x=50, y=100)

btnsignup = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Signup', command=signupp)
btnsignup.place(x=150, y=100)

btncancel = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit', command=quit)
btncancel.place(x=100, y=150)

roots.mainloop()
