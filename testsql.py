# #!/usr/bin/python
# import pymysql
#
#
# #id = nameE.get()
# #strpswd = passwdE.get()
# # Connect
# db = pymysql.connect(host="localhost",user="root",passwd="redhat",db="test")
#
# cursor = db.cursor()
#
# # Execute SQL select statement
# #cursor.execute("SELECT * FROM test.department")
# cursor.execute("Select * from customer where user_ID ='" + id + "'and password ='" + strpswd + "'")
# # Commit your changes if writing
# # In this case, we are only reading data
# # db.commit()
#
# # Get the number of rows in the resultset
# numrows = cursor.rowcount
#
# # Get and display one row at a time
# # for x in range(0, numrows):
# #     row = cursor.fetchone()
# #     print (row[0], "-->", row[1], "-->", row[2])
# # Close the connection
# data = cursor.fetchone()
#
# print(data)
#
# db.close()




from tkinter import *

import pymysql

# Connect
db = pymysql.connect(host="localhost",user="root",passwd="redhat",db="test")
#
cursor = db.cursor()
#
# # Execute SQL select statement
cursor.execute("SELECT * FROM test.login")
#
# # Commit your changes if writing
# # In this case, we are only reading data
 # db.commit()
#
# # Get the number of rows in the resultset
numrows = cursor.rowcount
#
# # Get and display one row at a time
for x in range(0, numrows):
     row = cursor.fetchone()
     print (row[0], "-->", row[1])
 # Close the connection
db.close()
#
#
# def loginn():
#
#     a =  nameE.get()
#     b = passwdE.get()
#
#     # global deptno
#     # global deptname
#
#     db = pymysql.connect(host="localhost", user="root", passwd="redhat", db="test")
#     cursor = db.cursor()
#
#     # Execute SQL select statement
#     #cursor.execute("SELECT * FROM test.department")
#
#     #cursor.execute("Select * from customer where NAME ='" + id + "'and PASSWORD ='" + strpswd + "'")
#     cursor.execute("Select * from simple_development.login where USERNAME ='" + a + "'and pasword ='" + b + "'")
#
#     #if( deptno == nameE.get() , deptname == passwdE.get()):
#      #   nameL = Label(log, text="HO GYA LOGIN")
#       #  nameL.place(x=100, y=100)
#
#     #else:
#        # namel2 =Label (log,text ="sahi data daalooo")
#         #namel2.place(x=100,y=100)
#
#     db.close()
#
#
#     log = Tk()
#
#     log.title("LOGINED")
#
#     log.geometry("250x250")
#
#     nameL = Label(log, text="HO GYA LOGIN")
#     nameL.place(x=100, y=100)
#
#
#     log.mainloop()
#
#
# def signupp():
#     sup = Tk()
#
#     sup.title("Sign Up Form")
#
#     sup.geometry("250x250")
#
#     nameL = Label(sup, text="Chalo Data Dalo")
#     nameL.place(x=100, y=100)
#
#     sup.mainloop()
#
#
# roots = Tk()
#
# roots.title("LOGIN")
#
# roots.geometry("250x250")
#
# ##instruction = Label(roots, text="Enter New credidential\n")
# ##instruction.grid(row=0,column=0,sticky=E)
# ##
#
# ##nameL = Label(roots,text="NAME",bd=5, bg="powder blue")
# ##nameL.place(x=10,y=30)
#
#
# nameL = Label(roots, text="NAME")
# nameL.place(x=10, y=30)
#
# nameE = Entry(roots, bg="powder blue")
# nameE.place(x=80, y=30)
#
# passwdL = Label(roots, text="PASSWORD")
# passwdL.place(x=10, y=60)
#
# passwdE = Entry(roots, bg="powder blue", show="*")
# passwdE.place(x=80, y=60)
#
# btnlogin = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Login', command=loginn)
# btnlogin.place(x=50, y=100)
#
# btnsignup = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Signup', command=signupp)
# btnsignup.place(x=150, y=100)
#
# btncancel = Button(roots, padx=8, bd=8, fg='black', font=('arial', 10, 'bold'), text='Quit', command=quit)
# btncancel.place(x=100, y=150)
#
# roots.mainloop()
