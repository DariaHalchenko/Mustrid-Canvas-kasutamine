from tkinter import * 
from turtle import width
import random 
from math import *

aken= Tk () 
aken.geometry("800x700") 
aken.iconbitmap('canvas.ico') 
aken.title("Mustrid. Canvas kasutamine") 

def ring():
    raam1 = Tk()
    raam1.title("Ring")
    tahvel1 = Canvas(raam1, width=600, height=600)
    tahvel1.create_text(30, 550, text="Ring", font=("Algerian" ,25), anchor=NW) 
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
            tahvel1.create_oval(x0,y0,x1,y1, fill=choice(colors))
    tahvel1.grid()




def ruut():
    raam2 = Tk()
    raam2.title("Ruut")
    tahvel2 = Canvas(raam2, width=600, height=600)
    tahvel2.create_text(30, 500, text="Ruut", font=("Algerian" ,25), anchor=NW) 
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
        tahvel2.create_rectangle(x0,y0,x1,y1, fill="Red")
        tahvel2.create_oval(x0,y0,x1,y1, fill="Yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2
    tahvel2.grid()


def malelaud():
    raam3 = Tk()
    raam3.title("Malelaud")
    tahvel3 = Canvas(raam3, width=600, height=600) 
    tahvel3.create_text(30, 550, text="Malelaud", font=("Algerian" ,25), anchor=NW) 
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
                tahvel3.create_rectangle(x1, y1, x1+a, y1+a, fill=color)
    tahvel3.grid()

def Eesti():
    raam4 = Tk()
    raam4.title("Eesti riigi lipp")
    tahvel4 = Canvas(raam4, width=400, height=400)
    tahvel4.create_text(65, 300, text="Eesti riigi lipp", font=("Algerian" ,25), anchor=NW) 
    x1=15
    y1=85
    y2=145
    y3=255
    a=250
    b=200
    tahvel4.create_rectangle(x1,y1,a, b, fill="Blue")
    tahvel4.create_rectangle(x1,y2,a, b, fill="Black")
    tahvel4.create_rectangle(x1,y3,a, b,  fill="White")
    tahvel4.grid()

def Ukrainlane():
    raam5 = Tk()
    raam5.title("Ukrainlane riigi lipp")
    tahvel5 = Canvas(raam5, width=400, height=400)
    tahvel5.create_text(30, 300, text="Ukrainlane riigi lipp", font=("Algerian" ,25), anchor=NW) 
    x1=35
    y1=35
    y2=115
    a=300
    b=200
    tahvel5.create_rectangle(x1,y1,a, b, fill="Blue")
    tahvel5.create_rectangle(x1,y2,a, b, fill="Yellow")
    tahvel5.grid()



def Bahama():
    raam6 = Tk()
    raam6.title("Bahama saarte lipp")
    tahvel6 = Canvas(raam6, width=400, height=400)
    tahvel6.create_text(30, 300, text="Bahama saarte lipp", font=("Algerian" ,25), anchor=NW) 
    x1=35
    a=300
    b=200
    y1=45
    y2=95
    y3=155
    tahvel6.create_rectangle(x1, y1, a, b, fill="Teal")
    tahvel6.create_rectangle(x1, y2, a, b, fill="Yellow")
    tahvel6.create_rectangle(x1, y3, a, b, fill="Teal")
    tahvel6.create_polygon([x1,y1],[x1,b],[115,125],fill="black")
    tahvel6.grid()
 

def valgusfoor(): 
    raam7 = Tk()
    raam7.title("Valgusfoor")
    tahvel7 = Canvas(raam7, width=300, height=300)
    tahvel7.create_text(25, 20, text="Valgusfoor", font=("Algerian" ,25), anchor=NW)
    a=150
    b=160
    x1=30
    y1=60
    y2=105
    y3=225
    tahvel7.create_rectangle(x1, y1, a, b, width=3, outline="white", fill="Red")
    tahvel7.create_rectangle(x1, y2, a, b, width=3, outline="white", fill="Yellow")
    tahvel7.create_rectangle(x1, y3, a, b, width=3, outline="white", fill="Green") 
    tahvel7.create_rectangle(125, 245, 60, 268, fill="Black") 
    tahvel7.create_rectangle(35, 275, 150, 257, fill="Black")
    tahvel7.grid()


var=IntVar()
def choice():
    figure = var.get()
    if figure == 1:
        ring()
    elif figure==2:
        ruut()
    elif figure==3:
        malelaud()
    elif figure ==4:
        Eesti()
    elif figure == 5:
        Ukrainlane()
    elif figure==6:
        Bahama()
    elif figure==7:
        valgusfoor()



r1 = Radiobutton(aken, 
                 text="Ring", 
                 font=("Algerian" ,25),
                 variable=var, 
                 value=1, 
                 command=choice)
r2 = Radiobutton(aken, 
                 text="Ruut", 
                 font=("Algerian" ,25),
                 variable=var, 
                 value=2, 
                 command=choice)
r3 = Radiobutton(aken, 
                 text="Malelaud", 
                 font=("Algerian" ,25),
                 variable=var, 
                 value=3, 
                 command=choice)
r4 = Radiobutton(aken, 
                 text="Eesti riigi lipp", 
                 font=("Algerian" ,25),
                 variable=var, 
                 value=4, 
                 command=choice)
r5 = Radiobutton(aken, 
                 text="Ukrainlane riigi lipp", 
                 font=("Algerian" ,25), 
                 variable=var, 
                 value=5, 
                 command=choice)
r6 = Radiobutton(aken, 
                 text="Bahama saarte lipp", 
                 font=("Algerian" ,25),
                 variable=var, 
                 value=6, 
                 command=choice)
r7 = Radiobutton(aken, 
                 text="Valgusfoor", 
                 font=("Algerian" ,25),
                 variable=var, 
                 value=7, 
                 command=choice)



r1.grid(row=1, column=0)
r2.grid(row=2, column=0)
r3.grid(row=3, column=0)
r4.grid(row=4, column=0)
r5.grid(row=5, column=0)
r6.grid(row=6, column=0)
r7.grid(row=7, column=0)

aken.mainloop()

﻿
