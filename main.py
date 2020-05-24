#frontend

from tkinter import *
import tkinter.messagebox as mbox
import stdDatabase_backend

class Student:

    def __init__(self,root):
        self.root=root
        self.root.title("student database management system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="ghost white")#bg="blue"

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # ******************************Function****************************************************
        def iexit():
            iexit=mbox.askyesno("student database management system","confirm if you really want to exit")
            if iexit>0:
                root.destroy()
                return

        def cleardata():
            self.txtstdID.delete(0,END)
            self.txtfirstname.delete(0, END)
            self.txtlastname.delete(0, END)
            self.txtdob.delete(0, END)
            self.txtage.delete(0, END)
            self.txtgender.delete(0, END)
            self.txtaddress.delete(0, END)
            self.txtmobile.delete(0, END)

        def addData():
            if(len(StdID.get())!=0):
                stdDatabase_backend.addstudentrecord(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),
                                    Gender.get(),Address.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),
                                    Gender.get(),Address.get(),Mobile.get()))


        def Displaydata():
            studentlist.delete(0, END)
            for row in stdDatabase_backend.viewdata():
                studentlist.insert(END,row,str(""))

        def studentrec(event):
            global sd
            searchstd=studentlist.curselection()[0]
            sd=studentlist.get(searchstd)

            self.txtstdID.delete(0, END)
            self.txtstdID.insert(END,sd[0])
            self.txtfirstname.delete(0, END)
            self.txtfirstname.insert(END, sd[1])
            self.txtlastname.delete(0, END)
            self.txtlastname.insert(END, sd[2])
            self.txtdob.delete(0, END)
            self.txtdob.insert(END, sd[3])
            self.txtage.delete(0, END)
            self.txtage.insert(END, sd[4])
            self.txtgender.delete(0, END)
            self.txtgender.insert(END, sd[5])
            self.txtaddress.delete(0, END)
            self.txtaddress.insert(END, sd[6])
            self.txtmobile.delete(0, END)
            self.txtmobile.insert(END, sd[7])

        def Deletedata():
            if (len(StdID.get()) != 0):
                stdDatabase_backend.deleteRec(StdID.get())
                cleardata()
                Displaydata()

        def searchdatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_backend.searchdata(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),
                                    Gender.get(),Address.get(),Mobile.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if(len(StdID.get())!=0):
                stdDatabase_backend.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                stdDatabase_backend.addstudentrecord(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),
                                    Gender.get(),Address.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),
                                    Gender.get(),Address.get(),Mobile.get()))




        #******************************myframe****************************************************
        Mainframe=Frame(self.root)#,bg='blue'
        Mainframe.grid()

        Titleframe = Frame(Mainframe,bd=2,padx=54,pady=8 ,bg='red',relief=RIDGE)
        Titleframe.pack(side=TOP)

        self.lbltitle=Label(Titleframe,font=('arial',47,'bold'),text='Student Database Management System',bg='red')
        self.lbltitle.grid()

        Buttonframe = Frame(Mainframe, bd=2,width=1350,height=70 ,padx=18, pady=10, bg='blue', relief=RIDGE)
        Buttonframe.pack(side=BOTTOM)

        dataframe = Frame(Mainframe, bd=1,width=1300,height=400 ,padx=20, pady=20,bg='blue') #,bg='cadet blue'
        dataframe.pack(side=BOTTOM)

        dataframeleft = LabelFrame(dataframe, bd=1, width=1000, height=600, padx=20, pady=20, bg='red',relief=RIDGE,
         font = ('arial', 20, 'bold'),text="student info\n"
                                   )
        dataframeleft.pack(side=LEFT)

        dataframeright = LabelFrame(dataframe, bd=1, width=450, height=300, padx=31, pady=3, bg='red',
                                   relief=RIDGE,font = ('arial', 20, 'bold'),text="student details\n")
        dataframeright.pack(side=RIGHT)
        # ******************************Labels and entry widget****************************************************

        self.lblstdID = Label(dataframeleft, font=('arial', 20, 'bold'), text='student ID:',
                              bg='red', padx=2, pady=2)
        self.lblstdID.grid(row=0,column=0,sticky=W)

        self.txtstdID = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtstdID.grid(row=0, column=1, sticky=W)
        #------------------------------------------------------------------------------------
                  #next label
        #------------------------------------------------------------------------------------
        self.lblfirstname = Label(dataframeleft, font=('arial', 20, 'bold'), text='FirstName:',
                              bg='red', padx=2, pady=2)
        self.lblfirstname.grid(row=1, column=0, sticky=W)

        self.txtfirstname = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfirstname.grid(row=1, column=1, sticky=W)

        # ------------------------------------------------------------------------------------
        # next label
        # ------------------------------------------------------------------------------------
        self.lbllastname = Label(dataframeleft, font=('arial', 20, 'bold'), text='LastName:',
                                  bg='red', padx=2, pady=2)
        self.lbllastname.grid(row=2, column=0, sticky=W)

        self.txtlastname = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Lastname, width=39)
        self.txtlastname.grid(row=2,column=1, sticky=W)
        # ------------------------------------------------------------------------------------
        # next label
        # ------------------------------------------------------------------------------------
        self.lbldob = Label(dataframeleft, font=('arial', 20, 'bold'), text='Date of Birth:',
                                 bg='red', padx=2, pady=2)
        self.lbldob.grid(row=3, column=0, sticky=W)

        self.txtdob = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Dob, width=39)
        self.txtdob.grid(row=3, column=1, sticky=W)
        # ------------------------------------------------------------------------------------
        # next label
        # ------------------------------------------------------------------------------------
        self.lblage = Label(dataframeleft, font=('arial', 20, 'bold'), text='Age:',
                                 bg='red', padx=2, pady=2)
        self.lblage.grid(row=4, column=0, sticky=W)

        self.txtage = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtage.grid(row=4, column=1, sticky=W)
        # ------------------------------------------------------------------------------------
        # next label
        # ------------------------------------------------------------------------------------
        self.lblgender = Label(dataframeleft, font=('arial', 20, 'bold'), text='Gender:',
                                 bg='red', padx=2, pady=2)
        self.lblgender.grid(row=5, column=0, sticky=W)

        self.txtgender = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtgender.grid(row=5, column=1, sticky=W)
        # ------------------------------------------------------------------------------------
        # next label
        # ------------------------------------------------------------------------------------
        self.lbladdress = Label(dataframeleft, font=('arial', 20, 'bold'), text='Address:',
                                 bg='red', padx=2, pady=2)
        self.lbladdress.grid(row=6, column=0, sticky=W)

        self.txtaddress = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtaddress.grid(row=6, column=1, sticky=W)
        # ------------------------------------------------------------------------------------
        # next label
        # ------------------------------------------------------------------------------------
        self.lblmobile = Label(dataframeleft, font=('arial', 20, 'bold'), text='Mobile:',
                                bg='red', padx=2, pady=2)
        self.lblmobile.grid(row=7, column=0, sticky=W)

        self.txtmobile = Entry(dataframeleft, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtmobile.grid(row=7, column=1, sticky=W)

        # ------------------------------------------------------------------------------------
        # list box and scroll bar widget
        # ------------------------------------------------------------------------------------
        scrollbar=Scrollbar(dataframeright)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist=Listbox(dataframeright,width=41,height=16,font=('arial', 12, 'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',studentrec)
        studentlist.grid(row=0,column=0,padx=8)

        scrollbar.config(command=studentlist.yview)
        # ------------------------------------------------------------------------------------
        # button widgets
        # ------------------------------------------------------------------------------------

        self.btnadddata=Button(Buttonframe,text='Add New',font=('arial', 20, 'bold'),width=10,height=1,bd=4,command=addData)
        self.btnadddata.grid(row=0,column=0)
        self.btndisplay = Button(Buttonframe, text='Display', font=('arial', 20, 'bold'), width=10, height=1, bd=4,command=Displaydata)
        self.btndisplay.grid(row=0, column=1)
        self.btnclear = Button(Buttonframe, text='Clear', font=('arial', 20, 'bold'), width=10, height=1, bd=4,command=cleardata )
        self.btnclear.grid(row=0, column=2)
        self.btndelete = Button(Buttonframe, text='Delete', font=('arial', 20, 'bold'), width=10, height=1, bd=4,command=Deletedata)
        self.btndelete.grid(row=0, column=3)
        self.btnsearch = Button(Buttonframe, text='Search', font=('arial', 20, 'bold'), width=10, height=1, bd=4,command=searchdatabase)
        self.btnsearch.grid(row=0, column=4)
        self.btnupdate = Button(Buttonframe, text='Update', font=('arial', 20, 'bold'), width=10, height=1, bd=4,command=update)
        self.btnupdate.grid(row=0, column=5)
        self.btnexit = Button(Buttonframe, text='Exit', font=('arial', 20, 'bold'), width=10, height=1, bd=4,command=iexit)
        self.btnexit.grid(row=0, column=6)



if __name__=='__main__':
    global root
    root=Tk()
    application=Student(root)
    root.mainloop()