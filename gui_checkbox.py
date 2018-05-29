from Tkinter import *

class Checkbuttons(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand= YES , fill=BOTH)
        self.master.title("CLICK ANY NUMBER OF CHECKBOXES")

        self.frame1=Frame(self)
        self.frame1.pack()

        self.text=Entry(self.frame1 , font="Arail 10" , width =60)
        self.text.insert(INSERT , "ENETR YOUR TEXT HERE ")
        self.text.pack(side=LEFT , pady=10)

        self.frame2=Frame(self)
        self.frame2.pack()

        self.boldvar = BooleanVar()
        self.bold=Checkbutton(self.frame2 , text="BOLD" , command=self.changefont , variable=self.boldvar)
        self.bold.pack(side=LEFT , padx=10)

        self.italicvar = BooleanVar()
        self.italic=Checkbutton(self.frame2 , text="ITALIC" , command=self.changefont , variable=self.italicvar)
        self.italic.pack(side=LEFT , padx=10)


    def changefont(self):

        font_="Arial 10"                # capital and lower cases in Arial , bold and italic and space in bold and italic        
        if (self.boldvar.get()):

            font_+=" bold"

        if (self.italicvar.get()):

            font_+=" italic"

            
        self.text.config(font = font_)
   
Checkbuttons().mainloop()
