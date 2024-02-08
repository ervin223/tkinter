from tkinter import *

def FromEntryToLabel(event):
    t = ent.get()
    l.configure(text=t)

def valik():
    t = var.get()
    ent.delete(0, END)
    ent.insert(END, t)

showflag=False
def showtarnid(event):
   global showflag
   if showflag:
       ent.configure(show="")
   else:
       ent.configure(show="*")
       showflag=True



aken = Tk()
aken.geometry("1080x1920")
aken.title("Pealkiri")
aken.iconbitmap("C:\\Users\\opilane\\Source\\Repos\\erwin\\PythonApplication1\\unnamed.png")
f = Frame(aken, bg="blue", bd=10, height=1750, width=1080)
l = Label(f, text="elemendid", bg="gold", fg="#aa4a44", font="Arial 24", height=24, width=54, justify=CENTER)

ent = Entry(f, fg="gold", bg="yellow", width=17, font="Arial 18") 
btn = Button(f, text="press the button", font="Arial 18", bg="Lightblue", relief=GROOVE)

var = IntVar()
r1 = Radiobutton(f, text="Esimene", font="Algerian 14", variable=var, value=1, command=valik)
r2 = Radiobutton(f, text="Teine", font="Algerian 14", variable=var, value=2, command=valik)
r3 = Radiobutton(f, text="Kolmas", font="Algerian 14", variable=var, value=3, command=valik)

btn.bind("<Button>", FromEntryToLabel)
ent.bind("<Return>", showtarnid) #enter

f.grid(row=0, column=8)
objects = [l, ent, btn, r1, r2, r3]
for obj in objects:
    obj.pack()

aken.mainloop()
