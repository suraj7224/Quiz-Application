import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import random
import smtplib
import mysql
import mysql.connector
from plyer import notification

class Test():
    global indexes ,questions,answer_choice,answers,user_answer,ques,radiovar, lblQuestion, r1, r2, r3, r4, ques, txt_label7,txt_label,score,email
    def __init__(self,root):
        self.root=root
        self.root.title("Take Test")
        self.root.geometry("1280x675+252+202")
        self.root.resizable(False, False)
        self.root.config(background="White")

        # ================================= background image==============================
        bg = Image.open("image\Dash_bg.jpeg")
        bg = bg.resize((1280, 650), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg)

        f_Lable = Label(self.root, image=self.photoimg1)
        f_Lable.place(x=0, y=0, width=1280, height=650)

        # ==================Top image===============================
        logo = Image.open("image\Logo.jpeg")
        logo = logo.resize((150, 120), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(logo)

        self.f_Lable = Label(root, image=self.photoimg)
        self.f_Lable.place(x=580, y=20, width=150, height=120)

        # =======================Instuction about Quiz================================

        self.txt_label5 = Label(self.root, text="Read these instruction carefully ", font=("times new roman", 20, "bold"), bg="white",fg="blue")
        self.txt_label5.place(x=430, y=150, width=420, height=40)

        self.txt_label1 = Label(self.root, text="1) There are a total 10 questions.", font=("times new roman", 20, "bold"),bg="white")
        self.txt_label1.place(x=430, y=200, width=400, height=40)

        self.txt_label2 = Label(self.root, text="2) Each question carries one mark.", font=("times new roman", 20, "bold"),bg="white")
        self.txt_label2.place(x=430, y=250, width=420, height=40)

        self.txt_label3 = Label(self.root, text="3) No negative marking for wrong answers.", font=("times new roman", 20, "bold"),bg="white")
        self.txt_label3.place(x=430, y=300, width=510, height=40)

        self.txt_label4 = Label(self.root, text="4) Questions are of Multiple Choice type.", font=("times new roman", 20, "bold"),bg="white")
        self.txt_label4.place(x=430, y=350, width=480, height=40)

        self.txt_label6 = Label(self.root, text="Click Take Test once you are ready.", font=("times new roman", 20, "bold"), bg="white",fg="Red")
        self.txt_label6.place(x=430, y=400, width=450, height=40)

        # ======================Button for Take Test============================
        self.test_btn = Button(self.root, text="Take Test", font=("times new roman", 20, "bold"), border=1, fg="gold", bg="black",relief=SUNKEN, command=self.startIsPressed)
        self.test_btn.place(x=580, y=480, width=120, height=40)

    def startIsPressed(self):
        self.f_Lable.destroy()
        self.txt_label1.destroy()
        self.txt_label2.destroy()
        self.txt_label3.destroy()
        self.txt_label4.destroy()
        self.txt_label5.destroy()
        self.txt_label6.destroy()
        self.test_btn.destroy()
        self.gen()
        self.start_Quiz()

    questions = [
        "Which of the following signals are sent to the processs when a user presses Control + C in the shell?",
        "Which of the following is abstracted by operating system?",
        "What are the standard file descriptor numbers for STDERR, STDIN, and STDOUT?",
        "Which part of a process is used for dynamic memory allocation?",
        "The smallest integer that can be represented by an 8-bit number in 2’s complement form is :",
        "The total number of inputs for a single bit full adder is:",
        "If A and B are the 2 inputs of a half adder, the sum is given by,",
        "Representation of hexadecimal (6DE)16  in decimal ",
        "2’s complement of the binary number 111 is:",
        " The length of a register is called a ___________", ]

    answer_choice = [
        [ "SIGINT","SIGTERM","SIGKILL","SIGQUIT"],
        ["Processor" ,"Memory","Network Cards","All of the above"],
        ["0,1,2","2,0,3", "1,2,3","Randomly decide"],
        ["Code Segment","Stack","Heap","Data Segment"],
        ["-256", "-128", "-127", "0"],
        ["1", "2", "3", "4"],
        [" A XOR B", " A AND B", " A OR B", " A XNOR B"],
        ["1756", "1758", "1760", "1754"],
        ["010", "001", "000", "111"],
        ["word limit", "register limit", "word size", "working limit"],
    ]

    answers = [0, 3, 1, 2, 3, 2, 0, 1, 1, 2]
    user_answer = []
    indexes = []

    def gen(self):
        global indexes
        while (len(indexes) < 5):
            x = random.randint(0, 9)
            indexes.append(x)
            if x in indexes:
                continue
            else:
                indexes.append(x)


    def mail(self):
        global txt_label, score, email
        User_id = self.var_user.get()
        try:

            if User_id == " ":
                messagebox.showerror("error", "no record found", parent=self.root)
            else:
                con = mysql.connector.connect(host="localhost", port=3306, user="root", password="1234",database="quizguruteam")
                cur = con.cursor()
                cur.execute("select * from reg where user ='" + User_id + "'")
                rows = cur.fetchall()
                con.close()
                for a in rows:
                    email = a[5]
                    sender_mail = ""                   #Add here your mail in the parenthesses
                    sender_password = ""               #Add here your password in the parenthesses
                    rec_mail = email
                    print(rec_mail)
                    message = f"Welcome to Quiz Guru \nCongratulations, You have Successfully submitted Test on Quiz Guru!! \nYour score is {self.score} /25\n\n Hey,Keep Guru happy!\n Remember that learning requires a little bit of practice every day.\nThank You."
                    if rec_mail == " ":
                       messagebox.showerror("Error", "All Fields Required", parent=self.root)
                    else:
                       server = smtplib.SMTP('smtp.gmail.com', 587)
                       server.starttls()
                       server.login(sender_mail, sender_password)
                       print("Send Email")
                       server.sendmail(sender_mail, rec_mail, message)
                       print("Email has been send to reciver", rec_mail)
                       title = "Quiz Guru"
                       message = "Email has been send Successfully on Your mail.\nThank You"
                       notification.notify(
                                        title=title,
                                        message=message,
                                        app_icon=None,
                                        timeout=5,
                                        toast=False
                                    )
        except Exception as ae:
              messagebox.showerror("Error", f"Error due to ths str{ae}", parent=self.root)

    def showresult(self, score):
        global txt_label, txt_user
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        lblimage = Label(
            self.root,
            bg="White",
        )
        lblimage.pack()
        lblresulttext = Label(
            self.root,
            font=("times new roman ", 20),
            bg="White",
        )
        lblresulttext.pack()
        self.var_user = StringVar()
        # User ID

        User = Label(self.root, text="Username ", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        User.place(x=20, y=120, width=140, height=30)

        self.txt_user = Entry(self.root, textvariable=self.var_user, font=("times new roman", 20), bg="white",fg="black")
        self.txt_user.place(x=20, y=160, width=200,height=40)

        email_button = Button(self.root, text="Send", font=("times new roman", 20, "bold"), fg="gold", bg="black",command=self.mail)
        email_button.place(x=240, y=160, width=140, height=40)

        if self.score >= 20:
            img = PhotoImage(file="image\Excellent.png")
            lblimage.configure(image=img)
            lblimage.image = img
            email_button.configure(command=self.mail)
            lblresulttext.configure(text=f"You are Excellent !!!! Your score is {score} .\nThank You.")
        elif (self.score >= 10 and self.score < 20):
            img = PhotoImage(file="image\Good.png")
            lblimage.configure(image=img)
            lblimage.image = img
            email_button.configure(command=self.mail)
            lblresulttext.configure(text=f"You Can Be Better. Your Score is {score}.\nThank You.")
        else:
            img = PhotoImage(file="image\Fail.png")
            lblimage.configure(image=img)
            lblimage.image = img
            email_button.configure(command=self.mail)
            lblresulttext.configure(text=f"You Should Work Hard!!!! Your Score is {score}.\nThank You.")




    def calc(self):
        global indexes, user_answer, answers
        x = 0
        self.score = 0
        for i in indexes:
            if user_answer[x] == answers[i]:
                self.score += 5
            x += 1
        print(self.score)
        self.showresult(self.score)

    ques = 1

    def selected(self):
        global radiovar, user_answer, lblQuestion, r1, r2, r3, r4, ques, txt_label7

        x = radiovar.get()
        user_answer.append(x)
        radiovar.set(-1)
        if ques < 5:
            lblQuestion.config(text=questions[indexes[ques]])
            r1['text'] = answer_choice[indexes[ques]][0]
            r2['text'] = answer_choice[indexes[ques]][1]
            r3['text'] = answer_choice[indexes[ques]][2]
            r4['text'] = answer_choice[indexes[ques]][3]
            ques += 1
        else:
            self.txt_label7.destroy()
            self.calc()


    def start_Quiz(self):
        global lblQuestion, r1, r2, r3, r4, txt_label7

        self.txt_label7 = Label(self.root, text="Welcome To This Quiz Guru", font=("times new roman", 20), justify="center",bg="black", fg="gold")
        self.txt_label7.place(x=0, y=0, width=1280, height=40)


        lblQuestion = Label(
            self.root,
            text=questions[indexes[0]],
            font=("times new roman", 15, "bold"),
            width=500,
            justify="center",
            wraplength=400,
            bg="white",
            fg="Red",
        )
        lblQuestion.pack(pady=(100, 30))

        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)

        r1 = Radiobutton(
            self.root,
            text=answer_choice[indexes[0]][0],
            font=("Times", 15),
            value=0,
            variable=radiovar,
            command=self.selected,
            bg="white",
            fg="blue",
        )
        r1.pack(pady=5)

        r2 = Radiobutton(
            self.root,
            text=answer_choice[indexes[0]][1],
            font=("Times", 15),
            value=1,
            variable=radiovar,
            command=self.selected,
            bg="white",
            fg="blue",
        )
        r2.pack(pady=5)

        r3 = Radiobutton(
            self.root,
            text=answer_choice[indexes[0]][2],
            font=("Times", 15),
            value=2,
            variable=radiovar,
            command=self.selected,
            bg="white",
            fg="blue",
        )
        r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=answer_choice[indexes[0]][3],
            font=("Times", 15),
            value=3,
            variable=radiovar,
            command=self.selected,
            bg="white",
            fg="blue",
        )
        r4.pack(pady=5)


if __name__== "__main__":
    root=Tk()
    obj=Test(root)
    root.mainloop()
