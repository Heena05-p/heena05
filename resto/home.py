from tkinter import*
from PIL import Image,ImageTk
class home:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="White")
        #mbg
        self.Mbg_img = Image.open("background.jpg")
        self.Mbg_img = self.Mbg_img.resize((1350,758), Image.Resampling.LANCZOS)
        self.Mbg_img = ImageTk.PhotoImage(self.Mbg_img)
        frame= LabelFrame(self.root, bg="white")
        frame.place(x=0, y=0, width=1350, height=758)
        Label(frame, image=self.Mbg_img, bg="white").pack()
        #bg
        self.BG_img = Image.open("hotel.jpg")
        self.BG_img = self.BG_img.resize((1200,480), Image.Resampling.LANCZOS)
        self.BG_img = ImageTk.PhotoImage(self.BG_img)
        frame= LabelFrame(self.root, bg="white")
        frame.place(x=80, y=20, width=1200, height=480)
        Label(frame, image=self.BG_img, bg="white").pack()
        #frame
       # M_Frame=LabelFrame(self.root,font=("times new roman",15),bg="lightgrey")
       # M_Frame.place(x=5,y=0,width=1350,height=50)
        #button
        btn_Home=Button(self.root,text="Home",font=("goudy old style",15,"bold"),bg="#F00B0B",fg="white",cursor="hand2").place(x=50,y=5,width=200,height=40)
        btn_Menu=Button(self.root,text="Menu",font=("goudy old style",15,"bold"),bg="#F00B0B",fg="white",cursor="hand2").place(x=300,y=5,width=200,height=40)
        btn_Location=Button(self.root,text="Location",font=("goudy old style",15,"bold"),bg="#F00B0B",fg="white",cursor="hand2").place(x=550,y=5,width=200,height=40)
        btn_Contact=Button(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="#F00B0B",fg="white",cursor="hand2").place(x=800,y=5,width=200,height=40)
        btn_Room=Button(self.root,text="Room Enquiry",font=("goudy old style",15,"bold"),bg="#F00B0B",fg="white",cursor="hand2").place(x=1050,y=5,width=200,height=40)
        #b1
        self.b1_img = Image.open("pizza.webp")
        self.b1_img = self.b1_img.resize((200,133), Image.Resampling.LANCZOS)
        self.b1_img = ImageTk.PhotoImage(self.b1_img)
        frame1 = LabelFrame(self.root, bg="white")
        frame1.place(x=830, y=510, width=200, height=133)
        Label(frame1, image=self.b1_img, bg="white").pack()
        #b2
        self.b2_img = Image.open("pasta.jpg")
        self.b2_img = self.b2_img.resize((200,133), Image.Resampling.LANCZOS)
        self.b2_img = ImageTk.PhotoImage(self.b2_img)
        frame2 = LabelFrame(self.root, bg="white")
        frame2.place(x=330, y=510, width=200, height=133)
        Label(frame2, image=self.b2_img, bg="white").pack()
        #b3
        self.b3_img = Image.open("noodle.webp")
        self.b3_img = self.b3_img.resize((200,133), Image.Resampling.LANCZOS)
        self.b3_img = ImageTk.PhotoImage(self.b3_img)
        frame3 = LabelFrame(self.root, bg="white")
        frame3.place(x=580, y=510, width=200, height=133)
        Label(frame3, image=self.b3_img, bg="white").pack()
        #b4
        self.b4_img = Image.open("noodd.jpg")
        self.b4_img = self.b4_img.resize((200,133), Image.Resampling.LANCZOS)
        self.b4_img = ImageTk.PhotoImage(self.b4_img)
        frame4 = LabelFrame(self.root, bg="white")
        frame4.place(x=1080, y=510, width=200, height=133)
        Label(frame4, image=self.b4_img, bg="white").pack()
        #b5
        self.b5_img = Image.open("paneer.webp")
        self.b5_img = self.b5_img.resize((200,133), Image.Resampling.LANCZOS)
        self.b5_img = ImageTk.PhotoImage(self.b5_img)
        frame5 = LabelFrame(self.root, bg="white")
        frame5.place(x=80, y=510, width=200, height=133)
        Label(frame5, image=self.b5_img, bg="white").pack()
        
        
        #footer
        footer=Label(self.root, text="ANY ISSUE CONTACT:\n 7019651787", font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)











root=Tk()
obj=home(root)
root.mainloop()