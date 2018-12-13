from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
            content = BeautifulSoup(site.content, 'html.parser')                    
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)

def addPlayerToList(evt):
    global players
    name = variable.get()
    if players.count(name) > 0:
        return
    listbox.insert(END, name)
    for i in range(listbox.size()):
        players.append(listbox.get(i))

def createlistbox(value):
    var=listbox.get(ANCHOR)
    if var!=NONE:
        dTag = content.find(attrs={"csk":var})
        parent = dTag.findParent("tr")
        points = int(parent.contents[8].text)
        games = int(parent.contents[5].text)
        team = str(parent.contents[3].text)
        position = str(parent.contents[4].text)
        goals = int(parent.contents[6].text)
        assists = int(parent.contents[7].text)
    listbox2 = Listbox(root, width=23, height=20)
    listbox2.place(x=227, y=426)
    listbox2.insert(END, 'Players Stats: ')
    listbox2.insert(END, "Points: " + str(points))
    listbox2.insert(END, "Goals:" + str(goals))
    listbox2.insert(END, "Assists:" + str(assists))
    listbox2.insert(END, "Team:"+ team)
    listbox2.insert(END,"Position: " + position)
        
def selected(evt):
    global player
    playerLabel.place(x=200, y=405)
    teamLabel.place(x=200, y=430)
    pointsLabel.place(x=200, y=455)
    goalsLabel.place(x=200, y=480)
    assistsLabel.place(x=200, y=505)

def switchPhoto(value):
    fullname = listbox.get(ACTIVE)
    full_list = fullname.split(",")
    first = full_list[1]
    last = full_list[0]
    filename = "headshots/" + last[0:5] + first[0:2] + "01.jpg"
    global photo2
    my_image = Image.open(filename.lower())
    photo2 = ImageTk.PhotoImage(my_image)
    can2.itemconfig(myimg2, image=photo2)
    
def updatelab():
    lstprint = ""
    for item in lst:
        lstprint = lstprint + item + "\n"
    mylab.configure(text=lstprint)

def addItem():
    item = entry.get()
    if (lst.count(item) == 0):
        lst.append(item)
        entry.delete(0, END)
        updatelab()
        listbox.insert(END, item)

def removeItem():
    items = listbox.curselection()
    pos = 0
    for i in items:
        x = int(i) - pos
        listbox.delete(x, x)
        pos = pos + 1

def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayer.txt", "Players saved to disk")
    
lst = []
assists = []
goals = []
points = []
lstprint = ""
totalpts = 0
players = []
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

root = Tk()
root.geometry("645x1000+0+0")
root.title("Hockey Pool")
root.config(background="cyan2")

if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99

can = Canvas(root, width=615, height=400)
can.grid(row=0, column=0, padx=10, pady=10)
image1 = Image.open("CP.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(450, 150, 500, 200, fill="blue4", outline="#DDD", width=4)
can.create_text(475, 175, text="HP", fill="orangered")

instlab = Label(root,text="Input(Last,First)")
instlab.place(x=517, y=474)

listbox = Listbox(root, width=23, height=20)
listbox.grid(row=1, column=0, sticky=NW, padx=10)
listbox.bind('<<ListboxSelect>>', switchPhoto)

listbox2 = Listbox(root, width=23, height=20)
listbox2.place(x=227, y=426)

entry = Entry(root)
entry.place(x=439, y=500)

addbutton = Button(root, text="Add", fg="lime", command=addItem)
addbutton.place(x=597, y=600)

removebutton = Button(root, text="Remove", fg="red", command=removeItem)
removebutton.place(x=572, y=623)

savebutton = Button(root, fg="goldenrod",text="Save", command=saveList)
savebutton.place(x=592, y=577)

mylab = Label(root,text=lstprint,anchor=W, justify=LEFT)
mylab.pack

can2 = Canvas(root, width=125, height=175)
image2 = Image.open("headshots/mcdavco01.jpg")
photo2 = ImageTk.PhotoImage(image2)
myimg2 = can2.create_image(0, 0, anchor=NW, image=photo2)
can2.place(x=270, y=575)

mainloop()