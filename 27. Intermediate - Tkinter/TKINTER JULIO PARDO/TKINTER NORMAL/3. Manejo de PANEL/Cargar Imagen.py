"""
Objetivo: adicionar widget - Button
"""

from tkinter import *
import tkinter.ttk as ttk
import cv2
import numpy as np
from PIL import Image, ImageTk

def cargar_imagen():
    #global window
    img = cv2.imread('1.jpg')
    b,g,r = cv2.split(img)
    img_1 = cv2.merge((r,g,b))
    im = Image.fromarray(img_1)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.imgtk = imgtk
    #lbl.configure(text="hola")
    lbl.configure(image=imgtk)
    #lbl.pack()

    
window=Tk()
# aqui se adicionaran los widgets a utilizar
#--PANEL
Frame1 = Frame(window)
Frame1.place(relx=0.073, rely=0.044, relheight=0.767, relwidth=0.839)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")
Frame1.configure(width=345)
#--BOTON CARGAR IMAGEN
btn=Button(window, text="Load Image")
btn.place(relx=0.292, rely=0.867, height=34, width=157)
btn.configure(activebackground="#ececec")
btn.configure(activeforeground="#000000")
btn.configure(background="#d9d9d9")
btn.configure(disabledforeground="#a3a3a3")
btn.configure(foreground="#000000")
btn.configure(highlightbackground="#d9d9d9")
btn.configure(highlightcolor="black")
btn.configure(pady="0")
btn.configure(text='''Load Image''')
btn.configure(width=157)
btn.configure(command=cargar_imagen)

#--LABEL
lbl=Label(Frame1, text="IMAGE")
lbl.place(relx=0.058, rely=0.058, height=300, width=300)
lbl.configure(background="#d85a34")
lbl.configure(foreground="#000000")
#lbl.configure(justify='left')

#...............................................
window.title('CARGAR IMAGEN')
window.geometry("411x450+326+129")
window.configure(background="#d9d9d9")
"""
img = cv2.imread('1.jpg')
b,g,r = cv2.split(img)
img_1 = cv2.merge((r,g,b))
im = Image.fromarray(img_1)
imgtk = ImageTk.PhotoImage(image=im)
lbl.configure(image=imgtk)
"""

window.mainloop()

"""
geometry
dimensiones 300x200
ubicacion (100,20)
"""
