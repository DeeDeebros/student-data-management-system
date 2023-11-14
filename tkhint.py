from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry

class Login:
    def __init__(self,my_frame) -> None:
        self.mainlogin_frame = my_frame
        # self.mainlogin_frame = Frame(self.window,background="#2C3333")
        self.mainlogin_frame.place(x=0,y=0,width=1366,height=768)

        # creating login form
        self.login_frame = Frame(self.mainlogin_frame,bg="white",height=580,width=550,padx=130,pady=90,background="#395B64")
        self.login_frame.pack()

        self.project_name = Label(self.login_frame,text="Student Management System",font=("",16,"bold"),bg="#395B64",fg="white")

        self.user_name = Label(self.login_frame,text="Username: ",bg="#395B64",fg="white",font=("",16,"bold"))
        self.passwd = Label(self.login_frame,text="Password: ",bg="#395B64",fg="white",font=("",16,"bold"))
        self.user_entry = Entry(self.login_frame,width=20)
        self.passwd_entry = Entry(self.login_frame,width=20,show="*")
        self.login_button = Button(self.login_frame,text="Login",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:change_2(mydash.returned(),self.user_entry.get(),self.passwd_entry.get()))

        self.project_name.grid(row=0,column=0,columnspan=2,pady=20)
        self.user_name.grid(row=1,column=0,padx=5,pady=20)
        self.user_entry.grid(row=1,column=1,padx=5,pady=20)
        self.passwd.grid(row=2,column=0,padx=5,pady=20)
        self.passwd_entry.grid(row=2,column=1,padx=5,pady=20)
        self.login_button.grid(row=3,column=0,columnspan=2,pady=20)

        self.user_entry.bind('<Return>',focus_next)
        self.passwd_entry.bind('<Return>',focus_next)
       
    def returned(self):
        
        return self.mainlogin_frame
class Student:
    def __init__(self,my_frame) -> None:
        self.users_frame = my_frame
        self.users_frame.place(x=0,y=0,width=1366,height=768)
        self.welcome = Label(self.users_frame,text="Welcome Back",font=("",20,"bold"),bg="#395B64",fg="white")
        self.welcome.place(y=10,x=600)
        self.back = Button(self.users_frame,text="logout",cursor="hand2",activebackground="gray",command=lambda:change(mylogin.returned(),0))
        self.back.place(x=658,y=680)
    def create_details(self,output,user_id):
            self.output = output
            self.personal_frame = Frame(self.users_frame,bg="black")
            self.personal_frame.place(x=100,y=150,width=550,height=500)
            self.academic_frame = Frame(self.users_frame,bg="black")
            self.academic_frame.place(x=730,y=150,width=550,height=500)
            
            self.label = Label(self.personal_frame,text="Personal Details",font=("",16,"bold"),bg="black",fg="white")
            self.name = Label(self.personal_frame,text="Fullname: ",font=("",10,"bold"),bg="black",fg="white")
            self.age = Label(self.personal_frame,text="Age: ",font=("",10,"bold"),bg="black",fg="white")
            self.sex = Label(self.personal_frame,text="Sex: ",font=("",10,"bold"),bg="black",fg="white")
            self.address = Label(self.personal_frame,text="Address: ",font=("",10,"bold"),bg="black",fg="white")
            self.dob = Label(self.personal_frame,text="Date Of Birth: ",font=("",10,"bold"),bg="black",fg="white")
            self.guardian = Label(self.personal_frame,text="Guardian: ",font=("",10,"bold"),bg="black",fg="white")
            self.number = Label(self.personal_frame,text="Mobile Number: ",font=("",10,"bold"),bg="black",fg="white")
            self.state = Label(self.personal_frame,text="State: ",font=("",10,"bold"),bg="black",fg="white")
            self.pincode = Label(self.personal_frame,text="Pincode: ",font=("",10,"bold"),bg="black",fg="white")
            self.department = Label(self.personal_frame,text="Department : ",font=("",10,"bold"),bg="black",fg="white")
            
            self.name_entry = Label(self.personal_frame,text=self.output[1],font=("",10,"bold"),bg="black",fg="white")
            self.age_entry = Label(self.personal_frame,text=self.output[2],font=("",10,"bold"),bg="black",fg="white")
            self.sex_entry = Label(self.personal_frame,text=self.output[4],font=("",10,"bold"),bg="black",fg="white")
            self.address_entry = Label(self.personal_frame,text=self.output[7],font=("",10,"bold"),bg="black",fg="white")
            self.dob_entry = Label(self.personal_frame,text=self.output[3],font=("",10,"bold"),bg="black",fg="white")
            self.guardian_entry = Label(self.personal_frame,text=self.output[6],font=("",10,"bold"),bg="black",fg="white")
            self.number_entry = Label(self.personal_frame,text=self.output[10],font=("",10,"bold"),bg="black",fg="white")
            self.state_entry = Label(self.personal_frame,text=self.output[9],font=("",10,"bold"),bg="black",fg="white")
            self.pincode_entry = Label(self.personal_frame,text=self.output[8],font=("",10,"bold"),bg="black",fg="white")
            self.department_entry = Label(self.personal_frame,text=self.output[5],font=("",10,"bold"),bg="black",fg="white")

            self.label.grid(row=0,column=0,columnspan=4,padx=5,pady=10)

            self.name.grid(row=1,column=0,padx=15,pady=10,sticky="w")
            self.name_entry.grid(row=1,column=1,padx=5,pady=10,sticky="w")

            self.age.grid(row=2,column=0,padx=15,pady=10,sticky="w")
            self.age_entry.grid(row=2,column=1,padx=5,pady=10,sticky="w")

            self.sex.grid(row=3,column=0,padx=15,pady=10,sticky="w")
            self.sex_entry.grid(row=3,column=1,padx=5,pady=10,sticky="w")

            self.dob.grid(row=4,column=0,padx=15,pady=10,sticky="w")
            self.dob_entry.grid(row=4,column=1,padx=15,pady=10,sticky="w")

            self.address.grid(row=7,column=0,padx=15,pady=10,sticky="w")
            self.address_entry.grid(row=7,column=1,padx=5,pady=10,sticky="w")

            self.guardian.grid(row=6,column=0,padx=15,pady=10,sticky="w")
            self.guardian_entry.grid(row=6,column=1,padx=5,pady=10,sticky="w")
            
            self.number.grid(row=8,column=0,padx=15,pady=10,sticky="w")
            self.number_entry.grid(row=8,column=1,padx=5,pady=10,sticky="w")

            self.state.grid(row=9,column=0,padx=15,pady=10,sticky="w")
            self.state_entry.grid(row=9,column=1,padx=5,pady=10,sticky="w")

            self.pincode.grid(row=10,column=0,padx=15,pady=10,sticky="w")
            self.pincode_entry.grid(row=10,column=1,padx=5,pady=10,sticky="w")

            self.department.grid(row=5,column=0,padx=15,pady=10,sticky="w")
            self.department_entry.grid(row=5,column=1,padx=5,pady=10,sticky="w")

            self.ac_label = Label(self.academic_frame,text="Academic Details",font=("",16,"bold"),bg="black",fg="white")
            self.date = Label(self.academic_frame,text="Date: ",font=("",10,"bold"),bg="black",fg="white")
            self.date_entry = DateEntry(self.academic_frame,date_pattern="y-mm-dd")
            self.status = Label(self.academic_frame,text="Status: ",font=("",10,"bold"),bg="black",fg="white")
            self.status_entry = Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")

            self.type_entry =ttk.Combobox(self.academic_frame, values=['','internal exam','public exam'])
            self.type = Label(self.academic_frame,text="Exam Type : ",font=("",10,"bold"),bg="black",fg="white")
            self.sub1 = Label(self.academic_frame,text="Subject 1: ",font=("",10,"bold"),bg="black",fg="white")
            self.sub2= Label(self.academic_frame,text="Subject 2: ",font=("",10,"bold"),bg="black",fg="white")
            self.sub3 = Label(self.academic_frame,text="Subject 3: ",font=("",10,"bold"),bg="black",fg="white")

            self.sub1_entry = Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")
            self.sub2_entry= Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")
            self.sub3_entry = Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")

            self.mark_search = Button(self.academic_frame,text="Search",cursor="hand2",activebackground="gray",command=lambda:academic_search2(flag=0,user_id=user_id,date=self.date_entry.get(),typ=self.type_entry.get()))
            self.attend_search = Button(self.academic_frame,text="Search",cursor="hand2",activebackground="gray",command=lambda:academic_search2(flag=1,user_id=user_id,date=self.date_entry.get(),typ=self.type_entry.get()))
            self.ac_label.place()

            self.date.place(x=20,y=50)
            self.type.place(x=20,y=150)
            self.status.place(x=20,y=100)
            self.sub1.place(x=20,y=200)
            self.sub2.place(x=20,y=250)
            self.sub3.place(x=20,y=300)
            self.mark_search.place(x=380,y=150)


            self.date_entry.place(x=120,y=50)
            self.status_entry.place(x=120,y=100)
            self.type_entry.place(x=120,y=150)
            self.sub1_entry.place(x=120,y=200)
            self.sub2_entry.place(x=120,y=250)
            self.sub3_entry.place(x=120,y=300)
            self.attend_search.place(x=300,y=50)

            self.ac_label.place(y=0,x=180)
    def configed(self,output,flag):
        self.output = output
        if flag == 1:
            self.status_entry.configure(text=output[0])
        else:
            self.sub1_entry.configure(text=output[0])
            self.sub2_entry.configure(text=output[1])
            self.sub3_entry.configure(text=output[2])
    
    def returned(self):
        return self.users_frame   
class Users:
    def __init__(self,my_frame) -> None:
        self.users_frame = my_frame
        self.users_frame.place(x=0,y=0,width=1366,height=768)
        self.user_search_frame = Frame(self.users_frame,bg="#395B64")
        self.user_search_frame.place(x=450,y=0,width=600,height=90)

        self.search_label = Label(self.user_search_frame,text="Username: ",font=("",18,"bold"),bg="#395B64",fg="white")
        self.search_entry = Entry(self.user_search_frame)
       
        if self.search_entry.get =="":
            messagebox.showinfo(title="Error",message="Username cannot be empty!!")

        self.search_button = Button(self.user_search_frame,text="search",cursor="hand2",activebackground="gray",command=lambda:display(self.search_entry.get()))
        self.back_button = Button(self.user_search_frame,text="Back",cursor="hand2",activebackground="gray",command=lambda:change(mydash.returned(),1))

        self.search_label.grid(row=0,column=0,padx=5,pady=20)
        self.search_entry.grid(row=0,column=1,padx=5,pady=20)
        self.search_button.grid(row=0,column=2,padx=5,pady=20)
        self.back_button.grid(row=0,column=3,padx=5,pady=20)
    
    def create_details(self,output):
            self.output = output
            self.personal_frame = Frame(self.users_frame,bg="black")
            self.personal_frame.place(x=100,y=150,width=550,height=500)
            self.academic_frame = Frame(self.users_frame,bg="black")
            self.academic_frame.place(x=730,y=150,width=550,height=500)
            
            self.label = Label(self.personal_frame,text="Personal Details",font=("",16,"bold"),bg="black",fg="white")
            self.name = Label(self.personal_frame,text="Fullname: ",font=("",10,"bold"),bg="black",fg="white")
            self.age = Label(self.personal_frame,text="Age: ",font=("",10,"bold"),bg="black",fg="white")
            self.sex = Label(self.personal_frame,text="Sex: ",font=("",10,"bold"),bg="black",fg="white")
            self.address = Label(self.personal_frame,text="Address: ",font=("",10,"bold"),bg="black",fg="white")
            self.dob = Label(self.personal_frame,text="Date Of Birth: ",font=("",10,"bold"),bg="black",fg="white")
            self.guardian = Label(self.personal_frame,text="Guardian: ",font=("",10,"bold"),bg="black",fg="white")
            self.number = Label(self.personal_frame,text="Mobile Number: ",font=("",10,"bold"),bg="black",fg="white")
            self.state = Label(self.personal_frame,text="State: ",font=("",10,"bold"),bg="black",fg="white")
            self.pincode = Label(self.personal_frame,text="Pincode: ",font=("",10,"bold"),bg="black",fg="white")
            self.department = Label(self.personal_frame,text="Department : ",font=("",10,"bold"),bg="black",fg="white")
            
            self.name_entry = Label(self.personal_frame,text=self.output[2],font=("",10,"bold"),bg="black",fg="white")
            self.age_entry = Label(self.personal_frame,text=self.output[3],font=("",10,"bold"),bg="black",fg="white")
            self.sex_entry = Label(self.personal_frame,text=self.output[5],font=("",10,"bold"),bg="black",fg="white")
            self.address_entry = Label(self.personal_frame,text=self.output[8],font=("",10,"bold"),bg="black",fg="white")
            self.dob_entry = Label(self.personal_frame,text=self.output[4],font=("",10,"bold"),bg="black",fg="white")
            self.guardian_entry = Label(self.personal_frame,text=self.output[7],font=("",10,"bold"),bg="black",fg="white")
            self.number_entry = Label(self.personal_frame,text=self.output[11],font=("",10,"bold"),bg="black",fg="white")
            self.state_entry = Label(self.personal_frame,text=self.output[10],font=("",10,"bold"),bg="black",fg="white")
            self.pincode_entry = Label(self.personal_frame,text=self.output[9],font=("",10,"bold"),bg="black",fg="white")
            self.department_entry = Label(self.personal_frame,text=self.output[6],font=("",10,"bold"),bg="black",fg="white")

            self.label.grid(row=0,column=0,columnspan=4,padx=5,pady=10)

            self.name.grid(row=1,column=0,padx=15,pady=10,sticky="w")
            self.name_entry.grid(row=1,column=1,padx=5,pady=10,sticky="w")

            self.age.grid(row=2,column=0,padx=15,pady=10,sticky="w")
            self.age_entry.grid(row=2,column=1,padx=5,pady=10,sticky="w")

            self.sex.grid(row=3,column=0,padx=15,pady=10,sticky="w")
            self.sex_entry.grid(row=3,column=1,padx=5,pady=10,sticky="w")

            self.dob.grid(row=4,column=0,padx=15,pady=10,sticky="w")
            self.dob_entry.grid(row=4,column=1,padx=15,pady=10,sticky="w")

            self.address.grid(row=7,column=0,padx=15,pady=10,sticky="w")
            self.address_entry.grid(row=7,column=1,padx=5,pady=10,sticky="w")

            self.guardian.grid(row=6,column=0,padx=15,pady=10,sticky="w")
            self.guardian_entry.grid(row=6,column=1,padx=5,pady=10,sticky="w")
            
            self.number.grid(row=8,column=0,padx=15,pady=10,sticky="w")
            self.number_entry.grid(row=8,column=1,padx=5,pady=10,sticky="w")

            self.state.grid(row=9,column=0,padx=15,pady=10,sticky="w")
            self.state_entry.grid(row=9,column=1,padx=5,pady=10,sticky="w")

            self.pincode.grid(row=10,column=0,padx=15,pady=10,sticky="w")
            self.pincode_entry.grid(row=10,column=1,padx=5,pady=10,sticky="w")

            self.department.grid(row=5,column=0,padx=15,pady=10,sticky="w")
            self.department_entry.grid(row=5,column=1,padx=5,pady=10,sticky="w")

            self.ac_label = Label(self.academic_frame,text="Academic Details",font=("",16,"bold"),bg="black",fg="white")
            self.date = Label(self.academic_frame,text="Date: ",font=("",10,"bold"),bg="black",fg="white")
            self.date_entry = DateEntry(self.academic_frame,date_pattern="y-mm-dd")
            self.status = Label(self.academic_frame,text="Status: ",font=("",10,"bold"),bg="black",fg="white")
            self.status_entry = Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")

            self.type_entry =ttk.Combobox(self.academic_frame, values=['','internal exam','public exam'])
            self.type = Label(self.academic_frame,text="Exam Type : ",font=("",10,"bold"),bg="black",fg="white")
            self.sub1 = Label(self.academic_frame,text="Subject 1: ",font=("",10,"bold"),bg="black",fg="white")
            self.sub2= Label(self.academic_frame,text="Subject 2: ",font=("",10,"bold"),bg="black",fg="white")
            self.sub3 = Label(self.academic_frame,text="Subject 3: ",font=("",10,"bold"),bg="black",fg="white")

            self.sub1_entry = Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")
            self.sub2_entry= Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")
            self.sub3_entry = Label(self.academic_frame,text="",font=("",10,"bold"),bg="black",fg="white")

            self.mark_search = Button(self.academic_frame,text="Search",cursor="hand2",activebackground="gray",command=lambda:academic_search(flag=0,user_id=self.search_entry.get(),date=self.date_entry.get(),typ=self.type_entry.get()))
            self.attend_search = Button(self.academic_frame,text="Search",cursor="hand2",activebackground="gray",command=lambda:academic_search(flag=1,user_id=self.search_entry.get(),date=self.date_entry.get(),typ=self.type_entry.get()))
            self.ac_label.place()

            self.date.place(x=20,y=50)
            self.type.place(x=20,y=150)
            self.status.place(x=20,y=100)
            self.sub1.place(x=20,y=200)http://127.0.0.1:8000/posts
            self.sub2.place(x=20,y=250)
            self.sub3.place(x=20,y=300)
            self.mark_search.place(x=380,y=150)


            self.date_entry.place(x=120,y=50)
            self.status_entry.place(x=120,y=100)
            self.type_entry.place(x=120,y=150)
            self.sub1_entry.place(x=120,y=200)
            self.sub2_entry.place(x=120,y=250)
            self.sub3_entry.place(x=120,y=300)
            self.attend_search.place(x=300,y=50)

            self.ac_label.place(y=0,x=180)
            self.back = Button(self.users_frame,text="Delete User",cursor="hand2",activebackground="gray",command=lambda:delete_user(self.output))
            self.back.place(x=658,y=680)
    def reset(self):
        self.__init__(frame_users)
    def reset_frame(self):
        self.users_frame.destroy()
        
    def configed(self,output,flag):
        self.output = output
        if flag == 1:
            self.status_entry.configure(text=output[0])
        else:
            self.sub1_entry.configure(text=output[0])
            self.sub2_entry.configure(text=output[1])
            self.sub3_entry.configure(text=output[2])
    
    def returned(self):
        return self.users_frame
def delete_user(output):
    asked = messagebox.askyesno(title="Confirm",message="Do you want to delete this user ?")
    if asked:
        args_1 = []
        args_2 = []
        try:
            cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
            query_1 = 'delete from marks where student_id = %s'
            query_2 = 'delete from attendance where student_id = %s'
            query_3 = 'delete from student where student_id = %s'
            query_4 = 'delete from user where user_id = %s'
            args_1.append(output[0])
            args_2.append(output[1])
            cursor_1 = cnx.cursor()
            cursor_1.execute(query_1,args_1)

            cursor_2 = cnx.cursor()
            cursor_2.execute(query_2,args_1)

            cursor_3 = cnx.cursor()
            cursor_3.execute(query_3,args_1)

            cursor_4 = cnx.cursor()
            cursor_4.execute(query_4,args_2)
            cnx.commit()
        
            
            
        except mysql.connector.Error as error:
            print(error)  
        finally:
            messagebox.showinfo(title="Success",message="User deleted successfully!!")  
            cursor_1.close()
            cursor_2.close()
            cursor_3.close()
            cursor_4.close()
            cnx.close()
            new_output = ('','','','','','','','','','','','','','','','','','')
            myusers.create_details(new_output)
    else:
        return
def academic_search(flag,user_id,date=1,typ=0):
    args1 = []
    args2 = []
    
    if date == 1 and typ == 0:
        messagebox.showinfo(title="Error",message="Filter cannot be empty!!")
        new_output = ("")
        myusers.create_details(new_output) 
    try:
        cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
        query1 = 'select status from attendance inner join student where student.student_id = attendance.student_id and user_id = %s and date = %s'
        query2 = 'select sub_1,sub_2,sub_3 from marks inner join student where student.student_id = marks.student_id and user_id = %s and type = %s'
        args1.append(user_id)
        args1.append(date)
        args2.append(user_id)
        args2.append(typ)
        if flag == 1:
            cursor = cnx.cursor()
            cursor.execute(query1,args1)
            output = cursor.fetchone()
            
            if output is not None:
                myusers.configed(output,flag)
            else:
                messagebox.showinfo(title="Error",message="Data not found!!")
                new_output = ("",)
                myusers.configed(new_output,flag) 
        else:
            cursor = cnx.cursor()
            cursor.execute(query2,args2)
            output = cursor.fetchone()
            if output is not None:
                myusers.configed(output,flag)
            else:
                messagebox.showinfo(title="Error",message="Data not found!!")
                new_output = ("","","")
                myusers.configed(new_output,flag) 
            
        cnx.commit()
        
            
    except mysql.connector.Error as error:
            print(error)  
    finally:
            
            cursor.close()
            cnx.close()
def academic_search2(flag,user_id,date=1,typ=0):
    args1 = []
    args2 = []
    
    if date == 1 and typ == 0:
        messagebox.showinfo(title="Error",message="Filter cannot be empty!!")
        new_output = ("")
        mystudent.create_details(new_output) 
    try:
        cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
        query1 = 'select status from attendance inner join student where student.student_id = attendance.student_id and user_id = %s and date = %s'
        query2 = 'select sub_1,sub_2,sub_3 from marks inner join student where student.student_id = marks.student_id and user_id = %s and type = %s'
        args1.append(user_id)
        args1.append(date)
        args2.append(user_id)
        args2.append(typ)
        if flag == 1:
            cursor = cnx.cursor()
            cursor.execute(query1,args1)
            output = cursor.fetchone()
            
            if output is not None:
                mystudent.configed(output,flag)
            else:
                messagebox.showinfo(title="Error",message="Data not found!!")
                new_output = ("",)
                mystudent.configed(new_output,flag) 
        else:
            cursor = cnx.cursor()
            cursor.execute(query2,args2)
            output = cursor.fetchone()
            if output is not None:
                mystudent.configed(output,flag)
            else:
                messagebox.showinfo(title="Error",message="Data not found!!")
                new_output = ("","","")
                mystudent.configed(new_output,flag) 
            
        cnx.commit()
        
            
    except mysql.connector.Error as error:
            print(error)  
    finally:
            
            cursor.close()
            cnx.close()
def display(user_id):
        args = []
        try:
            cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
            query = 'select student_id,user_id,name,age,dob,sex,branch,guardian,address,pincode,state,mob_no from student inner join department where student.department_id = department.department_id and user_id = %s'
            args.append(user_id)
            cursor = cnx.cursor()
            cursor.execute(query,args)
            output = cursor.fetchone()

            cnx.commit()
            if output is not None:
                myusers.create_details(output) 
            else:
                messagebox.showinfo(title="Error",message="Username not found!!")
            
        except mysql.connector.Error as error:
            print(error)  
        finally:
            
            cursor.close()
            cnx.close()
def display2(user_id):
        args = []
        try:
            cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
            query = 'select user_id,name,age,dob,sex,branch,guardian,address,pincode,state,mob_no from student inner join department where student.department_id = department.department_id and user_id = %s'
            args.append(user_id)
            cursor = cnx.cursor()
            cursor.execute(query,args)
            output = cursor.fetchone()

            cnx.commit()
            if output is not None:
                mystudent.create_details(output,user_id) 
            else:
                messagebox.showinfo(title="Error",message="Username not found!!")
            
        except mysql.connector.Error as error:
            print(error)  
        finally:
            
            cursor.close()
            cnx.close()              
class Dashboard:
    def __init__(self,my_frame) -> None:
    
        self.dashboard_frame = my_frame
        self.dashboard_frame.place(x=0,y=0,width=1366,height=768)

        # creating header frame with a logout button and dashboard label
        self.header = Frame(self.dashboard_frame,bg="#395B64")
        self.header.place(x=350,y=0,width=1050,height=70)
        self.logout = Button(self.header,text="logout",font=("",10,"bold"),bg="#E7F6F2",bd=0,cursor="hand2",activebackground="gray",command=lambda:change(mylogin.returned(),0))
        self.logout.place(x=900,y=25,width=80,height=25)
        self.dashboard_label = Label(self.header,text="Dashboard",font=("",18,"bold"),bg="#395B64")
        self.dashboard_label.place(x=40,y=25,width=200,height=25)

        # creating a navigation frame with user logo and details
        self.navigation = Frame(self.dashboard_frame,bg="#A5C9CA")
        self.navigation.place(x=0,y=0,width=350,height=768)

        # adding admin details and current datetime
        self.admin_name = Label(self.navigation,text="Name: Admin",bg="#A5C9CA",font=("",10,"bold")).place(x=90,y=250)
        self.admin_sex = Label(self.navigation,text="Sex: Male",bg="#A5C9CA",font=("",10,"bold")).place(x=90,y=300)
        self.admin_college = Label(self.navigation,text="College: Nss College,Palakkad",bg="#A5C9CA",font=("",10,"bold")).place(x=90,y=350)
        # self.current_date = Label(self.navigation,text=f"Date: {self.date_now}",bg="#A5C9CA",font=("",10,"bold")).place(x=90,y=400)

    

        # adding user logo in the navigation frame
        self.user_logo = Image.open("/home/amal/Documents/python programs/python_database/user.png")
        self.resized_logo = self.user_logo.resize((120,120), Image.Resampling.LANCZOS)
        user_photo = ImageTk.PhotoImage(self.resized_logo)
        self.user_logo_img = Label(self.navigation,image=user_photo,bg="#A5C9CA")
        self.user_logo_img.image=user_photo
        self.user_logo_img.place(x=90,y=80,width=120,height=120)


        # creating a body frame with buttons
        self.body = Frame(self.dashboard_frame,bg="#2C3333")
        self.body.place(x=350,y=70,width=1050,height=698)

        # adding button to body frame
        self.add_user = Button(self.body,text="Add User",width=20,height=8,bd=0,cursor="hand2",activebackground="gray",font=("",12,"bold"),command=lambda:change(adduser.returned(),0))
        self.add_attendance = Button(self.body,text="Add Attendance",width=20,height=8,bd=0,cursor="hand2",activebackground="gray",font=("",12,"bold"),command=lambda:change(myattend.returned(),0))
        self.add_marks = Button(self.body,text="Add Marks",width=20,height=8,bd=0,cursor="hand2",activebackground="gray",font=("",12,"bold"),command=lambda:change(mymarks.returned(),0))
        self.user_details = Button(self.body,text="User Search",width=20,height=8,bd=0,cursor="hand2",activebackground="gray",font=("",12,"bold"),command=lambda:change(myusers.returned(),0))

        # using grid to position the button in the body frame
        self.add_user.grid(row=0,column=0,padx=145,pady=100)
        self.add_attendance.grid(row=0,column=1,padx=145,pady=100)
        self.add_marks.grid(row=1,column=0,padx=145,pady=100)
        self.user_details.grid(row=1,column=1,padx=145,pady=100)

    def returned(self):
        return self.dashboard_frame
class Adduser:
    def __init__(self,my_frame) -> None:
        self.adduser_frame = my_frame
        # self.mainlogin_frame = Frame(self.window,background="#2C3333")
        self.adduser_frame.place(x=0,y=0,width=1366,height=768)
        self.adduser_container_frame=Frame(self.adduser_frame,background="#395B64")
        self.adduser_container_frame.pack()

        self.registration = Label(self.adduser_container_frame,text="Student Registration Form",font=("",18,"bold"),bg="#395B64",fg="white")

        self.fullname = Label(self.adduser_container_frame,text="Fullname: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.age = Label(self.adduser_container_frame,text="Age: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.sex = Label(self.adduser_container_frame,text="Sex: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.address = Label(self.adduser_container_frame,text="Address: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.dob = Label(self.adduser_container_frame,text="Date Of Birth: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.guardian = Label(self.adduser_container_frame,text="Guardian: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.number = Label(self.adduser_container_frame,text="Mobile Number: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.state = Label(self.adduser_container_frame,text="State: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.pincode = Label(self.adduser_container_frame,text="Pincode: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.department_id = Label(self.adduser_container_frame,text="Department ID: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.password = Label(self.adduser_container_frame,text="Password: ",font=("",10,"bold"),bg="#395B64",fg="white")
        self.admission = Label(self.adduser_container_frame,text="Admission No: ",font=("",10,"bold"),bg="#395B64",fg="white")

        self.registration_submit = Button(self.adduser_container_frame,text="Submit",width=11,height=2,bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:submit_form(self.fullname_entry.get(),self.age_entry.get(),self.sex_entry.get(),self.address_entry.get(),self.dob_entry.get(),self.guardian_entry.get(),self.number_entry.get(),self.state_entry.get(),self.pincode_entry.get(),self.department_id_entry.get(),self.password_entry.get(),self.admission_entry.get()))

        self.registration_back = Button(self.adduser_container_frame,text="Back",width=11,height=2,bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:change(mydash.returned(),0))



        self.fullname_entry = Entry(self.adduser_container_frame,width=20)
        self.age_entry = Entry(self.adduser_container_frame,width=20)
        self.sex_entry = Entry(self.adduser_container_frame,width=20)
        self.dob_entry = Entry(self.adduser_container_frame,width=20)
        self.address_entry = Entry(self.adduser_container_frame,width=20)
        self.guardian_entry = Entry(self.adduser_container_frame,width=20)
        self.number_entry = Entry(self.adduser_container_frame,width=20)
        self.state_entry = Entry(self.adduser_container_frame,width=20)
        self.pincode_entry = Entry(self.adduser_container_frame,width=20)
        self.department_id_entry = Entry(self.adduser_container_frame,width=20)
        self.password_entry = Entry(self.adduser_container_frame,width=20)
        self.admission_entry = Entry(self.adduser_container_frame,width=20)

        self.registration.grid(row=0,column=0,columnspan=4,padx=5,pady=30)

        self.fullname.grid(row=1,column=0,padx=5,pady=30)
        self.fullname_entry.grid(row=1,column=1,padx=5,pady=30)

        self.age.grid(row=2,column=0,padx=5,pady=30)
        self.age_entry.grid(row=2,column=1,padx=5,pady=30)

        self.sex.grid(row=3,column=0,padx=5,pady=30)
        self.sex_entry.grid(row=3,column=1,padx=5,pady=30)

        self.dob.grid(row=4,column=0,padx=5,pady=30)
        self.dob_entry.grid(row=4,column=1,padx=5,pady=30)

        self.address.grid(row=5,column=0,padx=5,pady=30)
        self.address_entry.grid(row=5,column=1,padx=5,pady=30)

        self.guardian.grid(row=6,column=0,padx=5,pady=30)
        self.guardian_entry.grid(row=6,column=1,padx=5,pady=30)
        
        self.number.grid(row=1,column=2,padx=5,pady=30)
        self.number_entry.grid(row=1,column=3,padx=5,pady=30)

        self.state.grid(row=2,column=2,padx=5,pady=30)
        self.state_entry.grid(row=2,column=3,padx=5,pady=30)

        self.pincode.grid(row=3,column=2,padx=5,pady=30)
        self.pincode_entry.grid(row=3,column=3,padx=5,pady=30)

        self.department_id.grid(row=4,column=2,padx=5,pady=30)
        self.department_id_entry.grid(row=4,column=3,padx=5,pady=30)

        self.password.grid(row=5,column=2,padx=5,pady=30)
        self.password_entry.grid(row=5,column=3,padx=5,pady=30)

        self.admission.grid(row=6,column=2,padx=5,pady=30)
        self.admission_entry.grid(row=6,column=3,padx=5,pady=30)
        
        self.registration_submit.grid(row=7,column=0,columnspan=4,padx=5,pady=5)
        self.registration_back.grid(row=8,column=0,columnspan=4,padx=5,pady=5)

        self.fullname_entry.bind('<Return>',focus_next)
        self.age_entry.bind('<Return>',focus_next)
        self.sex_entry.bind('<Return>',focus_next)
        self.dob_entry.bind('<Return>',focus_next)
        self.department_id_entry.bind('<Return>',focus_next)
        self.address_entry.bind('<Return>',focus_next)
        self.guardian_entry.bind('<Return>',focus_next)
        self.number_entry.bind('<Return>',focus_next)
        self.state_entry.bind('<Return>',focus_next)
        self.pincode_entry.bind('<Return>',focus_next)
        self.password_entry.bind('<Return>',focus_next)
        self.admission_entry.bind('<Return>',focus_next)
    def returned(self):
        return self.adduser_frame
class AddMarks:
    def __init__(self,my_frame) -> None:
        self.indicate = "marks"
        self.marks_frame = my_frame
        self.marks_frame.place(x=0,y=0,width=1366,height=768)
        # creating search form
        self.search_frame = Frame(self.marks_frame,bg="white",padx=130,pady=90,background="#395B64")
        self.search_frame.place(x=0,y=0,height=768,width=683)
       
        self.result_frame = Frame(self.marks_frame,bg="white",padx=20,pady=20,background="gray")
        self.result_frame.place(x=683,y=0,height=768,width=683)


        cols = ('userid','name','department')
        self.treeview = ttk.Treeview(self.result_frame,columns=cols,show='headings')
        self.scrollbar = Scrollbar(self.result_frame, orient="vertical", command=self.treeview.yview)
        
        for col in cols:
            self.treeview.heading(col,text=col)
        

        # Configure the treeview to use the scrollbar
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.treeview.column("#2",width=180)

        # Add the treeview and scrollbar to the window
        self.treeview.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.bind('<<TreeviewSelect>>',self.treeview_select)
   
        # Add the frame to the main window and show it               
        self.heading = Label(self.search_frame,text="Search Student By",font=("",16,"bold"),bg="#395B64",fg="white")
        self.user_id = Label(self.search_frame,text="User ID: ",font=("",16,"bold"),bg="#395B64",fg="white")
        self.department = Label(self.search_frame,text="Department: ",font=("",16,"bold"),bg="#395B64",fg="white") 
        self.user_id_entry = Entry(self.search_frame)
        self.department_combo = ttk.Combobox(self.search_frame, values=['no selection','computer science engineering', 'civil engineering', 'mechanical engineering','electrical engineering','applied science'])
        selected_combo = self.department_combo.get()
        # Set the default value
        self.department_combo.set('no selection')
        
        self.submit = Button(self.search_frame,text="Search",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:search(self.user_id_entry.get(),self.department_combo.get(),self.indicate))
        self.back_button = Button(self.search_frame,text="Back",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:change(mydash.returned(),0))
       

        self.heading.grid(row=0,column=0,columnspan=2,padx=5,pady=20)

        self.user_id.grid(row=1,column=0,padx=5,pady=20)
        self.user_id_entry.grid(row=1,column=1,padx=5,pady=20)

        self.department.grid(row=2,column=0,padx=5,pady=20)
        self.department_combo.grid(row=2,column=1,padx=5,pady=20)

        self.submit.grid(row=3,column=0,columnspan=2,padx=5,pady=20)
        self.back_button.grid(row=4,column=0,columnspan=2,padx=5,pady=20)

    def create_marks(self):

        # self.marks_add_frame = Frame(self.search_frame,bg="white",padx=50,pady=40,background="#395B64")
        self.marks_add_frame = Frame(self.search_frame,bg="white",padx=15,pady=10,background="#395B64")
        self.marks_add_frame.place(x=0,y=400,height=230,width=485)
        self.sub1_label = Label(self.marks_add_frame,text="subject 1: ",font=("",12,"bold"),bg="#395B64",fg="white")
        self.sub1_entry = Entry(self.marks_add_frame)

        self.sub2_label = Label(self.marks_add_frame,text="subject 2: ",font=("",12,"bold"),bg="#395B64",fg="white")
        self.sub2_entry = Entry(self.marks_add_frame)

        self.sub3_label = Label(self.marks_add_frame,text="subject 3: ",font=("",12,"bold"),bg="#395B64",fg="white")
        self.sub3_entry = Entry(self.marks_add_frame)

        self.type_label = Label(self.marks_add_frame,text="exam type: ",font=("",12,"bold"),bg="#395B64",fg="white")
        # self.type_entry = Entry(self.marks_add_frame)
        self.type_entry = ttk.Combobox(self.marks_add_frame, values=['internal exam','public exam'])
        self.type_entry.set(" ")
        


        self.marks_add_button = Button(self.marks_add_frame,text="Add",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:update_marks(self.output[0],self.sub1_entry.get(),self.sub2_entry.get(),self.sub3_entry.get(),self.type_entry.get()))


        self.sub1_label.grid(row=0,column=0,padx=2,pady=10)
        self.sub1_entry.grid(row=0,column=1,padx=2,pady=10)

        self.sub2_label.grid(row=1,column=0,padx=2,pady=10)
        self.sub2_entry.grid(row=1,column=1,padx=2,pady=10)

        self.sub3_label.grid(row=2,column=0,padx=2,pady=10)
        self.sub3_entry.grid(row=2,column=1,padx=2,pady=10)

        self.type_label.grid(row=3,column=0,padx=2,pady=10)
        self.type_entry.grid(row=3,column=1,padx=2,pady=10)


        self.marks_add_button.grid(row=4,column=0,columnspan=2,padx=2,pady=10)
        self.marks_add_frame.tkraise()


    def treeview_select(self,event):
        marks_ask = messagebox.askyesno(title="Message",message="Do you want to add/edit marks ?")
        mylist = []
        if marks_ask:
            try:
                cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
                cursor = cnx.cursor()
                    # Execute the INSERT query
                selected_item = self.treeview.selection()[0]
               
                self.user_id_selected = mymarks.treeview.item(selected_item)['values'][0]
               
                mylist.append(self.user_id_selected)
                
               
                
                query = 'select student_id from student where user_id = %s'
                
               
                cursor.execute(query, mylist)
                self.output = cursor.fetchone()
              
                    # Commit the transaction
                cnx.commit()
            except mysql.connector.Error as error:
                print(error)
            except TclError:
                print("error inside tree view")
            finally: 
                cursor.close()
                cnx.close()
            #   
            #   print(self.user_id_selected)

            mymarks.create_marks()
    def update(self,data,flag):
        try:
        
            self.treeview.delete(*self.treeview.get_children())
            if flag == 0:
                for lines in data:
                    self.treeview.insert("", "end",values=lines)
            else:
                self.treeview.insert("","end",values=data)
        except TclError:
            pass
    def returned(self):
        return self.marks_frame    
class AddAttendance:
    def __init__(self,my_frame) -> None:
        self.indicate = "attend"
        self.attend_frame = my_frame
        self.attend_frame.place(x=0,y=0,width=1366,height=768)
        # creating search form
        self.search_frame = Frame(self.attend_frame,bg="white",padx=130,pady=90,background="#395B64")
        self.search_frame.place(x=0,y=0,height=768,width=683)
       
        self.result_frame = Frame(self.attend_frame,bg="white",padx=20,pady=20,background="gray")
        self.result_frame.place(x=683,y=0,height=768,width=683)


        cols = ('userid','name','department')
        self.treeview = ttk.Treeview(self.result_frame,columns=cols,show='headings')
        self.scrollbar = Scrollbar(self.result_frame, orient="vertical", command=self.treeview.yview)
        
        for col in cols:
            self.treeview.heading(col,text=col)
        

        # Configure the treeview to use the scrollbar
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.treeview.column("#2",width=180)

        # Add the treeview and scrollbar to the window
        self.treeview.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.bind('<<TreeviewSelect>>',self.treeview_select)
   
        # Add the frame to the main window and show it               
        self.heading = Label(self.search_frame,text="Search Student By",font=("",16,"bold"),bg="#395B64",fg="white")
        self.user_id = Label(self.search_frame,text="User ID: ",font=("",16,"bold"),bg="#395B64",fg="white")
        self.department = Label(self.search_frame,text="Department: ",font=("",16,"bold"),bg="#395B64",fg="white") 
        self.user_id_entry = Entry(self.search_frame)
        self.department_combo = ttk.Combobox(self.search_frame, values=['no selection','computer science engineering', 'civil engineering', 'mechanical engineering','electrical engineering','applied science'])
        selected_combo = self.department_combo.get()
        # Set the default value
        self.department_combo.set('no selection')
        
        self.submit = Button(self.search_frame,text="Search",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:search(self.user_id_entry.get(),self.department_combo.get(),self.indicate))
        self.back_button = Button(self.search_frame,text="Back",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:change(mydash.returned(),0))
       

        self.heading.grid(row=0,column=0,columnspan=2,padx=5,pady=20)

        self.user_id.grid(row=1,column=0,padx=5,pady=20)
        self.user_id_entry.grid(row=1,column=1,padx=5,pady=20)

        self.department.grid(row=2,column=0,padx=5,pady=20)
        self.department_combo.grid(row=2,column=1,padx=5,pady=20)

        self.submit.grid(row=3,column=0,columnspan=2,padx=5,pady=20)
        self.back_button.grid(row=4,column=0,columnspan=2,padx=5,pady=20)

    def create_attendance(self):

        self.attend_add_frame = Frame(self.search_frame,bg="white",padx=50,pady=40,background="#395B64")
        self.attend_add_frame.place(x=0,y=400,height=230,width=485)
        self.date_entry_label = Label(self.attend_add_frame,text="DATE",font=("",12,"bold"),bg="#395B64",fg="white")
        self.date_entry = DateEntry(self.attend_add_frame,date_pattern="y-mm-dd")
        
        self.attend_status_label = Label(self.attend_add_frame,text="STATUS",font=("",12,"bold"),bg="#395B64",fg="white")
        self.attend_status = ttk.Combobox(self.attend_add_frame, values=['no selection','present','absent'])
        self.attend_status.set('no selection')
        
        self.attend_add_button = Button(self.attend_add_frame,text="Add",bg="white",cursor="hand2",activebackground="#A5C9CA",command=lambda:update_attend(self.output[0],self.date_entry.get(),self.attend_status.get()))
        

        self.date_entry_label.place(x=30,y=50)
        self.date_entry.place(x=30,y=88)
        self.attend_status_label.place(x=160,y=50)
        self.attend_status.place(x=160,y=88)
        self.attend_add_button.place(y=120,x=130)

        self.attend_add_frame.tkraise()

    def treeview_select(self,event):
        attendance_ask = messagebox.askyesno(title="Message",message="Do you want to add/edit attendance ?")
        mylist = []
        if attendance_ask:
            try:
                cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
                cursor = cnx.cursor()
                    # Execute the INSERT query
                selected_item = self.treeview.selection()[0]
               
                self.user_id_selected = myattend.treeview.item(selected_item)['values'][0]
               
                mylist.append(self.user_id_selected)
                
               
                
                query = 'select student_id from student where user_id = %s'
                
               
                cursor.execute(query, mylist)
                self.output = cursor.fetchone()
              
                    # Commit the transaction
                cnx.commit()
            except mysql.connector.Error as error:
                print(error)
            except TclError:
                print("error")
            finally: 
                cursor.close()
                cnx.close()
            #   
            #   print(self.user_id_selected)

            myattend.create_attendance()
    def update(self,data,flag):
        try:
        
            self.treeview.delete(*self.treeview.get_children())
            if flag == 0:
                for lines in data:
                    self.treeview.insert("", "end",values=lines)
            else:
                self.treeview.insert("","end",values=data)
        except TclError:
            pass
    def returned(self):
        return self.attend_frame
def search(user_no,selected_combo,indicate):
    try:
        if len(user_no) == 0 and str(selected_combo) == "no selection":
            messagebox.showerror(title="Error",message="Search Fields Cannot Be Empty !!!")
        mylist = []
        flag = 0
        cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
        cursor = cnx.cursor()
        if str(selected_combo) == 'no selection':
            mylist.append(user_no)
            query = "SELECT user_id,name,branch FROM student INNER JOIN department ON student.department_id = department.department_id where user_id = %s"
            cursor.execute(query,mylist)
            mysearch = cursor.fetchone()
            flag = 1
        else:
            mylist.append(selected_combo)
            query = "SELECT user_id,name,branch FROM student INNER JOIN department ON student.department_id = department.department_id where branch = %s"
            cursor.execute(query,mylist)
            mysearch = cursor.fetchall()
        cnx.commit()
        if indicate == "attend":            
            myattend.update(mysearch,flag)
        else:
            mymarks.update(mysearch,flag)
    except mysql.connector.Error as error:
        print(error)  
    finally:  
        cursor.close()
        cnx.close()        
def submit_form(*args):
  try:
    cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
    cursor = cnx.cursor()
        # Execute the INSERT query
    sub_args =(args[11],args[0],args[10])
    query_1 = 'insert into user(user_id,name,password) values(%s,%s,%s)'
    query_2 = 'INSERT INTO student (name,age,sex,address,dob,guardian,mob_no,state,pincode,department_id,password,user_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' 
    cursor.execute(query_1,sub_args)
    cursor.execute(query_2, args)
    cnx.commit()
  except mysql.connector.Error as error:
    print(error)
  except TclError:
    print("error")  
  finally:  
    cursor.close()
    cnx.close()
    messagebox.showinfo(title="Success",message="Student was added successfully!!")
def update_attend(user_id,date,status):
    
  try:
    args_2 = (user_id,date,status)
    query_1 = 'select status from attendance where student_id = %s and date = %s'
    args_1 = (user_id,date)
    query_2 = 'insert into attendance(student_id,date,status) values(%s,%s,%s)'
    cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
    cursor = cnx.cursor()
    cursor.execute(query_1, args_1)
    result = cursor.fetchone()
    
    if result == None:
        cursor_1 = cnx.cursor()
        cursor_1.execute(query_2, args_2)
        cnx.commit()
        messagebox.showinfo(title="Success",message="Attendance was added successfully!!")
    else:
        cursor_2 = cnx.cursor()
        query_3 = 'update attendance set status = %s where student_id = %s'
        args_3 = (status,user_id)
        cursor_2.execute(query_3, args_3)
        cnx.commit()
        messagebox.showinfo(title="Success",message="Attendance was updated successfully!!")


  except mysql.connector.Error as error:
    print(error)
  except TclError:
    print("error")
  finally:  
    cursor.close()
    cnx.close()
def update_marks(user_id,sub1,sub2,sub3,typ):
    
  try:
    args_2 = (user_id,sub1,sub2,sub3,typ)
    query_1 = 'select marks_id from marks where student_id = %s and type = %s'
    args_1 = (user_id,typ)
    query_2 = 'insert into marks(student_id,sub_1,sub_2,sub_3,type) values(%s,%s,%s,%s,%s)'
    cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
    cursor = cnx.cursor()
    cursor.execute(query_1, args_1)
    result = cursor.fetchone()
    
    if result == None:
        cursor_1 = cnx.cursor()
        cursor_1.execute(query_2, args_2)
        cnx.commit()
        messagebox.showinfo(title="Success",message="Marks was added successfully!!")
    else:
        cursor_2 = cnx.cursor()
        query_3 = 'update marks set sub_1 = %s,sub_2 = %s,sub_3 = %s  where student_id = %s'
        args_3 = (sub1,sub2,sub3,user_id)
        cursor_2.execute(query_3, args_3)
        cnx.commit()
        messagebox.showinfo(title="Success",message="Marks was updated successfully!!")


  except mysql.connector.Error as error:
    print(error)
  except TclError:
    print("error inside update marks")
  finally:  
    cursor.close()
    cnx.close()  
def focus_next(event):
    event.widget.tk_focusNext().focus()
def change(frame,session_id):
    if session_id == 1:
        # myusers.reset_frame()
        # myusers.reset()
        global myusers
        del myusers
        myusers = Users(frame_users)
        
        
    frame.tkraise()
def change_2(frame,username,password):
    if username == '20a100' and password == 'python':
       frame.tkraise()
    else:
       check_password(username,password)
def check_password(username,password):

    try:
        # Connect to the database
        cnx = mysql.connector.connect(user='project', password='project', host='localhost', database='project')
        student_frame = mystudent.returned()
        # Create a cursor
        cursor = cnx.cursor()

        # Define the search query
        query = "SELECT * FROM user WHERE user_id = %s AND password = %s"

        # Define the values to search for
        values = (username, password)

        # Execute the query
        cursor.execute(query, values)

        # Fetch the result
        result = cursor.fetchone()
        if result is not None:
            change(mystudent.returned(),0)
            display2(username)
        else:
            messagebox.showinfo(title="Authentication Error",message="Invalid Username Or Password!!")
    except mysql.connector.Error as error:
        print(error)

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()

if __name__=="__main__":

    
    window = Tk()
    window.title("project")
    window.geometry("1366x768")
    window.resizable(False, False)
    window.state("normal")
    window.config(background="white")

    frame_student = Frame(window,bg="#395B64")
    frame_log = Frame(window,background="#2C3333")
    frame_dash = Frame(window)
    frame_adduser = Frame(window,bg="#395B64")
    frame_student_login = Frame(window,bg="red")
    frame_addattend = Frame(window,bg="black")
    frame_addmarks = Frame(window,bg="black")
    frame_users = Frame(window,bg="#395B64")

    mystudent = Student(frame_student)
    myusers = Users(frame_users)
    mylogin = Login(frame_log)
    mydash = Dashboard(frame_dash)
    myattend = AddAttendance(frame_addattend)
    mymarks = AddMarks(frame_addmarks)

    adduser = Adduser(frame_adduser)
    
    myattend = AddAttendance(frame_addattend)
    

    change(mylogin.returned(),0)
    window.mainloop()
    