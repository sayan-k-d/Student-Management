from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from Student import *
class ConnectorDB:
    def __init__(self,root):
        self.root=root
        tspace=" "
        self.root.title(100 * tspace + "DATABASE PROJECT")
        self.root.geometry("804x645+300+0")
        self.root.resizable(width=False, height=False)
        mainframe=Frame(self.root,bd=10,width=776,height=700,bg="#F16A57", relief=RIDGE)
        mainframe.grid()

        TitleFrame = Frame(mainframe, bd=7, width=776, height=100, relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        Topframe3 = Frame(mainframe, bd=5, width=776, height=500, relief=RIDGE)
        Topframe3.grid(row=1,column=0)

        Leftframe = Frame(Topframe3, bd=5, width=776, height=400, bg="#F16A57",padx=2, relief=RIDGE)
        Leftframe.pack(side=LEFT)
        Leftframe1 = Frame(Leftframe, bd=5, width=500, height=200, padx=12, pady=4, relief=RIDGE)
        Leftframe1.pack(side=TOP, padx=0, pady=0)
        Leftframe1a = Frame(Leftframe, bd=5, width=600, height=200, padx=12,pady=4, relief=RIDGE)
        Leftframe1a.pack(side=TOP,padx=0,pady=0)

        Rightframe = Frame(Topframe3, bd=5, width=100, height=400, bg="#F16A57", relief=RIDGE)
        Rightframe.pack(side=RIGHT)
        Rightframe1 = Frame(Rightframe, bd=5, width=90, height=300,padx=2,pady=2, relief=RIDGE)
        Rightframe1.pack(side=TOP)
        #====================================         Variables          ===============================================

        StudentId=StringVar()
        Name=StringVar()
        Phone=StringVar()
        Email=StringVar()
        Password=StringVar()

        #=====================================        Methods       ====================================================


        def enable(childList):
            for child in childList:
                child.configure(state='normal')

        def disable(childList):
            for child in childList:
                child.configure(state='disable')

        def dbExit():
            dbexit= askyesno("Database Connection","Confirm if You Want to Exit")
            if dbexit > 0:
                self.root.destroy()
                return

        def Reset():
            enable(Leftframe1.winfo_children())
            self.enstudentid.delete(0,END)
            disable(Leftframe1.winfo_children())
            self.enstudentname.delete(0, END)
            self.enphone.delete(0, END)
            self.enemail.delete(0, END)
            self.enpassword.delete(0, END)

        def AddNew():
            if Name.get()=="" or Phone.get()=="" or Email.get()=="":
                showerror("Database Connection","Enter Correct Details")
            else:
                users=obj.addone(Name.get(),Phone.get(),Email.get(),Password.get())
                if users != 0:
                    showinfo("Database Connection","Record Added Successfully")

        def DisplayData():
            result=obj.findall()
            if len(result) != 0:
                self.records.delete(*self.records.get_children())
                for row in result:
                    self.records.insert('',END,values=row)

        def info(event):
            try:
                viewinfo= self.records.focus()
                data=self.records.item(viewinfo)
                row=data['values']
                StudentId.set(row[0]),
                Name.set(row[1]),
                Phone.set(row[2]),
                Email.set(row[3]),
                Password.set(row[4])
            except Exception:
                return


        def Update():
            if Name.get()=="" or Phone.get()=="" or Email.get()=="":
                showerror("Database Connection","Enter Correct Details")

            else:
                users=obj.updateuser(Name.get(),Phone.get(),Email.get(),Password.get(),int(StudentId.get()))
                if users != 0:
                    DisplayData()
                    showinfo("Database Connection","Record Updated Successfully")

        def Delete():
            if Name.get()=="" or Phone.get()=="" or Email.get()=="":
                showerror("Database Connection","Enter Correct Details")
            else:
                users=obj.deluser(StudentId.get())
                if users !=0 :
                    showinfo("Database Connection","Record Deleted Successfully")
                    Reset()

        def searchDB():
            Reset()
            enable(Leftframe1.winfo_children())
            disable(Leftframe1a.winfo_children())
        def findDB():
            try:
                if StudentId.get() == "":
                    showerror("Database Connection", "Enter Correct Details")
                else:
                    users=obj.findone(StudentId.get())
                    enable(Leftframe1a.winfo_children())
                    disable(Leftframe1.winfo_children())
                    if users != 0:
                        Name.set(users[1]),
                        Phone.set(users[2]),
                        Email.set(users[3]),
                        Password.set(users[4])
            except:
                Reset()
                showwarning("Database Connection","No Such Record Found")

        #===================================      Labels & Entry       =================================================

        self.lbltitle=Label(TitleFrame,font=('consolas',35,'bold'),text="DATABASE CONNECTION",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=130)

        self.studentid = Label(Leftframe1, font=('consolas', 12, 'bold'), text="Student ID", bd=7)
        self.studentid.grid(row=0,column=0, sticky=W,padx=5)
        self.enstudentid = Entry(Leftframe1, font=('consolas', 12, 'bold'), bd=5, width=30, justify='left',textvariable=StudentId)
        self.enstudentid.grid(row=0,column=1, sticky=W,padx=5)
        self.findBtn = Button(Leftframe1, font=('consolas', 12, 'bold'), text="Find", bd=4, width=8,padx=20,command=findDB)
        self.findBtn.grid(row=0, column=2,padx=2)
        for child in Leftframe1.winfo_children():
            child.configure(state='disable')

        self.studentname = Label(Leftframe1a, font=('consolas',12, 'bold'), text="Name ", bd=7)
        self.studentname.grid(row=1, column=0,sticky=W,padx=5)
        self.enstudentname = Entry(Leftframe1a, font=('consolas', 12, 'bold'), bd=5,width=46,justify='left',textvariable=Name)
        self.enstudentname.grid(row=1, column=1, sticky=W, padx=5)

        self.phone = Label(Leftframe1a, font=('consolas', 12, 'bold'), text="Phone", bd=7)
        self.phone.grid(row=2, column=0, sticky=W, padx=5)
        self.enphone = Entry(Leftframe1a, font=('consolas', 12, 'bold'), bd=5, width=46, justify='left',textvariable=Phone)
        self.enphone.grid(row=2, column=1, sticky=W, padx=5)

        self.email = Label(Leftframe1a, font=('consolas', 12, 'bold'), text="Email", bd=7)
        self.email.grid(row=3, column=0, sticky=W, padx=5)
        self.enemail = Entry(Leftframe1a, font=('consolas', 12, 'bold'), bd=5, width=46, justify='left',textvariable=Email)
        self.enemail.grid(row=3, column=1, sticky=W, padx=5)

        self.password = Label(Leftframe1a, font=('consolas', 12, 'bold'), text="Password", bd=7)
        self.password.grid(row=4, column=0, sticky=W, padx=5)
        self.enpassword = Entry(Leftframe1a, font=('consolas', 12, 'bold'), bd=5, width=46, justify='left',show='*',textvariable=Password)
        self.enpassword.grid(row=4, column=1, sticky=W, padx=5)

        for child in Leftframe1a.winfo_children():
            child.configure(state='normal')
        #======================================      Tables View        ================================================

        scroll_Y=Scrollbar(Leftframe,orient=VERTICAL)
        self.records=ttk.Treeview(Leftframe,height=14,columns=("StudentID","Name","Phone","Email"),yscrollcommand=scroll_Y.set)
        scroll_Y.pack(side=RIGHT,fill=Y)


        self.records.heading("StudentID",text="Student ID")
        self.records.heading("Name", text="Name")
        self.records.heading("Phone", text="Phone")
        self.records.heading("Email", text="Email")

        self.records['show']="headings"

        self.records.column("StudentID", width=70)
        self.records.column("Name", width=100)
        self.records.column("Phone", width=100)
        self.records.column("Email", width=100)
        self.records.pack(fill=BOTH,expand=1)

        self.records.bind("<ButtonRelease-1>",info)

        # ======================================        Buttons        =================================================

        self.addnewBtn=Button(Rightframe1,font=('consolas', 16, 'bold'), text="Add New", bd=4,width=8,height=2,padx=24,command=AddNew)
        self.addnewBtn.grid(row=0,column=0,padx=1)

        self.displayBtn = Button(Rightframe1, font=('consolas', 16, 'bold'), text="Display", bd=4, width=8, height=2,
                                padx=24,pady=2,command=DisplayData)
        self.displayBtn.grid(row=1, column=0, padx=1)

        self.searchBtn = Button(Rightframe1, font=('consolas', 16, 'bold'), text="Search", bd=4, width=8, height=2,
                                padx=24,pady=2,command=searchDB)
        self.searchBtn.grid(row=2, column=0, padx=1)

        self.updateBtn = Button(Rightframe1, font=('consolas', 16, 'bold'), text="Update", bd=4, width=8, height=2,
                                padx=24,pady=2,command=Update)
        self.updateBtn.grid(row=3, column=0, padx=1)

        self.deleteBtn = Button(Rightframe1, font=('consolas', 16, 'bold'), text="Delete", bd=4, width=8, height=2,
                                padx=24, pady=2,command=Delete)
        self.deleteBtn.grid(row=4, column=0, padx=1)

        self.resetBtn = Button(Rightframe1, font=('consolas', 16, 'bold'), text="Reset", bd=4, width=8, height=2,
                                padx=24,pady=2,command=Reset)
        self.resetBtn.grid(row=5, column=0, padx=1)

        self.exitBtn = Button(Rightframe1, font=('consolas', 16, 'bold'), text="Exit", bd=4, width=8, height=2,
                                padx=24,pady=2,command=dbExit)
        self.exitBtn.grid(row=6, column=0, padx=1)




if __name__ == '__main__':
    obj=Student()
    root=Tk()
    mainscreen=ConnectorDB(root)
    root.mainloop()
