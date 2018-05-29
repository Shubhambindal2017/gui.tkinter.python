from Tkinter import *
class Labeldemo(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack( expand = NO , fill = NONE)
        self.master.title("Labels")

        self.Label1 = Label(self,text="hello ")

        self.Label1.pack()
        self.Label2=Label(self,text="How are YOU")

        self.Label2.pack(side=LEFT)

        self.Label3=Label(self,bitmap="questhead")
        self.Label3.pack(side=LEFT)

 #   def main():
Labeldemo().mainloop()

#if __name__=="__main__":
#    main()
