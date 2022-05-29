from multiprocessing.dummy import connection
from tkinter import*
from tkinter import ttk
from typing_extensions import Self
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
 
sys.setrecursionlimit(10**6)



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("face Recognition system")
        
        #=================variables=======================
        self.va_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Division=StringVar()
        self.var_Roll=StringVar()
        self.var_Email=StringVar()
        self.var_phoneno=StringVar()
        self.var_gender=StringVar()
        self.var_subject=StringVar()
        self.var_teacher=StringVar() 
        
        
        
        #first iMAGE
        img=Image.open(r"C:\mproject\face 9.jpg")
        img=img.resize((1300,190),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=190)
        
        
        #background iMAGE
        img1=Image.open(r"C:\mproject\face 9.jpg")
        img1=img.resize((1400,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1400,height=700)
        
        
        title_lbl=Label(bg_img,text="STUDENT INFORMATION",font=("times new roman",22,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=20,width=1300,height=35)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=70,width=1300,height=600)
        
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Info",font=("Britannic Bold",11,"bold"))
        left_frame.place(x=10,y=10,width=630,height=550)
        
        
         #class student info
        Class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Britannic Bold",11,"bold"))
        Class_Student_frame.place(x=25,y=45,width=530,height=430) 
        
        
        #student id
        studentid_label=Label(Class_Student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white",fg="black")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(Class_Student_frame,textvariable=self.va_ID,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #student name
        studentname_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        studentname_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #class division
        class_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white",fg="black")
        class_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        class_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Division,width=20,font=("times new roman",13,"bold"))
        class_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #roll no
        rollno_label=Label(Class_Student_frame,text="Roll NO.:",font=("times new roman",13,"bold"),bg="white",fg="black")
        rollno_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        rollno_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #email
        email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white",fg="black")
        email_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #phone no.
        phoneno_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white",fg="black")
        phoneno_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        
        phoneno_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",13,"bold"))
        phoneno_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        
        #gender
        gender_label=Label(Class_Student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white",fg="black")
        gender_label.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        
        #studentname_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #studentname_entry.grid(row=6,column=1,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),state="readonly",width=12)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=6,column=1,pady=10,stick=W)
        
        
        #subject
        subject_label=Label(Class_Student_frame,text="Subject:",font=("times new roman",13,"bold"),bg="white",fg="black")
        subject_label.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        
        subject_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_subject,width=20,font=("times new roman",13,"bold"))
        subject_entry.grid(row=7,column=1,padx=10,pady=5,sticky=W)  
        
        
        #teacher name
        teacher_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        teacher_label.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=8,column=1,padx=10,pady=5,sticky=W)
    
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=13,column=0)
        
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=13,column=1)
        
        
        #buttons frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=340,width=520,height=70)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",10,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)
        
        
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",10,"bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=1)
        
        
        
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=16,font=("times new roman",10,"bold"),bg="black",fg="white")
        take_photo_btn.grid(row=0,column=2)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",10,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=3)
          
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Britannic Bold",11,"bold"))
        Right_frame.place(x=650,y=10,width=600,height=550)
        
        #==========search system=================
        #search info
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Britannic Bold",11,"bold"))
        Search_frame.place(x=5,y=15,width=590,height=60) 
        
        search_label=Label(Search_frame,text="Search System",font=("times new roman",14,"bold"),bg="yellow",fg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",11,"bold"),state="readonly",width=12)
        search_combo["values"]=("select","Roll_no","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,pady=10,stick=W)
        
        search_entry=ttk.Entry(Search_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="black",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="black",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        ############======================table frame====================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=85,width=590,height=430) 
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("ID","Name","Division","Roll","Email","phoneno","gender","subject","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Division",text="Class Division") 
        self.student_table.heading("Roll",text="Roll NO")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("phoneno",text="Phone NO")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("subject",text="Subject")
        self.student_table.heading("teacher",text="Teacher Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("subject",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data(  )
        
        #===================function declearation=======================
    def add_data(self):
        if self.var_Name.get()=="" or self.va_ID.get()=="":
            messagebox.showerror("Error","All need to be filled",parent=self.root)
            
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9827369676",database="microsoft")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                self.va_ID.get(),
                                                                                                self.var_Name.get(),
                                                                                                self.var_Division.get(),                                                        
                                                                                                self.var_Roll.get(),
                                                                                                self.var_Email.get(),
                                                                                                self.var_phoneno.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_subject.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()

                                                                                              ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","Student Details has been added successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showinfo("Error",f"Due To:{str(es)}",parent=self.root) 
                
                
                
    #====================fetch data-------------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9827369676",database="microsoft")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            self.fetch_data()
        conn.close()     
        
         
                       
    #====================get cursor===================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus) 
        data=content["values"]
        
        self.va_ID.set(data[0]),
        self.var_Name.set(data[1]),
        self.var_Division.set(data[2]),
        self.var_Roll.set(data[3]),
        self.var_Email.set(data[4]),
        self.var_phoneno.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_subject.set(data[7]),
        self.var_teacher.set(data[8]),
        self.var_radio1.set(data[9]),
        
        
        
    #===================update===============================
    def update_data(self):
        if self.var_Name.get()=="" or self.va_ID.get()=="":
            messagebox.showerror("Error","All need to be filled",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Upadate","Do you want to update this students details")
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9827369676",database="microsoft")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Student_ID=%s,Name=%s,Division=%s,Roll=%s,Email=%s,Phone_NO=%s,Gender=%s,Subject=%s,Teacher=%s,PhotoSample=%s)",(
                
                                                                                                                                                         self.va_ID.get(),
                                                                                                                                                         self.var_Name.get(),
                                                                                                                                                         self.var_Division.get(),                                                        
                                                                                                                                                         self.var_Roll.get(),
                                                                                                                                                         self.var_Email.get(),
                                                                                                                                                         self.var_phoneno.get(),
                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                         self.var_subject.get(),
                                                                                                                                                         self.var_teacher.get(),
                                                                                                                                                         self.var_radio1.get()

                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
               
                    
        
        
        
#======================delete function==================

    def delete_data(self):
        if self.va_ID.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","DO you want to delete this student",parent=self.root)           
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9827369676",database="microsoft")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"   
                    val=(self.va_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully deleted students details",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    
                    
                    
    #==============================generate data set or take photo smaples========================
    def generate_dataset(self):
        if self.var_Name.get()=="" or self.va_ID.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9827369676",database="microsoft")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1 
                my_cursor.execute("update student set Student_ID=%s,Name=%s,Division=%s,Roll=%s,Email=%s,Phone_NO=%s,Gender=%s,Subject=%s,Teacher=%s,PhotoSample=%s)",(
                
                                                                                                                                                         self.va_ID.get(),
                                                                                                                                                         self.var_Name.get(),
                                                                                                                                                         self.var_Division.get(),                                                        
                                                                                                                                                         self.var_Roll.get(),
                                                                                                                                                         self.var_Email.get(),
                                                                                                                                                         self.var_phoneno.get(),
                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                         self.var_subject.get(),
                                                                                                                                                         self.var_teacher.get(),
                                                                                                                                                         self.var_radio1.get()

                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
            
            
       #============load predifiend data on face opencv=============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
    
                   for(x,y,w,h) in faces:
                      face_cropped=img[y:y+h,x:x+w]
                      return face_cropped
    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id )+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),2)
                    cv2.imshow("crooped Face",face)
    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")
            except Exception as es:
                messagebox.showinfo("Error",f"Due To:{str(es)}",parent=self.root) 
     
              
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
        