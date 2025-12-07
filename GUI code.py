# khaled mahmoud eldesoky eldesoky 
# SECTION 4
from tkinter import *
import webbrowser
def fun():
    link = txt.get()
    webbrowser.open(link)


myframe=Tk()
myframe.geometry('400x300')
myframe.title('My App')


lbl=Label(myframe,text='Web Browser',fg='black',font=' Tahoma 30 bold')
lbl.pack(pady=30)

txt = Entry(myframe,width=50)
txt.pack(pady=10)

btn = Button(myframe,commond=fun,text='click on the link',fg='blue',bg='yellow',font='poplarStd 20 bold',padx=10)
btn.pack()


myframe.mainloop()
