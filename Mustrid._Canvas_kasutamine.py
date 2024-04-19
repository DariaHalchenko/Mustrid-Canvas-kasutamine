
from tkinter import * 
from turtle import width
from random import * 
from math import *

aken= Tk () 
aken.geometry("800x600") 
aken.iconbitmap('canvas.ico') 
aken.title("Mustrid. Canvas kasutamine") 

def ring(aken):
    colors=["black",
                "cyan",
                "magenta",
                "red",
                "blue",
                "gray",
                "yellow",
                "green",
                "lightblue",
                "pink",
                "gold"]
    x0=0
    y0=0
    x1=600
    y1=600
    p=2
    for i in range(150):
            x0+=p 
            y0+=p 
            x1-=p 
            y1-=p 
            aken.create_oval(x0,y0,x1,y1, fill=choice(colors))




def ruut():
    x0=80
    y0=80
    x1=400
    y1=400
    a=200
    r=(a**2+a**2)**(1/2) 
    p=(a-r) 
    for i in range(35):
        x0+=p 
        y0+=p 
        x1-=p 
        y1-=p
        aken.create_rectangle(x0,y0,x1,y1, fill="Red")
        aken.create_oval(x0,y0,x1,y1, fill="Yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2


def malelaud(aken):
    a=45
    b=a*15
    for i in range(12):
        for j in range(12):
            x1=i * a
            y1=j *  a
            if (i + j) % 2 == 0:
                color = "white"
            else:
                color = "black" 
                aken.create_rectangle(x1, y1, x1+a, y1+a, fill=color)


def Eesti(aken):
    x1=15
    y1=85
    y2=145
    y3=255
    a=250
    b=200
    aken.create_rectangle(x1,y1,a, b, fill="Blue")
    aken.create_rectangle(x1,y2,a, b, fill="Black")
    aken.create_rectangle(x1,y3,a, b,  fill="White")
    aken.grid()

def Ukrainlane(aken):
    x1=35
    y1=35
    y2=115
    a=300
    b=200
    aken.create_rectangle(x1,y1,a, b, fill="Blue")
    aken.create_rectangle(x1,y2,a, b, fill="Yellow")




def Bahama(aken):
    x1=35
    a=300
    b=200
    y1=45
    y2=95
    y3=155
    aken.create_rectangle(x1, y1, a, b, fill="Teal")
    aken.create_rectangle(x1, y2, a, b, fill="Yellow")
    aken.create_rectangle(x1, y3, a, b, fill="Teal")
    aken.create_polygon([x1,y1],[x1,b],[115,125],fill="black")
 

def valgusfoor(aken): 
    a=150
    b=160
    x1=30
    y1=60
    y2=105
    y3=225
    aken.create_rectangle(x1, y1, a, b, width=3, outline="white", fill="Red")
    aken.create_rectangle(x1, y2, a, b, width=3, outline="white", fill="Yellow")
    aken.create_rectangle(x1, y3, a, b, width=3, outline="white", fill="Green") 
    aken.create_rectangle(125, 245, 60, 268, fill="Black") 
    aken.create_rectangle(35, 275, 150, 257, fill="Black")




def valik():
    num = 0
    if num == 1:
        raam = Tk()
        raam.title("Ring")
        tahvel1 = Canvas(aken, width=600, height=600)
        tahvel1.create_text(30, 550, text="Ring", font="Algerian 25", anchor=NW) 
        ring(aken)
        aken.pack()
    elif num==2:
        raam1 = Tk()
        raam1.title("Ruut")
        tahvel2 = Canvas(aken, width=600, height=600)
        tahvel2.create_text(30, 500, text="Ruut",font="Algerian 25", anchor=NW) 
        ruut(aken)
        aken.pack()
    elif num==3:
        raam2 = Tk()
        raam2.title("Malelaud")
        tahvel3 = Canvas(aken, width=600, height=600)
        tahvel3.create_text(30, 550, text="Malelaud", font="Algerian 25", anchor=NW) 
        malelaud(aken)
        aken.pack()
    elif num ==4:
        raam2 = Tk()
        raam2.title("Eesti riigi lipp")
        tahvel4 = Canvas(aken, width=400, height=400)
        tahvel4.create_text(65, 300, text="Eesti riigi lipp", font="Algerian 25", anchor=NW) 
        Eesti(aken)
        aken.pack()
    elif num == 5:
        raam2 = Tk()
        raam2.title("Ukrainlane riigi lipp")
        tahvel5 = Canvas(aken, width=400, height=400)
        tahvel5.create_text(30, 300, text="Ukrainlane riigi lipp", font="Algerian 25", anchor=NW) 
        Ukrainlane(aken)
        aken.pack()
    elif num==6:
        raam2 = Tk()
        raam2.title("Bahama saarte lipp")
        tahvel6 = Canvas(aken, width=400, height=400)
        tahvel6.create_text(30, 300, text="Bahama saarte lipp", font="Algerian 25", anchor=NW) 
        Bahama(aken)
        aken.pack()
    elif num==7:
        raam2 = Tk()
        raam2.title("valgusfoor")
        tahvel7 = Canvas(aken, width=300, height=300)
        tahvel7.create_text(25, 20, text="Valgusfoor", font="Algerian 25", anchor=NW)
        valgusfoor(aken)
        aken.pack()

r1 = Radiobutton(aken, text="Ring",  value=1, command=ring)
r2 = Radiobutton(aken, text="Ruut", value=2, command=ruut)
r3 = Radiobutton(aken, text="Malelaud",  value=3, command=malelaud)
r4 = Radiobutton(aken, text="Eesti riigi lipp",  value=4, command=Eesti)
r5 = Radiobutton(aken, text="Ukrainlane riigi lipp",  value=5,command =Ukrainlane)
r6 = Radiobutton(aken, text="Bahama saarte lipp",  value=6, command=Bahama)
r7 = Radiobutton(aken, text="Valgusfoor",  value=7, command=valgusfoor)

lbox = Listbox(aken, height=3, width=33)

r1.grid(row=1, column=0)
r2.grid(row=2, column=0)
r3.grid(row=3, column=0)
r4.grid(row=4, column=0)
r5.grid(row=5, column=0)
r6.grid(row=6, column=0)
r7.grid(row=7, column=0)

aken.mainloop()







