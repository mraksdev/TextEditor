from tkinter import *

root = Tk()
root.title("Notebook")
root.geometry("500x500")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file="icon.png"))

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

textinfo = Text(root, yscrollcommand=scrollbar.set)
textinfo.pack(expand=True, fill=BOTH)

scrollbar.config(command=textinfo.yview)

root.config(menu=menu_bar)

root.mainloop()