from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class student:
    #------------------main_window-----------------#
    def __init__(self, root):
        self.root = root
        self.root.geometry('1360x660+1+1')
        self.root.title('يرنامج اداره المدارس')
        self.root.configure(background="#2b2d42")
        self.root.resizable(False, False)
        title = Label(self.root,bg="#2b2d42",text="نظام تسجيل الطلاب",font=("monospace",14),fg="white")
        title.pack()
    #-----------------variables------------------#   

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.add_var = StringVar()
        self.gender_var = StringVar()
        self.delete_var = StringVar()
        self.search_var = StringVar()
        self.search_by = StringVar()

    #-----------------student_info------------------#
        frame1 = Frame(root, width=300, height=400)
        frame1.place(x=1060, y=1)

        info_label = Label(frame1,text="ادخال بيانات الطالب")
        info_label.place(x=100, y=4)

        id_label = Label(frame1, text=":كود الطالب", font=("monospace",12))
        id_label.place(x=215, y=40)
        id_entry = Entry(frame1, width="30", justify=CENTER, textvariable=self.id_var)
        id_entry.place(x=20, y=42)

        name_label = Label(frame1, text=":اسم الطالب", font=("monospace",12))
        name_label.place(x=215, y=80)
        name_entry = Entry(frame1, width="30", justify=CENTER, textvariable=self.name_var)
        name_entry.place(x=20, y=82)

        age_label = Label(frame1, text=":سن الطالب", font=("monospace",12))
        age_label.place(x=215, y=120)
        age_entry = Entry(frame1, width="30", justify=CENTER, textvariable=self.age_var)
        age_entry.place(x=20, y=122)

        add_label = Label(frame1, text=":عنوان الطالب", font=("monospace",12))
        add_label.place(x=214, y=200)
        add_entry = Entry(frame1, width="30", justify=CENTER, textvariable=self.add_var)
        add_entry.place(x=20, y=202)

        gender_label = Label(frame1, text=":جنس الطالب", font=("monospace",12))
        gender_label.place(x=210, y=160)
        gender_combo = ttk.Combobox(frame1, width='27', textvariable=self.gender_var)
        gender_combo['value'] = ('ذكر','انثي')
        gender_combo.place(x=20, y=162)
        
        delewithname_label = Label(frame1, text=": حذف الطالب", font=("monospace",12))
        delewithname_label.place(x=210, y=240)
        delewithname_entry = Entry(frame1, width="30", justify=CENTER, textvariable=self.delete_var)
        delewithname_entry.place(x=20, y=242)


        #-----------------control_buttons------------------#
        frame2 = Frame(root, width=300, height=400)
        frame2.place(x=1060, y=404)

        add_btn = Button(frame2, text='اضافه طالب',bg='#2b2d42', fg='white' ,command=self.add_student)
        add_btn.place(x=150, y=16, width=140, height=40)

        delete_btn = Button(frame2, text='حذف طالب',bg='#2b2d42', fg='white' ,command=self.delete_name)
        delete_btn.place(x=8, y=16, width=140, height=40)

        update_btn = Button(frame2, text='تعديل بيانات طالب',bg='#2b2d42', fg='white' ,command=self.update)
        update_btn.place(x=150, y=65, width=140, height=40)

        exit_btn = Button(frame2, text=' حذف بيانات',bg='#2b2d42', fg='white' ,command=root.quit)
        exit_btn.place(x=8, y=65, width=140, height=40)

        empty_btn = Button(frame2, text=' مدرستنا ',bg='#2b2d42', fg='white' ,command= self.clear)
        empty_btn.place(x=68, y=115, width=180, height=40)

        about_btn = Button(frame2, text='اغلاق البرنامج',bg='#2b2d42', fg='white' ,command=self.about)
        about_btn.place(x=68, y=165, width=180, height=40)


         #-----------------search_frame------------------#
        frame3 = Frame(root, width=1058, height=40)
        frame3.place(x=1, y=29)
        
        search_label = Label(frame3, text="البحث عن طالب") 
        search_label.place(x=970,y=6)
        search_combo = ttk.Combobox(frame3, textvariable=self.search_by, justify=CENTER)
        search_combo['value'] = ('id','name','address')
        search_combo.place(x=820, y=8)

        search_entry = Entry(frame3, width=50, textvariable=self.search_var, justify="right")
        search_entry.place(x=500, y=9)

        search_btn = Button(frame3, text="بحث", bg="#2b2d42", fg='white' ,command=self.search)
        search_btn.place(x=438, y=9, width=54, height=20)

         #-----------------data_view------------------#
        frame4 = Frame(self.root)
        frame4.place(x=1,y=70,width=1058, height=590)
        
        scroll_x = Scrollbar(frame4, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame4, orient=VERTICAL)

        self.data_table = ttk.Treeview(frame4,show='headings',
            columns=('add','gender','age','name','id'),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        self.data_table.place(x=18, y=1, width=1050,height=570)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.data_table.xview)
        scroll_y.config(command=self.data_table.yview)
        
        self.data_table.heading('add', text='عنوان الطالب')
        self.data_table.heading('gender', text='جنس الطالب')
        self.data_table.heading('age', text='عمر الطالب')
        self.data_table.heading('name', text='اسم الطالب')
        self.data_table.heading('id', text='كود الطالب')

        self.data_table.column('add', width='100')
        self.data_table.column('gender', width='30')
        self.data_table.column('age', width='50')
        self.data_table.column('name', width='100')
        self.data_table.column('id', width='100')

        self.data_table.bind('<ButtonRelease-1>', self.view_data)


    #-----------------------conecct DB and addto DB-----------------------------#
        self.fetch_all()
    def add_student(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='students')
        cur = con.cursor()
        cur.execute('insert into student values(%s, %s, %s, %s, %s)',(
                                                                  self.add_var.get(),
                                                                  self.gender_var.get(),
                                                                  self.age_var.get(),
                                                                  self.name_var.get(),
                                                                  self.id_var.get()
        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        #------------------------view data in tree view-----------------#
    def fetch_all(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='students')
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert('',END, value=row)
            con.commit()

        con.close()

    def delete_name(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='students')
        cur = con.cursor()
        cur.execute('delete from student where name = %s', self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.age_var.set('')
        self.gender_var.set('')
        self.add_var.set('')

    def view_data(self, ev):
        data_focus = self.data_table.focus()
        selected_item = self.data_table.item(data_focus)
        row = selected_item['values']
        self.id_var.set(row[4])
        self.name_var.set(row[3])
        self.age_var.set(row[2])
        self.add_var.set(row[1])
        self.gender_var.set(row[0])

    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='students')
        cur = con.cursor()
        cur.execute('update student set address = %s, gender = %s, age = %s, name = %s where id = %s',(
                                                                  self.add_var.get(),
                                                                  self.gender_var.get(),
                                                                  self.age_var.get(),
                                                                  self.name_var.get(),
                                                                  self.id_var.get()
        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def search(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='students')
        cur = con.cursor()
        cur.execute("select * from student where " + 
                    str(self.search_by.get())+" LIKE '%"+ str(self.search_var.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert('',END, value=row)
            con.commit()

        con.close()

    def about(self):
        messagebox.showinfo("sohila nabil","welcome to our school")

    




 






root = Tk()
obj = student(root)
root.mainloop()