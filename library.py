from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1560x1560+0+0")

    #==============================================VARIABLE===================================================================
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.Id_var=StringVar()
        self.firstname_var=StringVar()
        self.middlename_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.mobilenumber_var=StringVar()
        self.bookid_var=StringVar()
        self.title_var=StringVar()
        self.author_var=StringVar()
        self.price_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.latereturn_var=StringVar()
        self.overdue_var=StringVar()
      




        #creating label widget with specified font, bg anf fg colors.
        lbltitle=Label(self.root,text='LIBRARY MANGEMENT SYSTEM ',bg='powder blue',fg='red',bd=12,relief=RIDGE,font=('arial',50,'bold'),padx=2,pady=6)
        #placing the label at the top of the window and makes it stretch horizontally.
        lbltitle.pack(side=TOP,fill=X)
        
        #creates a frame widget(below title label) with given specifications
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
        #positions the frame atgiven coordinates
        frame.place(x=0,y=110,width=1560 ,height=420)
        
#===================================================================================DataFrameLeft================================================================
        #creating a LabelFrame on left side inside the main frame 
        DataFrameLeft=LabelFrame(frame,text='Library Membership Information',bg='powder blue',fg='green',bd=12,relief=RIDGE,font=('arial',25,'bold'),padx=2,pady=6)
        # positions the LabelFrame at given coordinates
        DataFrameLeft.place(x=0,y=5,width=940,height=380)
             

             #=================adding Member label widget in the parent widget DataFrameLeft================================
        lblMember=Label(DataFrameLeft,bg='powder blue',text='MEMBER TYPE',font=('arial',12,'bold'),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
         
             #=================creating combobox widget(or dropdown menu) in parent widget at specified location in grid================================
        comMember=ttk.Combobox(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.member_var,width=27,state='readonly')
        #selected value from dropdown is stored in a variable self.member_var and can be used elswhere in the code
        comMember['value']=('Admin Staff','Student','Lecturer')
        comMember.grid(row=0,column=1)

             #==============adding PRN column==============================
        lblPRN=Label(DataFrameLeft,bg='powder blue',text='PRN NO',font=('arial',12,'bold'),padx=2,pady=6)
        lblPRN.grid(row=1,column=0,sticky=W)

             #===================adding PRN written option====================
        txtPRN=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.prn_var,width=29)
        txtPRN.grid(row=1,column=1)

            #==================adding ID NO column==============================
        lblID=Label(DataFrameLeft,bg='powder blue',text='ID NUMBER',font=('arial',12,'bold'),padx=2,pady=6)
        lblID.grid(row=2,column=0,sticky=W)


            #==================adding ID NO written option====================
        txtID=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.Id_var,width=29)
        txtID.grid(row=2,column=1)


            #==========adding First Name Column====================
        lblFirst=Label(DataFrameLeft,bg='powder blue',text='FIRST NAME',font=('arial',12,'bold'),padx=2,pady=6)
        lblFirst.grid(row=3,column=0,sticky=W)
            
            #==================adding First Nmae written option====================
        txtFirst=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.firstname_var,width=29)
        txtFirst.grid(row=3,column=1)



             #==========adding Middle Name Column====================
        lblmiddle=Label(DataFrameLeft,bg='powder blue',text='MIDDLE NAME',font=('arial',12,'bold'),padx=2,pady=6)
        lblmiddle.grid(row=4,column=0,sticky=W)


            #==================adding Middle Nmae written option====================
        txtmiddle=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.middlename_var,width=29)
        txtmiddle.grid(row=4,column=1)

              #==========adding Last Name Column====================
        lbllast=Label(DataFrameLeft,bg='powder blue',text='LAST NAME',font=('arial',12,'bold'),padx=2,pady=6)
        lbllast.grid(row=5,column=0,sticky=W)


           #==================adding Last Nmae written option====================
        txtlast=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.lastname_var,width=29)
        txtlast.grid(row=5,column=1)


            #==========adding Address Column====================
        lbladdress=Label(DataFrameLeft,bg='powder blue',text='ADDRESS',font=('arial',12,'bold'),padx=2,pady=6)
        lbladdress.grid(row=6,column=0,sticky=W)


           #==================adding Address written option====================
        txtaddress=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.address_var,width=29)
        txtaddress.grid(row=6,column=1)
        
        

        #==========adding Mobile Number Column====================
        lblmobile=Label(DataFrameLeft,bg='powder blue',text='MOBILE NUMBER',font=('arial',12,'bold'),padx=2,pady=6)
        lblmobile.grid(row=7,column=0,sticky=W)


           #==================adding Mobile Number  written option====================
        txtmobile=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.mobilenumber_var,width=29)
        txtmobile.grid(row=7,column=1)


         #==========adding Book Id Column====================
        lblbookid=Label(DataFrameLeft,bg='powder blue',text='BOOK ID',font=('arial',12,'bold'),padx=2,pady=6)
        lblbookid.grid(row=0,column=2,sticky=W)


           #==================adding Book Id written option====================
        txtbookid=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.bookid_var,width=27)
        txtbookid.grid(row=0,column=3)


            #==========adding Book Title Column====================
        lblbooktitle=Label(DataFrameLeft,bg='powder blue',text='BOOK TITLE',font=('arial',12,'bold'),padx=2,pady=6)
        lblbooktitle.grid(row=1,column=2,sticky=W)


           #==================adding Book Title  written option====================
        txtbooktitle=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.title_var,width=27)
        txtbooktitle.grid(row=1,column=3)


           #==========adding Author Column====================
        lblauthor=Label(DataFrameLeft,bg='powder blue',text='BOOK AUTHOR',font=('arial',12,'bold'),padx=2,pady=6)
        lblauthor.grid(row=2,column=2,sticky=W)


           #==================adding Author written option====================
        txtauthor=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.author_var,width=27)
        txtauthor.grid(row=2,column=3)

        #==========adding Actual Price  Column==================== 
        lblprice=Label(DataFrameLeft,bg='powder blue',text='ACTUAL PRICE',font=('arial',12,'bold'),padx=2,pady=6)
        lblprice.grid(row=3,column=2,sticky=W)


           #==================adding Actual Price  written option====================
        txtprice=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.price_var,width=27)
        txtprice.grid(row=3,column=3)

        #==========adding Date Borrowed Column====================
        lbldatebr=Label(DataFrameLeft,bg='powder blue',text='Date Borrowed',font=('arial',12,'bold'),padx=2,pady=6)
        lbldatebr.grid(row=4,column=2,sticky=W)


           #==================adding Date Borrowed written option====================
        txtdatebr=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.dateborrowed_var,width=27)
        txtdatebr.grid(row=4,column=3)


        #==========adding Date Due  Column====================
        lbldatedue=Label(DataFrameLeft,bg='powder blue',text='DATE DUE',font=('arial',12,'bold'),padx=2,pady=6)
        lbldatedue.grid(row=5,column=2,sticky=W)


           #==================adding Date Due written option====================
        txtdatedue=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.datedue_var,width=27)
        txtdatedue.grid(row=5,column=3)
          

          #==========adding Late Return Fine Column====================
        lblreturn=Label(DataFrameLeft,bg='powder blue',text='Late Return Fine',font=('arial',12,'bold'),padx=2,pady=6)
        lblreturn.grid(row=6,column=2,sticky=W)


           #==================adding Late Return Fine written option====================
        txtreturn=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.latereturn_var,width=27)
        txtreturn.grid(row=6,column=3)

            #==========adding Date Over Due Column====================
        lbldateover=Label(DataFrameLeft,bg='powder blue',text='Date Over Due',font=('arial',12,'bold'),padx=2,pady=6)
        lbldateover.grid(row=7,column=2,sticky=W)


           #==================adding Date over due written option====================
        txtdateover=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.overdue_var,width=27)
        txtdateover.grid(row=7,column=3)







#===============================================================================DataFrameRight==================================================================
        DataFrameRight=LabelFrame(frame,text='Book Information',bg='powder blue',fg='green',bd=12,relief=RIDGE,font=('arial',25,'bold'),padx=2, pady=6)
        DataFrameRight.place(x=970,y=5,width=500,height=380)


         # Horizontal Scrollbar setup for Text widget
        textScrollbar = Scrollbar(DataFrameRight)
        # textScrollbar.grid(row=1, column=2, sticky='ew')
        

        # self.txtBox=Text(DataFrameRight,font=('arial',12,'bold'),width= 32,height=20 ,padx=0,pady=0)
        # self.txtBox.grid(row=0,column=2)
        self.txtBox = Text(DataFrameRight, font=('arial', 12, 'bold'), width=30, height=15,wrap='none', xscrollcommand=textScrollbar.set)
        self.txtBox.grid(row=0, column=2, padx=2, pady=6, sticky='ns')

         # Connect horizontal scrollbar to Text widget
        textScrollbar.config(command=self.txtBox.xview)


        
        #===========creating scrollbar=======================
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky='ns')
        
        #==============creating list of books========================
        listbooks=["To Kill a Mockingbird","Python","1984 by George Orwell","The Great Gatsby by F. Scott Fitzgerald","The Lord of the Rings by J.R.R. Tolkien",
                   "Harry Potter and the Philosopher's Stone by J.K. Rowling","The Catcher in the Rye by J.D. Salinger","The Chronicles of Narnia by C.S. Lewis","The Hitchhiker's Guide to the Galaxy by Douglas Adams","The Da Vinci Code by Dan Brown",
                   "The Alchemist by Paulo Coelho","To Kill a Kingdom by Alexandra Christo","Gone Girl by Gillian Flynn","The Girl on the Train by Paula Hawkins","The Hunger Games by Suzanne Collins","The Handmaid's Tale by Margaret Atwood",
                   "A Game of Thrones by George R.R. Martin","The Hobbit by J.R.R. Tolkien","The Kite Runner by Khaled Hosseini","The Fault in Our Stars by John Green"]

        
        def selectbook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="To Kill a Mockingbird"):
                self.bookid_var.set("BKID5454")
                self.title_var.set("To Kill a Mockingbird")
                self.author_var.set('Harper Lee')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.50.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.785.00")
            elif(x=="Python"):
                self.bookid_var.set("BKID8937")
                self.title_var.set("Python")
                self.author_var.set('HerryPoter')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.50.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.585.00")
            elif(x=="1984 by George Orwell"):
                self.bookid_var.set("BKID5678")
                self.title_var.set("1984 by George Orwell")
                self.author_var.set('George Orwell')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.40.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.620.00")
            # elif(x=="Pride and Prejudice by Jane Austen"):
            #     self.bookid_var.set("BKID9101")
            #     self.title_var.set("Pride and Prejudice by Jane Austen")
            #     self.author_var.set('Jane Austen')
            #     d1=datetime.datetime.today()
            #     d2=datetime.timedelta(days=15)  
            #     d3=d1+d2
            #     self.dateborrowed_var.set(d1)
            #     self.datedue_var.set(d3)
            #     self.latereturn_var.set('Rs.30.00')
            #     self.overdue_var.set("No")
            #     self.price_var.set("Rs.450.00")
            elif(x=="The Great Gatsby by F. Scott Fitzgerald"):
                self.bookid_var.set("BKID1121")
                self.title_var.set("The Great Gatsby by F. Scott Fitzgerald")
                self.author_var.set('F. Scott Fitzgerald')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.35.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.500.00")
            elif(x=="The Lord of the Rings by J.R.R. Tolkien"):
                self.bookid_var.set("BKID1314")
                self.title_var.set("The Lord of the Rings by J.R.R. Tolkien")
                self.author_var.set('J.R.R. Tolkien')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.45.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.850.00")
            elif(x=="Harry Potter and the Philosopher's Stone by J.K. Rowling"):
                self.bookid_var.set("BKID1516")
                self.title_var.set("Harry Potter and the Philosopher's Stone by J.K. Rowling")
                self.author_var.set('J.K. Rowling')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.50.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.900.00")
            elif(x=="The Catcher in the Rye by J.D. Salinger"):
                self.bookid_var.set("BKID1718")
                self.title_var.set("The Catcher in the Rye by J.D. Salinger")
                self.author_var.set('J.D. Salinger')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.20.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.475.00")
            elif(x=="The Chronicles of Narnia by C.S. Lewis"):
                self.bookid_var.set("BKID1920")
                self.title_var.set("The Chronicles of Narnia by C.S. Lewis")
                self.author_var.set('C.S. Lewis')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.60.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.1100.00")
            elif(x=="The Hitchhiker's Guide to the Galaxy by Douglas Adams"):
                self.bookid_var.set("BKID2122")
                self.title_var.set("The Hitchhiker's Guide to the Galaxy by Douglas Adams")
                self.author_var.set('Douglas Adams')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.25.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.650.00")
            elif(x=="The Da Vinci Code by Dan Brown"):
                self.bookid_var.set("BKID2324")
                self.title_var.set("The Da Vinci Code by Dan Brown")
                self.author_var.set('Dan Brown')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.55.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.780.00")
            elif(x=="The Alchemist by Paulo Coelho"):
                self.bookid_var.set("BKID2526")
                self.title_var.set("The Alchemist by Paulo Coelho")
                self.author_var.set('Paulo Coelho')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.35.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.520.00")
            elif(x=="To Kill a Kingdom by Alexandra Christo"):
                self.bookid_var.set("BKID2728")
                self.title_var.set("To Kill a Kingdom by Alexandra Christo")
                self.author_var.set('Alexandra Christo')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.40.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.670.00")
            elif(x=="Gone Girl by Gillian Flynn"):
                self.bookid_var.set("BKID2930")
                self.title_var.set("Gone Girl by Gillian Flynn")
                self.author_var.set('Gillian Flynn')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.50.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.750.00")
            elif(x=="The Girl on the Train by Paula Hawkins"):
                self.bookid_var.set("BKID3132")
                self.title_var.set("The Girl on the Train by Paula Hawkins")
                self.author_var.set('Paula Hawkins')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.45.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.730.00")
            elif(x=="The Hunger Games by Suzanne Collins"):
                self.bookid_var.set("BKID3334")
                self.title_var.set("The Hunger Games by Suzanne Collins")
                self.author_var.set('Suzanne Collins')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.50.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.670.00")
            elif(x=="The Handmaid's Tale by Margaret Atwood"):
                self.bookid_var.set("BKID3536")
                self.title_var.set("The Handmaid's Tale by Margaret Atwood")
                self.author_var.set('Margaret Atwood')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.45.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.700.00")
            elif(x=="A Game of Thrones by George R.R. Martin"):
                self.bookid_var.set("BKID3738")
                self.title_var.set("A Game of Thrones by George R.R. Martin")
                self.author_var.set('George R.R. Martin')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.60.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.950.00")
            elif(x=="The Hobbit by J.R.R. Tolkien"):
                self.bookid_var.set("BKID3940")
                self.title_var.set("The Hobbit by J.R.R. Tolkien")
                self.author_var.set('J.R.R. Tolkien')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.40.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.600.00")
            elif(x=="The Kite Runner by Khaled Hosseini"):
                self.bookid_var.set("BKID4142")
                self.title_var.set("The Kite Runner by Khaled Hosseini")
                self.author_var.set('Khaled Hosseini')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.35.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.720.00")
            elif(x=="The Fault in Our Stars by John Green"):
                self.bookid_var.set("BKID4344")
                self.title_var.set("The Fault in Our Stars by John Green")
                self.author_var.set('John Green')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturn_var.set('Rs.30.00')
                self.overdue_var.set("No")
                self.price_var.set("Rs.550.00")















        listbox = Listbox(DataFrameRight, font=('arial', 12, 'bold'), width=20, height=15)
        listbox.grid(row=0, column=0, padx=2, pady=6, sticky='ns')

        # Connect scrollbar to listbox
        listbox.config(yscrollcommand=listScrollbar.set)
        listScrollbar.config(command=listbox.yview)


   




        # listbox=Listbox(DataFrameRight,font=('arial',12,'bold'),width= 20,height=20)
        listbox.bind("<<ListboxSelect>>",selectbook)
        # listbox.grid(row=0,column=0,padx=0)
        # listScrollbar.config(command=listbox.yview)
       
     


        #=========adding books in scroll bar==============
        for item in listbooks:
            listbox.insert(END,item)






       
#==============================================================================Buttons Frame============================================================================
        Buttonframe=Frame(self.root, bd=12, relief=RIDGE, padx=100, bg="powder blue") 
        Buttonframe.place(x=0,y=530, width=1530,height=70)
        #================create Add Button===================
        btnAddData=Button(Buttonframe,command=self.add_data,text='Add Data',font=('arial',12,'bold'),width= 20,bg='blue',fg='white')
        btnAddData.grid(row=0,column=0)


        #================create show Button===================
        btnAddData=Button(Buttonframe,command=self.showData,text='Show Data',font=('arial',12,'bold'),width= 20,bg='blue',fg='white')
        btnAddData.grid(row=0,column=1)
        

        #================create update Button===================
        btnAddData=Button(Buttonframe,command=self.update,text='Update',font=('arial',12,'bold'),width= 20,bg='blue',fg='white')
        btnAddData.grid(row=0,column=2)


        #================create Delete Button===================
        btnAddData=Button(Buttonframe,command=self.delete,text='Delete',font=('arial',12,'bold'),width= 20,bg='blue',fg='white')
        btnAddData.grid(row=0,column=3)

        #================create Reset Button===================
        btnAddData=Button(Buttonframe,command=self.resetData,text='Reset',font=('arial',12,'bold'),width= 20,bg='blue',fg='white')
        btnAddData.grid(row=0,column=4)

        #================create Exit Button===================
        btnAddData=Button(Buttonframe,command=self.Exit,text='Exit',font=('arial',12,'bold'),width= 20,bg='blue',fg='white')
        btnAddData.grid(row=0,column=5)


#=========================================================================Information Frame==================================================================
        infoframe=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
        infoframe.place(x=0,y=610,width=1560 ,height=170)


        Table_frame=Frame(infoframe,bd=12,relief=RIDGE,bg='powder blue')
        Table_frame.place(x=0,y=2,width=1470 ,height=140)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=('member type','prn no','id no','first name','middle name',
                                                           'last name','address','mobile number','book id','book title','book author','actual price',
                                                               'date borrowed','date due','late return','date over due'    ),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)#Packs the horizontal scrollbar at the bottom of Table_frame and makes it fill the horizontal space.
        yscroll.pack(side=RIGHT,fill=Y)


        xscroll.config(command=self.library_table.xview) #Links the horizontal & vertical scrollbar to the Treeview.
        yscroll.config(command=self.library_table.yview)

    
        self.library_table.heading('member type',text='Member Type')
        self.library_table.heading('prn no',text='PRN NO')
        self.library_table.heading('id no',text='ID NO')
        self.library_table.heading('first name',text='FIRST NAME')
        self.library_table.heading('middle name',text='MIDDLE NAME')
        self.library_table.heading('last name',text='LAST NAME')
        self.library_table.heading('mobile number',text='MOBILE NUBER')
        self.library_table.heading('address',text='ADDRESS')
        self.library_table.heading('book id',text='BOOK ID')
        self.library_table.heading('book title',text='BOOK TITLE')
        self.library_table.heading('book author',text='BOOK AUTHOR')
        self.library_table.heading('actual price',text='ACTUAL PRICE')
        self.library_table.heading('date borrowed',text='DATE BORROWED')
        self.library_table.heading('date due',text='DATE DUE')
        self.library_table.heading('late return',text='LATE RETURN')
        self.library_table.heading('date over due',text='DATE OVER DUE')
       


        self.library_table['show']='headings'# Configures the Treeview to display the column headings.
        self.library_table.pack(fill=BOTH,expand=1)#Packs the Treeview into Table_frame.
          
        self.library_table.column('member type',width=100)
        self.library_table.column('prn no',width=100)
        self.library_table.column('id no',width=100)
        self.library_table.column('first name',width=100)
        self.library_table.column('middle name',width=100)
        self.library_table.column('last name',width=100)
        self.library_table.column('mobile number',width=100)
        self.library_table.column('address',width=100)
        self.library_table.column('book id',width=100)
        self.library_table.column('book title',width=100)
        self.library_table.column('book author',width=100)
        self.library_table.column('actual price',width=100)
        self.library_table.column('date borrowed',width=110)
        self.library_table.column('date due',width=100)
        self.library_table.column('late return',width=100)
        self.library_table.column('date over due',width=100)   
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host='127.0.0.1',username='root',password='pr.0123456',database='temp')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              self.member_var.get(),
                                                                                                              self.prn_var.get(),
                                                                                                              self.Id_var.get(),
                                                                                                              self.firstname_var.get(),
                                                                                                              self.middlename_var.get(),
                                                                                                              self.lastname_var.get(),
                                                                                                              self.address_var.get(),
                                                                                                              self.mobilenumber_var.get(),
                                                                                                              self.bookid_var.get(),
                                                                                                              self.title_var.get(),
                                                                                                              self.author_var.get(),
                                                                                                              self.price_var.get(),
                                                                                                              self.dateborrowed_var.get(),
                                                                                                              self.datedue_var.get(),
                                                                                                              self.latereturn_var.get(),
                                                                                                              self.overdue_var.get(),
                                                                                                            ))
        
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")



    def update(self):
        conn=mysql.connector.connect(host='127.0.0.1',username='root',password='pr.0123456',database='temp')
        my_cursor=conn.cursor()
        # my_cursor.execute("update library set MemberType=%s,IDNumber=%s,FirstName=%s,MiddleName=%s,LastName=%s,Address=%s,MobileNumber=%s,BookId=%s,BookTitle=%s,BookAuthor=%s,ActualPrice=%s,DateBorrowed=%s,DateDue=%s,LateReturnFine=%s,DateOverDue=%s Where PRN_No=%s",(
        #                                                                                                       self.member_var.get(),
        #                                                                                                       self.Id_var.get(),
        #                                                                                                       self.firstname_var.get(),
        #                                                                                                       self.middlename_var.get(),
        #                                                                                                       self.lastname_var.get(),
        #                                                                                                       self.address_var.get(),
        #                                                                                                       self.mobilenumber_var.get(),
        #                                                                                                       self.bookid_var.get(),
        #                                                                                                       self.title_var.get(),
        #                                                                                                       self.author_var.get(),
        #                                                                                                       self.price_var.get(),
        #                                                                                                       self.dateborrowed_var.get(),
        #                                                                                                       self.datedue_var.get(),
        #                                                                                                       self.latereturn_var.get(),
        #                                                                                                       self.overdue_var.get(),
        #                                                                                                       self.prn_var.get(),
        #                                                                                                     ))
        
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,MiddleName=%s,LastName=%s,Address=%s,MobileNumber=%s,BookId=%s,Title=%s,Author=%s,Price=%s,DateBorrowed=%s,DateDue=%s,LateReturn=%s,OverDue=%s Where PRN_No=%s",(
                                                                                                              self.member_var.get(),
                                                                                                              self.Id_var.get(),
                                                                                                              self.firstname_var.get(),
                                                                                                              self.middlename_var.get(),
                                                                                                              self.lastname_var.get(),
                                                                                                              self.address_var.get(),
                                                                                                              self.mobilenumber_var.get(),
                                                                                                              self.bookid_var.get(),
                                                                                                              self.title_var.get(),
                                                                                                              self.author_var.get(),
                                                                                                              self.price_var.get(),
                                                                                                              self.dateborrowed_var.get(),
                                                                                                              self.datedue_var.get(),
                                                                                                              self.latereturn_var.get(),
                                                                                                              self.overdue_var.get(),
                                                                                                              self.prn_var.get(),
                                                                                                            ))
        
        
        
        conn.commit()
        self.fetch_data() 
        
        conn.close()

        messagebox.showinfo("Success","Member has been updated successfully")






    def fetch_data(self):
           conn=mysql.connector.connect(host='127.0.0.1',username='root',password='pr.0123456',database='temp')
           my_cursor=conn.cursor()
           my_cursor.execute("select * from  library")
           row=my_cursor.fetchall()

           if len(row) != 0:
               self.library_table.delete(*self.library_table.get_children())
               for i in row:
                   self.library_table.insert("",END,values=i)
               conn.commit()
           conn.close()

    #============================================add cursor to show all data===========================================

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']


        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.Id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.middlename_var.set(row[4]),
        self.lastname_var.set(row[5]),
        self.address_var.set(row[6]),
        self.mobilenumber_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.title_var.set(row[9]),
        self.author_var.set(row[10]),
        self.price_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.latereturn_var.set(row[14]),
        self.overdue_var.set(row[15]),
    
    ##==================================define show function=========================================
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")          
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"Member ID\t\t"+self.Id_var.get()+"\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Middle Name\t\t"+self.middlename_var.get()+"\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address\t\t"+self.address_var.get()+"\n")
        self.txtBox.insert(END,"Mobile Number\t\t"+self.mobilenumber_var.get()+"\n")
        self.txtBox.insert(END,"Book Id\t\t"+self.bookid_var.get()+"\n")                                 
        self.txtBox.insert(END,"Title\t\t"+self.title_var.get()+"\n")
        self.txtBox.insert(END,"Author\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"Price\t\t"+self.price_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date due\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Late fee\t\t"+self.latereturn_var.get()+"\n")
        self.txtBox.insert(END, "Date Over due\t\t"+self.overdue_var.get()+"\n")  
       
    def  resetData(self):
             
        self.member_var.set(""),
        self.Id_var.set(""),
        self.firstname_var.set(""),
        self.middlename_var.set(""),
        self.prn_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.mobilenumber_var.set(""),
        self.bookid_var.set(""),
        self.title_var.set(""),
        self.author_var.set(""),
        self.price_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.latereturn_var.set(""),
        self.overdue_var.set(""),
        self.txtBox.delete("1.0",END)                  

    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Library Mangement System","Do you want to exit")
        if Exit>0:
            self.root.destroy()
            return                        
                            
                            
    def delete(self):
        if self.prn_var.get()=="" or self.Id_var.get()=="" :
            messagebox.showerror("Error","First select the member.") 
        else:
           conn=mysql.connector.connect(host='127.0.0.1',username='root',password='pr.0123456',database='temp')
           my_cursor=conn.cursor()
           query="delete from  library where PRN_No=%s"
           value=(self.prn_var.get(),)
           my_cursor.execute(query,value)


           conn.commit()
           self.fetch_data()
          
           conn.close()
           
           messagebox.showinfo("Success","Member has been deleted successfully")






                                                                                                                                                   




if __name__ == '__main__': #ensures that the following code runs only if the script is executed directly (not imported as a module).
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()  #window doesnot closes instantly after opening due to this line




