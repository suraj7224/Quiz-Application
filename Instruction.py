from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow

class instruction():

    def __init__(self,root):
        self.root=root
        self.root.title("Instruction")
        self.root.geometry("1280x675+252+202")
        self.root.resizable(False,False)
        self.root.config(background="White")

        #================================= background image==============================
        bg = Image.open("image\Dash_bg.jpeg")
        bg = bg.resize((1280, 650), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg)

        f_Lable = Label(self.root, image=self.photoimg1)
        f_Lable.place(x=0, y=0, width=1280, height=650)

        # ============================Quiz ninja Welcome Lable======================================
        txt_label1=Label(self.root, text="Welcome To Quiz Guru!!!!Read The Given Instruction Carefully. ",font=("times new roman",20,"bold"),bg="lightblue",fg="black")
        txt_label1.place(x=0,y=10,width=1250,height=40)


        # ======================================Final Instruction==================================
        txt_label1=Label(self.root, text="For Attempting the quiz . ",font=("times new roman",20,"bold"),bg="pink",fg="Red")
        txt_label1.place(x=0,y=60,width=1250,height=40)

        txt_label1=Label(self.root, text="Step 1 -> ",font=("times new roman",20,"bold"),bg="pink",fg="black")
        txt_label1.place(x=0,y=110,width=120,height=40)

        txt_label1=Label(self.root, text="Go to the take test.",font=("times new roman",20,"bold"),bg="black",fg="gold")
        txt_label1.place(x=120,y=110,width=220,height=40)

        txt_label1 = Label(self.root, text="Step 2 -> ", font=("times new roman", 20, "bold"), bg="pink", fg="black")
        txt_label1.place(x=0, y=160, width=120, height=40)

        txt_label1 = Label(self.root, text="Select the subject/ topic for the test.", font=("times new roman", 20, "bold"), bg="black",fg="gold")
        txt_label1.place(x=120, y=160, width=420, height=40)

        txt_label1 = Label(self.root, text="Step 3 -> ", font=("times new roman", 20, "bold"), bg="pink", fg="black")
        txt_label1.place(x=0, y=210, width=120, height=40)

        txt_label1 = Label(self.root, text="Click Start Test to attempt the quiz.", font=("times new roman", 20, "bold"), bg="black",fg="gold")
        txt_label1.place(x=120, y=210, width=420, height=40)

        txt_label1 = Label(self.root, text="Step 4 -> ", font=("times new roman", 20, "bold"), bg="pink", fg="black")
        txt_label1.place(x=0, y=260, width=120, height=40)

        txt_label1 = Label(self.root, text="Click on Next button to move next question.Please note that you will not be \nable to go back to any of the previous question after clicking Next button.", font=("times new roman", 20, "bold"), bg="black",fg="gold")
        txt_label1.place(x=120, y=260, width=880, height=80)

        txt_label1 = Label(self.root, text="Step 5 -> ", font=("times new roman", 20, "bold"), bg="pink", fg="black")
        txt_label1.place(x=0, y=350, width=120, height=40)

        txt_label1 = Label(self.root, text="Click on Submit Test button on completion of the quiz. ", font=("times new roman", 20, "bold"), bg="black",fg="gold")
        txt_label1.place(x=120, y=350, width=650, height=40)

        txt_label1 = Label(self.root, text="Step 6 -> ", font=("times new roman", 20, "bold"), bg="pink", fg="black")
        txt_label1.place(x=0, y=400, width=120, height=40)

        txt_label1 = Label(self.root, text="You can not return back to test after submitting the test.", font=("times new roman", 20, "bold"), bg="black",fg="gold")
        txt_label1.place(x=120, y=400, width=660, height=40)










if __name__== "__main__":
    root=Tk()
    obj=instruction(root)
    root.mainloop()