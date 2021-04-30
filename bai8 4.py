from tkinter import*
def NewFile():
    print("New File!")
def About():
    print("this is a simple example of a menu")
root = Tk(root)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(Label("file"),menu=filemenu)
filemenu.add_command(label="new", command=Newfile)
filenemu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_casade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
mainloop()