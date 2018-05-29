from Tkinter import *
from tkMessageBox import *

class Entrydemo(Frame):
    def __init__(self):

        Frame.__init__(self)
        self.pack( expand = YES, fill = BOTH )
        self.master.title("ENTRY COMPONENTS")
        self.master.geometry("500x200" )

        self.frame1=Frame(self)
        self.frame1.pack(pady=30)

        self.entry1=Entry(self.frame1,name="text1")

        self.entry1.bind("<Return>",self.showcontents)
        self.entry1.pack(side=LEFT, padx=5)

        self.entry2=Entry(self.frame1,name="text2")
        self.entry2.insert(INSERT,"ENTER TEXT HERE")

        self.entry2.bind("<Return>",self.showcontents)
        self.entry2.pack(side=LEFT , padx=5)

        self.frame2=Frame(self)
        self.frame2.pack(pady=30)

        self.entry3=Entry(self.frame2,name="text3")
        self.entry3.insert(INSERT,"UNEDITABLE TEXT")
        
        self.entry3.config(state=DISABLED)
        self.entry3.bind("<Return>",self.showcontents)
        self.entry3.pack(side=LEFT , padx=5)

        self.entry4=Entry(self.frame2,name="text4",show="*")
        self.entry4.insert(INSERT,"HIDDEN TEXT")
        
        
        self.entry4.bind("<Return>",self.showcontents)
        self.entry4.pack(side=LEFT , padx=5)

    def showcontents(self,event):
        name_=event.widget.winfo_name()
        content_=event.widget.get()
        showinfo("MESSAGE" , name_ + "  :  "+content_)

Entrydemo().mainloop()
      
