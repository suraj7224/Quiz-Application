from tkinter import *
from tkinter import ttk
# from tkcalendar import *
from PIL import Image,ImageTk  #pip install pillow

class Aboutus():
    def __init__(self,root):
        self.root=root
        self.root.title("About Us")
        self.root.geometry("1280x675+252+202")
        self.root.resizable(False, False)
        self.root.config(background="White")

        # ==========================image here==================================
        bg = Image.open("image\AboutUs.jpeg")
        bg = bg.resize((1280, 650), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg)

        f_Lable = Label(self.root, image=self.photoimg1)
        f_Lable.place(x=0, y=0, width=1280, height=650)


if __name__=="__main__":
    root=Tk()
    obj=Aboutus(root)
    root.mainloop()


