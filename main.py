import tkinter as tk
# import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont


#calcualtor
def cal():
    import os 
    os.system('python Calculator.py')

#yt         
def yt():
    import os 
    os.system('python yt.py')
        
#currency convertor
def curren():
    import os 
    os.system('python curren.py')
        
#typing test
def typing():
    import os 
    os.system('python speedtyping.py')

#snake game
def snake():
    import os
    os.system('python snakee.py')

#tic tac toe game
def ttt():
    import os
    os.system('python ttt.py')

def qr():
    import os
    os.system('python qr.py')

def ps():
    import os
    os.system('python ps.py')

def ag():
    import os
    os.system('python ag.py')

#Frame Design
root = tk.Tk()
root.geometry("700x720+0+0") #(width X height)
root.title("Python Mini-Applications") 
fontStyle = tkFont.Font(family="Lucida Grande", size=30)
root.resizable(0,0)
canvas=Canvas(root,width=1350,height=700)
image=ImageTk.PhotoImage(Image.open("./res/mainbg.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#Heading 
title=Label(root,text="Python Mini application",font=("Helvetica",30,'bold'),bg="black",fg="white",relief=GROOVE)
title.place(x=0,y=0,relwidth=1)

#________________________________________________________________________________________________________________________
#Row 1
#Button 1
photo1 = PhotoImage(file = "./res/call.png")
photoimage1 = photo1.subsample(1,1)
Button1 = tk.Button(root, text ="Calculator",image = photoimage1,command=cal,relief=FLAT)
Button1.place(x=65,y=100,width=170,height=170) #width=200,height=200

#button 2
photo2 = PhotoImage(file = "./res/qri.png")
photoimage2 = photo2.subsample(1, 1)
Button2 = tk.Button(root, text ="Youtube downloadar",image = photoimage2,command=qr,relief=FLAT)
Button2.place(x=275,y=100,width=170,height=170)

#button 3
photo3 = PhotoImage(file = "./res/yt.png")
photoimage3 = photo3.subsample(1, 1)
Button3 = tk.Button(root, text ="Typing Test",image = photoimage3,command=yt,relief=FLAT)
Button3.place(x=475,y=100,width=170,height=170)

#________________________________________________________________________________________________________________________
#row 2
#button 4
photo4 = PhotoImage(file = "./res/type.png")
photoimage4 = photo4.subsample(1, 1)
Button4 = tk.Button(root, text ="Currency Convertor",image = photoimage4,command=typing,relief=FLAT)
Button4.place(x=65,y=285,width=170,height=170)

#Button 5
photo5 = PhotoImage(file = "./res/ttt.png")
photoimage5 = photo5.subsample(1,1)
Button5 = tk.Button(root, text ="Calculator",image = photoimage5,command=ttt,relief=FLAT)
Button5.place(x=275,y=285,width=170,height=170) #width=200,height=200

#button 6
photo6= PhotoImage(file = "./res/snake.png")
photoimage6 = photo6.subsample(1, 1)
Button6 = tk.Button(root, text ="Youtube downloadar",image = photoimage6,command=snake,relief=FLAT)
Button6.place(x=475,y=285,width=170,height=170)

#________________________________________________________________________________________________________________________
#row 3

#button 7
photo7= PhotoImage(file = "./res/curr.png")
photoimage7 = photo7.subsample(1, 1)
Button7 = tk.Button(root, text ="Currency Convertor",image = photoimage7,command=curren,relief=FLAT)
Button7.place(x=65,y=485,width=170,height=170)

#Button 8
photo8 = PhotoImage(file = "./res/ps.png")
photoimage8 = photo8.subsample(1,1)
Button8 = tk.Button(root, text ="Tic tac toe",image = photoimage8,command=ps,relief=FLAT)
Button8.place(x=275,y=485,width=175,height=170) #width=200,height=200


#button 9
photo9= PhotoImage(file = "./res/ag.png")
photoimage9 = photo9.subsample(1, 1)
Button9 = tk.Button(root, text ="Snake game",image = photoimage9,command=ag,relief=FLAT)
Button9.place(x=475,y=485,width=170,height=170)

#________________________________________________________________________________________________________________________


mainloop()

