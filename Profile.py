from tkinter import *
from tkinter import ttk ,messagebox
from PIL import Image,ImageTk
import mysql.connector

class profile():
    def __init__(self,root):
        self.root = root
        self.root.title("Profile")
        self.root.geometry("1280x675+252+202")
        self.root.resizable(False, False)
        self.root.config(background="White")


        # ====================================Background Image=====================================
        bg = Image.open("image\ProfilBg.png")
        bg = bg.resize((1280, 650), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(bg)

        f_Lable = Label(self.root, image=self.photoimg)
        f_Lable.place(x=0, y=0, width=1280, height=650)

        # =======================================Row 1==============================
        self.var_user = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_pass = StringVar()
        self.var_choice1 = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_dob = StringVar()
        self.var_choice = StringVar()
        self.var_answer = StringVar()


        User = Label(f_Lable,text="Username ",font=("times new roman" ,20,"bold"),bg="black",fg ="gold")
        User.place(x=80,y=120,width=140,height=30)

        self.txt_user=Entry(f_Lable,textvariable=self.var_user,font=("times new roman",15) , bg="white",fg="black")
        self.txt_user.place(x=80,y=160,width=240)

        # =====================================Search Button==========================
        self.search_button = Button(f_Lable, text="Search", font=("times new roman", 15), bg="blue", fg="white", cursor="hand2",command=self.search)
        self.search_button.place(x=750, y=140, width=140, height=40)

        # ===================================Row 1====================
        f_name = Label(f_Lable, text="First Name ", font=("times new roman", 20, "bold"),bg="black",fg ="gold")
        f_name.place(x=450, y=120, width=140, height=30)

        self.txt_fname = Entry(f_Lable,textvariable=self.var_fname, font=("times new roman", 15), bg="white", fg="black")
        self.txt_fname.place(x=450, y=160,width=240)

        # =======================================Row 2==============================
        l_name = Label(f_Lable, text="Last Name", font=("times new roman", 20, "bold"), bg="black",fg ="gold")
        l_name.place(x=80, y=200, width=120, height=30)

        self.txt_lname = Entry(f_Lable,textvariable=self.var_lname, font=("times new roman", 15), bg="white", fg="black")
        self.txt_lname.place(x=80, y=240, width=240)

        Pass = Label(f_Lable, text="Password", font=("times new roman", 20, "bold"), bg="black",fg ="gold")
        Pass.place(x=450, y=200, width=120, height=30)

        self.txt_pass = Entry(f_Lable,textvariable=self.var_pass, font=("times new roman", 15), bg="white", fg="black")
        self.txt_pass.place(x=450, y=240, width=240)

        # =======================================Row 3==============================
        gender = Label(f_Lable, text="Gender", font=("times new roman", 20, "bold"),bg="black",fg ="gold")
        gender.place(x=80, y=280, width=100, height=30)

        self.choice1 = ttk.Combobox(f_Lable, textvariable=self.var_choice1,font=("times new roman", 15), state="readonly", justify=CENTER)
        self.choice1["values"] = ("Select", "Male", "Female")
        self.choice1.place(x=80, y=320, width=240)
        self.choice1.current(0)

        email = Label(f_Lable, text="Email Id", font=("times new roman", 20, "bold"), bg="black",fg ="gold")
        email.place(x=450, y=280, width=100, height=30)

        self.txt_email = Entry(f_Lable,textvariable=self.var_email, font=("times new roman", 15), bg="white", fg="black")
        self.txt_email.place(x=450, y=320, width=240)

        # =======================================Row 4==============================
        phone_no = Label(f_Lable, text="Phone No", font=("times new roman", 20, "bold"),bg="black",fg ="gold")
        phone_no.place(x=80, y=360, width=120, height=30)

        self.txt_phone = Entry(f_Lable,textvariable=self.var_phone, font=("times new roman", 15), bg="white", fg="black")
        self.txt_phone.place(x=80, y=400, width=240)

        DOB = Label(f_Lable, text="DOB", font=("times new roman", 20, "bold"), bg="black",fg ="gold")
        DOB.place(x=450, y=360, width=60, height=30)

        self.txt_dob = Entry(f_Lable, textvariable=self.var_dob,font=("times new roman", 15), bg="white", fg="black")
        self.txt_dob.place(x=450, y=400, width=240)

        # =======================================Row 5==============================
        security_que = Label(f_Lable, text="Security Question", font=("times new roman", 20, "bold"),bg="black",fg ="gold")
        security_que.place(x=80, y=440, width=210, height=30)

        self.choice = ttk.Combobox(f_Lable,textvariable=self.var_choice, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.choice["values"] = ("select", "Your pet name", "Your School name", "Your Favorite colour", "Your Favorite Place")
        self.choice.place(x=80, y=480, width=240)
        self.choice.current(0)

        answer = Label(f_Lable, text="Answer", font=("times new roman", 20, "bold"),bg="black",fg ="gold")
        answer.place(x=450, y=440, width=100, height=30)

        self.txt_answer = Entry(f_Lable,textvariable=self.var_answer, font=("times new roman", 15), bg="white", fg="black")
        self.txt_answer.place(x=450, y=480, width=240)

    def search(self):
        User_id = self.var_user.get()
        if User_id == " ":
              messagebox.showerror("error", "no record found", parent=self.root)
        else:
            con = mysql.connector.connect(host="localhost", port=3306, user="root", password="1234", database="quizguruteam")
            cur = con.cursor()
            cur.execute("select * from reg where user ='" + User_id + "'")
            rows = cur.fetchall()
            for row in rows:
                self.var_fname.set(row[0])
                self.var_lname.set(row[1])
                self.var_pass.set(row[3])
                self.var_choice1.set(row[4])
                self.var_email.set(row[5])
                self.var_phone.set(row[6])
                self.var_dob.set(row[7])
                self.var_choice.set(row[8])
                self.var_answer.set(row[9])
            con.close()




if __name__== "__main__":
    root=Tk()
    obj=profile(root)
    root.mainloop()
