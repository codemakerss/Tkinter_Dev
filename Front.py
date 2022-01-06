from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Interface(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)   
        self.parent = parent
        self.UI()
        self.callback()
    
    def UI(self):
        self.parent.title("TEST")
        self.parent.geometry("700x700")
        style = ttk.Style()
        style.theme_use("aqua")

        

        ttk.Label(self.parent, text = 'Input something :', font=('calibre',25, 'bold')).place(x=40,y=60)
        ttk.Entry(self.parent, font=('calibre',25,'normal')).place(x=245,y=60)
    
    def callback(self, input):
        if input.isdigit():
            print(input)
            return True
                            
        elif input is "":
            print(input)
            return True

        else:
            print(input)
            return False



    
if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()