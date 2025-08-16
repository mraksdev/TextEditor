from tkinter import *
from tokenize import tabsize

root = Tk()
root.title("Notebook")
root.geometry("500x500")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file="icon.png"))

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

textinfo = Text(root, yscrollcommand=scrollbar.set)
textinfo.pack(expand=True, fill=BOTH)
textinfo.config(
    wrap=NONE,
    font="Consolas 11",
)

scrollbar.config(command=textinfo.yview)

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: textinfo.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: textinfo.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: textinfo.event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)

root.mainloop()