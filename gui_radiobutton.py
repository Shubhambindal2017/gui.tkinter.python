from Tkinter import *
from tkMessageBox import *
class Radio(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES , fill=BOTH)
        self.master.title("RADIO BUTTONS")

        self.frame1=Frame(self)
        self.frame1.pack()

        self.text=Entry(self.frame1,width=60,font="Arial 10")
        self.text.insert(INSERT, "ENTER YOUR TEXT HERE")
        self.text.pack(side=LEFT , pady=10 , padx=10)

        self.frame2=Frame(self)
        self.frame2.pack()

        Radiolist=["Plain","Bold","Italic","Bold/Italic"]

        self.var_=StringVar()

        self.var_.set(Radiolist[0])
        for i in Radiolist:

            self.radio_obj=Radiobutton(self.frame2,text=i,variable=self.var_,value=i,command=self.changeFont)
            self.radio_obj.pack(side=LEFT , padx=40)

    def changeFont(self):
        desired_font="Arial 10"

        if(self.var_.get()=="Bold"):
            desired_font+=" bold"

        if(self.var_.get()=="Italic"):
            desired_font+=" italic"

        if(self.var_.get()=="Bold/Italic"):
            desired_font+=" bold italic"

        self.text.config(font=desired_font)

Radio().mainloop()
