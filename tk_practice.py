from tkinter import *

def FromEntryToLabel(event):
    t = ent.get()
    l.configure(text=t)

def showtarnid(event):
    t = ent.get()
    if t == "*":
        t = t.replace("abc", "")
    elif t == "abc":
        t = t.replace("abc", "")
    ent.delete(0, END)
    ent.insert(END, t)

aken = Tk()
aken.geometry("700x340")
aken.title("Pealkiri")
aken.iconbitmap("C:\\Users\\opilane\\Source\\Repos\\erwin\\PythonApplication1\\unnamed.png")
f = Frame(aken, bg="blue", bd=10, height=700, width=340)
l = Label(f, text="elemendid", bg="gold", fg="#aa4a44", font="Arial 24", height=8, width=35, justify=CENTER)

ent = Entry(f, fg="gold", bg="yellow", width=17, font="Arial 18") 
btn = Button(f, text="press the button", font="Arial 18", bg="Lightblue", relief=GROOVE)

btn.bind("<Button>", FromEntryToLabel)
ent.bind("<Return>", showtarnid) # enter

f.grid(row=0, column=8)
objects = [l, ent, btn]
for obj in objects:
    obj.pack()

aken.mainloop()


