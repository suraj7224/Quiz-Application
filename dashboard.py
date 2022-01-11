from tkinter import *
from PIL import Image,ImageTk  #pip install pillow
from time import *
from time import strftime
from StudyMaterial import studyMaterial
from Instruction import instruction
from Profile import profile
from Taketest import Test
from AboutUs import Aboutus


class dashboard():
    def __init__(self,root):
        self.root=root
        # self.root.geometry()
        self.root.title("Dashboard ")
        self.root.geometry("1600x900+0+0")
        # self.root.iconbitmap("image\image3.jpeg")


        # =========================left side logo image================================
        logo=Image.open("image\Terna.jpeg")
        logo=logo.resize((200,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(logo)

        f_Lable=Label(self.root,image=self.photoimg)
        f_Lable.place(x=0,y=0,width=200,height=120)

        #============================== Middle image===================================
        logo1=Image.open("image\image3.jpeg")
        logo1=logo1.resize((1400,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(logo1)

        self.f_Lable1=Label(self.root,image=self.photoimg1)
        self.f_Lable1.place(x=200,y=0,width=1400,height=120)

        # ===============================Quiz ninja Label==============================
        txt_label1=Label(self.root,text="QUIZ GURU",font=("times new roman",20,"bold"),bg="black",fg="gold")
        txt_label1.place(x=0,y=120,width=1600,height=50)

        #====================================== main frame===================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=172,width=1600,height=900)

        # =========================Backgrond dashboard image============================
        logo4=Image.open("image\Dash_bg.jpeg")
        logo4=logo4.resize((1280,675),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(logo4)

        self.f_Lable4=Label(main_frame,image=self.photoimg4)
        self.f_Lable4.place(x=252,y=0,width=1280,height=675)

        # ========================Menu Label======================================
        txt_label3 = Label(self.root, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="white")
        txt_label3.place(x=0, y=172, width=250,height=40)

        #====================================== Button here===============================
        user_button=Button(main_frame,text="Profile",font=("times new roman",20,"bold"),bg="black" ,fg="gold", cursor="hand2",command=self.profile_Details)
        user_button.place(x=0,y=40,width=246,height=50)

        instrct_button=Button(main_frame,text="Instruction",font=("times new roman",20,"bold"),bg="black" ,fg="gold", cursor="hand2",command= self.instruct_Details)
        instrct_button.place(x=0,y=90,width=246,height=50)

        test_button=Button(main_frame,text="Take Test",font=("times new roman",20,"bold"),bg="black" ,fg="gold", cursor="hand2",command=self.Test_Details)
        test_button.place(x=0,y=140,width=246,height=50)

        about_button=Button(main_frame,text="About us",font=("times new roman",20,"bold"),bg="black" ,fg="gold", cursor="hand2",command=self.abput_us)
        about_button.place(x=0,y=190,width=246,height=50)

        study_button=Button(main_frame,text="Study Material",font=("times new roman",20,"bold"),bg="black" ,fg="gold", cursor="hand2",command=self.Study_Details)
        study_button.place(x=0,y=240,width=246,height=50)

        logout_button=Button(main_frame,text="Log Out",font=("times new roman",20,"bold"),bg="black" ,fg="gold", cursor="hand2",command=self.Log_out)
        logout_button.place(x=0,y=290,width=246,height=50)


        #================================ Down image===================================
        down_image = Image.open("image\Logo.jpeg")
        down_image= down_image.resize((246, 275), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(down_image)

        f_Lable2 = Label(main_frame, image=self.photoimg2)
        f_Lable2.place(x=2, y=342, width=246, height=275)

    def profile_Details(self):
        self.new_Window1 = Toplevel(self.root)
        self.app1 = profile(self.new_Window1)


    def instruct_Details(self):
        self.new_Window2 = Toplevel(self.root)
        self.app2 = instruction(self.new_Window2)

    def Test_Details(self):
        self.new_Window = Toplevel(self.root)
        self.app3 = Test(self.new_Window)

    def abput_us(self):
        self.new_Window4 = Toplevel(self.root)
        self.about = Aboutus(self.new_Window4)

    def Study_Details(self):
        self.new_Window3 = Toplevel(self.root)
        self.Study = studyMaterial(self.new_Window3)

    def Log_out(self):
       self.root.destroy()
       import Login

    def tick(self):
        clock = Label(self.root, font=("time",20, "bold"), bg="hotpink")
        clock.place(x=320, y=120,height=50)
        # call tick() function for clock label
        time_string = strftime('%H:%M:%S %p')
        clock.config(text=time_string)
        # call tick() after every 200 micro seconds to display updated time
        clock.after(100, self.tick)

    def date(self):
        date = Label(self.root, font=("date",20, "bold"), bg="purple")
        date.place(x=1290, y=120,height=50)
        # call tick() function for clock label
        date_string = strftime('%D')
        date.config(text=date_string)
        # call tick() after every 200 micro seconds to display updated time
        date.after(100, self.date)



root=Tk()
obj=dashboard(root)
obj.tick()
obj.date()
root.mainloop()