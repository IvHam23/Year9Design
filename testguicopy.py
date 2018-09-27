'''
testgui.py - basic ugly gui
ilee - original coding, Sept. 21, 2018
'''
from tkinter import *
master = Tk()
master.config(background="blue")
label = Label(master, text="Hockey Pool")
label.config(background="blue")
label.config(foreground="white")
label.pack()
button = Button(master, text="QUIT", fg="red", command=quit)
button.pack(side=BOTTOM)
listbox = Listbox(master)
listbox.config(background="blue")
listbox.config(foreground="white")
listbox.pack()
listbox.insert(END, "Player, Goals")
lst = [["connor mcdavid", 208], ["sidney crosby", 234], ["steven stamkos", 187], ["auston matthews", 70]]
for item in lst:
    listbox.insert(END, item[0] + "-" + str(item[1]))
    
mainloop()