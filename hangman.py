import random
from tkinter import *

a = 1

infile = open("C:\\Users\\KingGOD\\Documents\\hangman\\hangman.txt", "r")

line = infile.read()
line2 = line.split("\n")

def start():
    global b, c, count

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

    count = 0

    a = random.choice(line2)
    b = list(a.split(" "))
    c = []

    for i in range(len(b)):
        c.append("_")

    entry1.insert(END, c)
    entry3.insert(END, count)

def check():
    global b, c, count
    answer = str(entry2.get())
    entry2.delete(0, END)
    for i in range(len(b)):
        if b[i] == answer:
            c[i] = b[i]
    entry1.delete(0, END)
    entry1.insert(END, c)
    if not answer in b:
        count += 1
        entry3.delete(0, END)
        entry3.insert(END, count)
    if b == c or count == 10:
        if count == 10:
            entry3.delete(0, END)
            entry3.insert(END, "탈락")
        else:
            entry3.delete(0, END)
            entry3.insert(END, "성공")


window = Tk()
window.geometry("800x400")
button1 = Button(window, text = '시작', width = 20, height = 5, command = start)
button2 = Button(window, text = '확인', width = 20, height = 5, command = check)
entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)
button1.grid(row = 0, column = 0)
button2.grid(row = 1, column = 0)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)
entry3.grid(row = 2, column = 1)


window.mainloop()

infile.close()