from tkinter import *
import webbrowser
from PIL import Image,ImageTk  #pip install pillow

class studyMaterial():
    def __init__(self,root):
        self.root=root
        self.root.title("Study Material")
        self.root.geometry("1280x675+252+202")
        self.root.resizable(False,False)
        self.root.config(background="White")


        # ===============================Background Image==================================

        bg=Image.open("image\Blue and Pink Shapes Neon Noir Fitness Influencer Facebook Cover.png")
        bg=bg.resize((1280,650),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bg)

        f_Lable=Label(self.root,image=self.photoimg)
        f_Lable.place(x=0,y=0,width=1280,height=650)

        txt_label1 = Label(self.root, text="Python Swayam Course", font=("times new roman", 20, "bold"),bg="blue" , fg="gold")
        txt_label1.place(x=0, y=80,width=450, height=40)

        txt_label2 = Label(self.root, text="Operating System Swayam Course", font=("times new roman", 20, "bold"),bg="blue", fg="gold")
        txt_label2.place(x=0, y=130, width=450, height=40)

        txt_label3 = Label(self.root, text="DBMS Swayam Course", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label3.place(x=0, y=180, width=350, height=40)

        txt_label4 = Label(self.root, text="Data Structure And Algorithm Coursera Course", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label4.place(x=0, y=230, width=600, height=40)

        txt_label5 = Label(self.root, text="Python Programming Projects Udemy Course", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label5.place(x=0, y=280, width=600, height=40)

        txt_label6 = Label(self.root, text="Computers Networking Udemy Course", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label6.place(x=0, y=330, width=600, height=40)

        txt_label7 = Label(self.root, text="Ethical Hacking Udemy Course", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label7.place(x=0, y=380, width=600, height=40)

        txt_label8 = Label(self.root, text="Java Programming Udemy Course", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label8.place(x=0, y=430, width=600, height=40)

        txt_label9 = Label(self.root, text="computer organization architecture Udemy Course ", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label9.place(x=0, y=480, width=600, height=40)

        txt_label10 = Label(self.root, text="C++ Programming Udemy Courses", font=("times new roman", 20, "bold"), bg="blue", fg="gold")
        txt_label10.place(x=0, y=530, width=600, height=40)


        # Python  Swayam Course Link
        url1 = "https://onlinecourses.swayam2.ac.in/aic20_sp33/preview"
        def openpython():
            webbrowser.open(url1)

        # Operating System Swayam Course Link
        url2="https://onlinecourses.swayam2.ac.in/aic20_sp24/preview"
        def openOs():
            webbrowser.open_new(url2)

        # DBMS Swayam Course
        url3= "https://onlinecourses.swayam2.ac.in/aic20_sp36/preview"
        def openDBMS():
            webbrowser.open(url3)

        # Data Structure And Algorithm Coursera Course
        url4="https://www.coursera.org/specializations/data-structures-algorithms?"
        def openDSA():
            webbrowser.open_new(url4)

        # Python Programming Projects Udemy Cours
        url5="https://www.udemy.com/course/python-programming-projects/"
        def python():
            webbrowser.open_new(url5)

        # Computers Networking Udemy Course
        url6 = "https://www.udemy.com/course/learncomputernetworks/"
        def CNND():
            webbrowser.open_new(url6)

        # Ethical Hacking Udemy Course
        url7 = "https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"
        def Ethical_Hacking():
            webbrowser.open_new(url7)

        # Java Programming Udemy Course
        url8 = "https://www.udemy.com/course/java-the-complete-java-developer-course/"
        def java():
            webbrowser.open_new(url8)

        # COA
        url9 = "https://www.udemy.com/course/computer-architecture-computer-organization-course/"
        def COA():
            webbrowser.open_new(url9)

        #C++ Programming Udemy Courses
        url10 = "https://www.udemy.com/course/beginning-c-plus-plus-programming/"
        def c_programming():
            webbrowser.open_new(url10)

        # Button
        python_button1 = Button(self.root,text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=openpython)
        python_button1.place(x=850, y=80, width=200, height=40)

        os_button2 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=openOs)
        os_button2.place(x=850, y=130, width=200, height=40)

        dbms_button3 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=openDBMS)
        dbms_button3.place(x=850, y=180, width=200, height=40)

        DSA_button4 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=openDSA)
        DSA_button4.place(x=850, y=230, width=200, height=40)

        python_button5 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=python)
        python_button5.place(x=850, y=280, width=200, height=40)

        CNND_button6 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=CNND)
        CNND_button6.place(x=850, y=330, width=200, height=40)

        ethical_button7 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=Ethical_Hacking)
        ethical_button7.place(x=850, y=380, width=200, height=40)

        java_button8 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=java)
        java_button8.place(x=850, y=430, width=200, height=40)

        coa_button9 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=COA)
        coa_button9.place(x=850, y=480, width=200, height=40)

        c_button10 = Button(self.root, text="Click Here", font=("times new roman", 20, "bold"), bg="black", fg="gold",cursor="hand2",command=c_programming)
        c_button10.place(x=850, y=530, width=200, height=40)





if __name__== "__main__":
    root=Tk()
    obj=studyMaterial(root)
    root.mainloop()

