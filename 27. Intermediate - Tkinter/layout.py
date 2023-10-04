#Si lo importo así, no es necesario colocar tkinter.
from tkinter import *
#Si lo pongo así, si es necesario tkinter.
#import tkinter

def button_clicked():
    print("I got clicked!.")
    #my_label.config(text="Button got clicked!.")
    my_label.config(text=input.get())  


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Create Components inside the window

##########################################################################
#Label
my_label = Label(text="I am a Label", font=("Arial",24, "bold"))
#Packer
#my_label.pack(side="left") #sin el pack no se muestra el componente
# Modificar una propiedad por su nombre
my_label["text"] = "New Text"
my_label.config(text="My New Text 2")
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
#https://docs.python.org/3/library/tkinter.html#the-packer
#http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

#########################################################################
#Buttons
button = Button(text="Click Me", command=button_clicked)
#button.focus()
#button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#########################################################################
#Entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
#input.pack()
input.grid(column=3, row=2)

window.mainloop()