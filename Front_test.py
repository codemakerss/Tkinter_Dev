from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk

def drop_box(sth):
    lst_box.insert("end", sth.data)
    pass
def drop_file(sth):
    pass

root = TkinterDnD.Tk()
root.geometry("800x800")

lst_box = tk.Listbox(root, selectmode=tk.SINGLE, background="#ffe0d6")
lst_box.pack(fill=tk.X)
lst_box.drop_target_register(DND_FILES)
lst_box.dnd_bind("<<Drop>>", drop_box)

# text_box = tk.Text(root)
# text_box.pack()
# text_box.drop_target_register(DND_FILES)
# text_box.dnd_bind("<<Drop>>", drop_file())

root.mainloop()