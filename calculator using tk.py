from tkinter import *


window=Tk()
window.geometry("330x400")

e= Entry(window,width=50,borderwidth=5,relief=SUNKEN)
e.place(x=10,y=10)

def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

b=Button(window,text="1",width=12,pady=5,command=lambda:click(1))
b.place(x=20,y=60)

b=Button(window,text="2",width=12,pady=5,command=lambda:click(2))
b.place(x=120,y=60)

b=Button(window,text="3",width=12,pady=5,command=lambda:click(3))
b.place(x=220,y=60)

b=Button(window,text="4",width=12,pady=5,command=lambda:click(4))
b.place(x=20,y=120)

b=Button(window,text="5",width=12,pady=5,command=lambda:click(5))
b.place(x=120,y=120)

b=Button(window,text="6",width=12,pady=5,command=lambda:click(6))
b.place(x=220,y=120)

b=Button(window,text="7",width=12,pady=5,command=lambda:click(7))
b.place(x=20,y=180)

b=Button(window,text="8",width=12,pady=5,command=lambda:click(8))
b.place(x=120,y=180)

b=Button(window,text="9",width=12,pady=5,command=lambda:click(9))
b.place(x=220,y=180)

b=Button(window,text="0",width=12,pady=5,command=lambda:click(0))
b.place(x=20,y=240)

def add():
    n1=e.get()
    global math
    math="+"
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text="+",width=12,pady=5,command=add)
b.place(x=120,y=240)

def sub():
    n1=e.get()
    global math
    math="-"
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text="-",width=12,pady=5,command=sub)
b.place(x=220,y=240)

def multi():
    n1=e.get()
    global math
    math="*"
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text="*",width=12,pady=5,command=multi)
b.place(x=20,y=300)

def div():
    n1=e.get()
    global math
    math="/"
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text="/",width=12,pady=5,command=div)
b.place(x=120,y=300)

def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="+":
        e.insert(0,i+int(n2))
    elif math=="-":
        e.insert(0,i-int(n2))
    elif math=="*":
        e.insert(0,i*int(n2))
    elif math=="/":
        e.insert(0,i/int(n2))

b=Button(window,text="=",width=12,pady=5,command=equal)
b.place(x=220,y=300)

def clear():
    e.delete(0,END)

b=Button(window,text="Clear",width=12,pady=5,command=clear)
b.place(x=120,y=350)

window.mainloop()
