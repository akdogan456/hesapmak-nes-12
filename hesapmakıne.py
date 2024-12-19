import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hesap makinesi-faruk")# çalışınca pencerenın ustunde cıkar
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_446=tk.Button(root)
        GButton_446["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_446["font"] = ft
        GButton_446["fg"] = "#000000"
        GButton_446["justify"] = "center"
        GButton_446["text"] = "-"# butonun ustune yazmak veya ıstedıgın işlem için
        GButton_446.place(x=110,y=390,width=70,height=25)#width button genişliği
        GButton_446["command"] = self.GButton_446_command

        GButton_84=tk.Button(root)
        GButton_84["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_84["font"] = ft
        GButton_84["fg"] = "#000000"
        GButton_84["justify"] = "center"
        GButton_84["text"] = "+"
        GButton_84.place(x=220,y=390,width=70,height=25)
        GButton_84["command"] = self.GButton_84_command

        GButton_224=tk.Button(root)
        GButton_224["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_224["font"] = ft
        GButton_224["fg"] = "#000000"
        GButton_224["justify"] = "center"
        GButton_224["text"] = "*"
        GButton_224.place(x=330,y=390,width=70,height=25)
        GButton_224["command"] = self.GButton_224_command

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "/"
        GButton_265.place(x=430,y=390,width=70,height=25)
        GButton_265["command"] = self.GButton_265_command

        GLineEdit_157=tk.Entry(root)
        GLineEdit_157["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_157["font"] = ft
        GLineEdit_157["fg"] = "#333333"
        GLineEdit_157["justify"] = "center"
        GLineEdit_157["text"] = "Entry"
        GLineEdit_157.place(x=100,y=230,width=70,height=25)

        GLineEdit_141=tk.Entry(root)
        GLineEdit_141["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_141["font"] = ft
        GLineEdit_141["fg"] = "#333333"
        GLineEdit_141["justify"] = "center"
        GLineEdit_141["text"] = "Entry"
        GLineEdit_141.place(x=220,y=240,width=70,height=25)

        GLineEdit_634=tk.Entry(root)
        GLineEdit_634["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_634["font"] = ft
        GLineEdit_634["fg"] = "#333333"
        GLineEdit_634["justify"] = "center"
        GLineEdit_634["text"] = "Entry"
        GLineEdit_634.place(x=340,y=260,width=70,height=25)

        GLineEdit_502=tk.Entry(root)
        GLineEdit_502["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_502["font"] = ft
        GLineEdit_502["fg"] = "#333333"
        GLineEdit_502["justify"] = "center"
        GLineEdit_502["text"] = "Entry"
        GLineEdit_502.place(x=440,y=280,width=70,height=25)

        GLabel_493=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_493["font"] = ft
        GLabel_493["fg"] = "#333333"
        GLabel_493["justify"] = "center"
        GLabel_493["text"] = "rakam1"
        GLabel_493.place(x=100,y=160,width=70,height=25)

        GLabel_201=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_201["font"] = ft
        GLabel_201["fg"] = "#333333"
        GLabel_201["justify"] = "center"
        GLabel_201["text"] = "rkm2"
        GLabel_201.place(x=200,y=170,width=70,height=25)

        GLabel_432=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_432["font"] = ft
        GLabel_432["fg"] = "#333333"
        GLabel_432["justify"] = "center"
        GLabel_432["text"] = "rkm3"
        GLabel_432.place(x=340,y=190,width=70,height=25)

        GLabel_377=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "rkm4"
        GLabel_377.place(x=430,y=210,width=70,height=25)

    def GButton_446_command(self):
        print("button 1 calıstı")


    def GButton_84_command(self):
        print("button 2 calıstı")


    def GButton_224_command(self):
        print("button 3 calıstı")


    def GButton_265_command(self):
        print("button 4 calıstı")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    #buraya asagıdakılerı ekledım
    textBoxYazilanlar1 = tk.StringVar()
    textBoxYazilanlar2 = tk.StringVar()
    textBoxYazilanlar3 = tk.StringVar()

    root.mainloop()
