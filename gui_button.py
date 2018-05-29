from Tkinter import *
from tkMessageBox import *

class Buttondemo(Frame):

    def __init__(self):

        Frame.__init__(self)

        self.pack( expand=YES , fill=BOTH)
        self.master.title("CLICK SOMETHING")

        self.button1=Button( self, text="TEXT BUTTON" , command=self.textbutton)
        self.button1.bind("<Enter>",self.rolloverenter)
        self.button1.bind("<Leave>",self.rolloverleave)
        self.button1.pack(side=LEFT , pady=30)

        self.image_=PhotoImage( file = "php.gif")
        self.button2=Button(self, image = self.image_ , command=self.imagebutton)
        self.button2.bind("<Enter>",self.rolloverenter)
        self.button2.bind("<Leave>",self.rolloverleave)
        self.button2.pack(side=LEFT , padx=30)

    def textbutton(self):
        showinfo("MESSAGE", "YOU CHOOSE A TEXT BUTTON")

    def imagebutton(self):
        showinfo("MESSAGE", "YOU CHOOSE A IMAGE BUTTON")

    def rolloverenter(self,event):
        event.widget.config(relief=GROOVE)

    def rolloverleave(self,event):
        event.widget.config(relief=RAISED)

Buttondemo().mainloop()
        
