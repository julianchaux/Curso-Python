#Si lo importo así, no es necesario colocar tkinter.
from tkinter import *
#Si lo pongo así, si es necesario tkinter.
#import tkinter

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Create Components inside the window

##########################################################################
#Label
my_label = Label(text="I am a Label", font=("Arial",24, "bold"))
#Packer
#my_label.pack(side="left") #sin el pack no se muestra el componente
my_label.pack()
#https://docs.python.org/3/library/tkinter.html#the-packer
#http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# Modificar una propiedad por su nombre
my_label["text"] = "New Text"
my_label.config(text="My New Text 2")

#########################################################################
#Buttons
def button_clicked():
    print("I got clicked!.")
    #my_label.config(text="Button got clicked!.")
    my_label.config(text=input.get())    

button = Button(text="Click Me", command=button_clicked)
#button.focus()
button.pack()

#########################################################################
#Entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
input.pack()

#########################################################################
#Text Box
#Multiple lines
text = Text(height=5, width=30)
text.focus()    #Puts cursor in textbox
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

########################################################################
#Spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

########################################################################
#Scale
#Called with current scale value.
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#########################################################################
#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

checked_state = IntVar() #Variable Int de Tkinter
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
#checked_state.get()
checkbutton.pack()

#########################################################################
#Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#########################################################################
#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()