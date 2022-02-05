from tkinter import *
from pytube import YouTube
from PIL import ImageTk,Image

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube video downloader")

#image of bg
canvas=Canvas(root,width=1350,height=700)
image=ImageTk.PhotoImage(Image.open("G:\\Siddharth\\App\\python images\\bgg1.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

title=Label(root,text="Youtube video downloader",font=("Times New Roman Baltic",20),bg="black",fg="white",relief=GROOVE)
title.place(x=0,y=0,relwidth=1)
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()



##enter link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 90)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 140)



def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 250)  


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 190)



root.mainloop()
