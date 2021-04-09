from tkinter import *
from tkinter import Frame
import pymysql
from tkinter import ttk


class NTHStudentsData:
    def __init__(self, root):
        self.root = root
        self.root.title('NTH Students Data')
        self.root.geometry('1400x700')
        title = Label(self.root, text='NTH Students Data', bd=4, relief=GROOVE,
                      bg='green', fg='white', font=('times new roman', 20, 'bold'))
        title.pack(fill=X)
        self.roll_no_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.coursename_var = StringVar()
        self.fee_var = StringVar()
        self.contactnum_var = StringVar()
        self.emailid_var = StringVar()
        self.Trainer_var = StringVar()
        self.startdate_var = StringVar()
        self.gender_var = StringVar()
        self.searchby = StringVar()
        self.search = StringVar()


        # ---------Dataentry frame-----------

        DataEntryFrame = Frame(self.root, bg='green', bd=4, relief=GROOVE)
        DataEntryFrame.place(x=10, y=60, height=570, width=350)
        title = Label(DataEntryFrame, text='Students Data Entry Form', bg='green', fg='white',
                      font=('times new roman', 18, 'bold'))
        title.grid(row=0, columnspan=2, padx=40, pady=10)
        roll_no = Label(DataEntryFrame, text='Roll No:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        roll_no.grid(row=1, column=0, pady=3, sticky='W')
        roll_no = Entry(DataEntryFrame, textvariable=self.roll_no_var, font=('times new roman', 12, 'bold'))
        roll_no.grid(row=1, pady=3, column=1)
        firstname = Label(DataEntryFrame, text='FirstName:', bg='green', fg='white',
                          font=('times new roman', 15, 'bold'))
        firstname.grid(row=2, column=0, pady=3, sticky='W')
        firstname = Entry(DataEntryFrame, textvariable=self.firstname_var, font=('times new roman', 12, 'bold'))
        firstname.grid(row=2, pady=3, column=1)
        lastname = Label(DataEntryFrame, text='LastName:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        lastname.grid(row=3, column=0, pady=3, sticky='W')
        lastname = Entry(DataEntryFrame, textvariable=self.lastname_var, font=('times new roman', 12, 'bold'))
        lastname.grid(row=3, pady=3, column=1)
        coursename = Label(DataEntryFrame, text='CourseName:', bg='green', fg='white',
                           font=('times new roman', 15, 'bold'))
        coursename.grid(row=4, column=0, pady=3, sticky='W')
        coursename = Entry(DataEntryFrame, textvariable=self.coursename_var, font=('times new roman', 12, 'bold'))
        coursename.grid(row=4, pady=3, column=1)
        fee = Label(DataEntryFrame, text='Fee:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        fee.grid(row=5, column=0, pady=3, sticky='W')
        fee = Entry(DataEntryFrame, textvariable=self.fee_var, font=('times new roman', 12, 'bold'))
        fee.grid(row=5, pady=3, column=1)
        contactnum = Label(DataEntryFrame, text='Contact Num:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        contactnum.grid(row=6, column=0, pady=3, sticky='W')
        contactnum = Entry(DataEntryFrame, textvariable=self.contactnum_var, font=('times new roman', 12, 'bold'))
        contactnum.grid(row=6, pady=3, column=1)
        emailid = Label(DataEntryFrame, text='Email ID:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        emailid.grid(row=7, column=0, pady=3, sticky='W')
        emailid = Entry(DataEntryFrame, textvariable=self.emailid_var, font=('times new roman', 12, 'bold'))
        emailid.grid(row=7, column=1, pady=3)
        Trainer = Label(DataEntryFrame, text='Trainer:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        Trainer.grid(row=8, column=0, pady=3, sticky='W')
        Trainer = Entry(DataEntryFrame, textvariable=self.Trainer_var, font=('times new roman', 12, 'bold'))
        Trainer.grid(row=8, column=1, pady=3)
        startdate = Label(DataEntryFrame, text='StartDate:', bg='green', fg='white',
                          font=('times new roman', 15, 'bold'))
        startdate.grid(row=9, column=0, pady=3, sticky='W')
        startdate = Entry(DataEntryFrame, textvariable=self.startdate_var, font=('times new roman', 12, 'bold'))
        startdate.grid(row=9, column=1, pady=3)
        gender = Label(DataEntryFrame, text='Gender:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        gender.grid(row=10, column=0, pady=3, sticky='W')
        gender = Entry(DataEntryFrame, textvariable=self.gender_var, font=('times new roman', 12, 'bold'))
        gender.grid(row=10, column=1, pady=3)

        # -----------buttonframe----------
        btn_frame = Frame(DataEntryFrame, bg='green')
        btn_frame.place(x=10, y=450, height=60, width=320)
        btn_add = Button(btn_frame, text='Add', command=self.adding_data, bg='light green', bd=5, relief=GROOVE,
                         fg='black', width=4, font=('times new roman', 15, 'bold'))
        btn_add.grid(row=0, column=0, padx=5, pady=5)
        btn_update = Button(btn_frame, text='Update', command=self.update_data, bg='light green', bd=5, relief=GROOVE, fg='black', width=5,
                            font=('times new roman', 15, 'bold'))
        btn_update.grid(row=0, column=1, padx=5, pady=5)
        btn_delete = Button(btn_frame, command=self.delete_data, text='Delete', fg='black', bg='light green', bd=5, relief=GROOVE, width=4,
                            font=('times new roman', 15, 'bold'))
        btn_delete.grid(row=0, column=2, padx=5, pady=5)
        btn_clear = Button(btn_frame, text='Clear', command=self.clear, bg='light green', fg='black', width=4, bd=5, relief=GROOVE,
                           font=('times new roman', 15, 'bold'))
        btn_clear.grid(row=0, column=3, padx=5, pady=5)



        # -------Datadisplay frame------------

        DataDisplayFrame = Frame(self.root, bg='green', bd=4, relief=GROOVE)
        DataDisplayFrame.place(x=380, y=60, height=570, width=960)

        lbl_search = Label(DataDisplayFrame, text='Search By:', bg='green', fg='white', font=('times new roman', 15, 'bold'))
        lbl_search.grid(row=0, column=0, padx=30, pady=20)

        combo_search = ttk.Combobox(DataDisplayFrame, textvariable=self.searchby, font=('times new roman', 15, 'bold'), width=15)
        combo_search.grid(row=0, column=1, padx=20)
        combo_search['values'] = ('coursename', 'trainer', 'gender')

        txt_search = Entry(DataDisplayFrame, textvariable=self.search, font=('times new roman', 15, 'bold'), width=15)
        txt_search.grid(row=0, column=2, padx=20)

        btn_search = Button(DataDisplayFrame, command=self.search_data, text='Search', width=10,  bg='light green', fg='black', bd=5, relief=GROOVE,  font=('times new roman', 15, 'bold'))
        btn_search.grid(row=0, column=3, padx=20)

        btn_showall = Button(DataDisplayFrame, command=self.fetch_data, text='Show All', width=10, bg='light green', fg='black', bd=5, relief=GROOVE,  font=('times new roman', 15, 'bold'))
        btn_showall.grid(row=0, column=4, padx=20)

                   #-------------------tableframe---------

        tbl_frame = Frame(DataDisplayFrame, bd=5, relief=GROOVE)
        tbl_frame.place(x=10, y=80, width=930, height=450)

        self.Student_Table = ttk.Treeview(tbl_frame, columns=('roll_no', 'firstname', 'lastname', 'coursename', 'fee', 'contactnum', 'emailid', 'Trainer', 'startdate', 'gender'))

        self.Student_Table.heading('roll_no', text='Roll No')
        self.Student_Table.heading('firstname', text='First Name')
        self.Student_Table.heading('lastname', text='Last Name')
        self.Student_Table.heading('coursename', text='Course Name')
        self.Student_Table.heading('fee', text='Fee')
        self.Student_Table.heading('contactnum', text='Contact Num')
        self.Student_Table.heading('emailid', text='Email Id')
        self.Student_Table.heading('Trainer', text='Trainer')
        self.Student_Table.heading('startdate', text='Start Date')
        self.Student_Table.heading('gender', text='Gender')

        self.Student_Table.column('roll_no', width=90, anchor=CENTER)
        self.Student_Table.column('firstname', width=90, anchor=CENTER)
        self.Student_Table.column('lastname', width=90, anchor=CENTER)
        self.Student_Table.column('coursename', width=90, anchor=CENTER)
        self.Student_Table.column('fee', width=90, anchor=CENTER)
        self.Student_Table.column('contactnum', width=90, anchor=CENTER)
        self.Student_Table.column('emailid', width=90, anchor=CENTER)
        self.Student_Table.column('Trainer', width=90, anchor=CENTER)
        self.Student_Table.column('startdate', width=90, anchor=CENTER)
        self.Student_Table.column('gender', width=90, anchor=CENTER)

        self.Student_Table['show'] = 'headings'
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.Student_Table.pack()
        self.fetch_data()

    # -----------database connection----------

    def adding_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='Archana@1', db='nthdb')
        c = connection.cursor()
        c.execute('insert into nthdata values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                  (self.roll_no_var.get(),
                   self.firstname_var.get(),
                   self.lastname_var.get(),
                   self.coursename_var.get(),
                   self.fee_var.get(),
                   self.contactnum_var.get(),
                   self.emailid_var.get(),
                   self.Trainer_var.get(),
                   self.startdate_var.get(),
                   self.gender_var.get(),))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def fetch_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='Archana@1', db='nthdb')
        c = connection.cursor()
        c.execute('select *from nthdata')
        rows = c.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
                connection.commit()




    def clear(self):
        self.roll_no_var.set('')
        self.firstname_var.set('')
        self.lastname_var.set('')
        self.coursename_var.set('')
        self.fee_var.set('')
        self.contactnum_var.set('')
        self.emailid_var.set('')
        self.Trainer_var.set('')
        self.startdate_var.set('')
        self.gender_var.set('')

    def get_cursor(self,var):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.firstname_var.set(row[1])
        self.lastname_var.set(row[2])
        self.coursename_var.set(row[3])
        self.fee_var.set(row[4])
        self.contactnum_var.set(row[5])
        self.emailid_var.set(row[6])
        self.Trainer_var.set(row[7])
        self.startdate_var.set(row[8])
        self.gender_var.set(row[9])

    def update_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='Archana@1', db='nthdb')
        c = connection.cursor()
        c.execute('update nthdata set firstname=%s, lastname=%s, coursename=%s, fee=%s, contactnum=%s, emailid=%s, Trainer=%s, startdate=%s, gender=%s where rollno= %s',
                  (self.firstname_var.get(),
                   self.lastname_var.get(),
                   self.coursename_var.get(),
                   self.fee_var.get(),
                   self.contactnum_var.get(),
                   self.emailid_var.get(),
                   self.Trainer_var.get(),
                   self.startdate_var.get(),
                   self.gender_var.get(),
                   self.roll_no_var.get()))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def delete_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='Archana@1', db='nthdb')
        c = connection.cursor()
        c.execute('delete from nthdata where rollno=%s',
                  self.roll_no_var.get())
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def search_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='Archana@1', db='nthdb')
        c = connection.cursor()
        c.execute('select *from nthdata' 
                  ' where '+str(self.searchby.get())+' like "'+str(self.search.get())+'%" ')
        rows = c.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
                connection.commit()
                connection.close()







root = Tk()
obj = NTHStudentsData(root)
root.mainloop()
