from tkinter import*
from tkinter import ttk
from typing_extensions import Self
from PIL import Image,ImageTk
from studentID import Student
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("face Recognition system")
        
        #first iMAGE
        img=Image.open(r"C:\mproject\face 3.jpg")
        img=img.resize((1300,190),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=190)
        
        
        #background iMAGE
        img1=Image.open(r"C:\mproject\face 3.jpg")
        img1=img.resize((1400,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1400,height=700)
        
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="gray",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=35)
        
        #student button
        img2=Image.open(r"C:\mproject\face 4.jpg")
        img2=img2.resize((170,170),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b1=Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=170,height=170)
        
        b1_0=Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="purple")
        b1_0.place(x=150,y=250,width=170,height=35)
        
        
        #detectface button
        img3=Image.open(r"\mproject\face 6.jpg")
        img3=img3.resize((170,170),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b1=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b1.place(x=400,y=400,width=170,height=170)
        
        b1_0=Button(bg_img,text="Face Recognizer",cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="purple")
        b1_0.place(x=400,y=550,width=170,height=35)
        
        
        #attendance face button
        img4=Image.open(r"\mproject\face 7.jpg")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=400,y=100,width=170,height=170)
        
        b1_0=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="purple")
        b1_0.place(x=400,y=250,width=170,height=35)
        
        
        #creator button
        img5=Image.open(r"\mproject\face8.jpg")
        img5=img5.resize((170,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=150,y=400,width=170,height=170)
        
        b1_0=Button(bg_img,text="Creator",cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="purple")
        b1_0.place(x=150,y=550,width=170,height=35)
        
        
        #photo button
        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",17,"bold"),bg="white",fg="purple")
        b1_1.place(x=700,y=200,width=170,height=35)
        
        
        #data button 
        b1_2=Button(bg_img,text="DATA",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="purple")
        b1_2.place(x=700,y=300,width=170,height=35)
        
        
        #help button
        b1_2=Button(bg_img,text="HELP",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="purple")
        b1_2.place(x=700,y=400,width=170,height=35)
        
        
        #exit button
        b1_2=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="purple")
        b1_2.place(x=700,y=500,width=170,height=35)
        
        
    def open_img(self):
        os.starfile("data")
        
        #====================function button=====================
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
    
    
            


