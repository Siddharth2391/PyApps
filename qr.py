from tkinter import *
import os
import pyqrcode
from PIL import ImageTk,Image
import tkinter.font as tkFont
import tkinter.messagebox

window = Tk()
window.title("QR Code Generator")
window.geometry("500x600")

def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
       tkinter.messagebox.showinfo("error","Please Enter some Subject")

    imageLabel = Label(window,image=photo).place(x=130,y=240)
    #sublabel= Label(window,text="QR of " + Subject.get(),font=fontStyle).place(x=200,y=450)

def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qr.png(os.path.join(dir,name.get()+".png"),scale=8)
        else:
            tkinter.messagebox.showinfo("Please enter a File Name")
    except:
        tkinter.messagebox.showinfo("Saved","QR code saved")


#font
fontStyle = tkFont.Font(family="Lucida Grande", size=18)

#for background of window
canvas=Canvas(window,width=1350,height=700)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Project\\qr.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#Heading 
title=Label(window,text="QR code generator",font=("Helvetica",25,'bold'),bg="black",fg="white",relief=GROOVE)
title.place(x=0,y=0,relwidth=1)


Sub = Label(window,text="Enter subject",font=fontStyle).place(x=10,y=80)

#FName = Label(window,text="Enter FileName",font=fontStyle).place(x=10,y=130)


Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject,font=fontStyle).place(x=200,y=80)

name = StringVar()
#nameEntry = Entry(window,textvariable = name,font=fontStyle).place(x=200,y=130)

button = Button(window,text = "Generate",width=15,command = generate,font=fontStyle,bg='lawn green').place(x=150,y=150)
 

#saveB = Button(window,text="Save as PNG",width=15,command = save,font=fontStyle,bg='lawn green').place(x=250,y=180)


 
window.mainloop()
