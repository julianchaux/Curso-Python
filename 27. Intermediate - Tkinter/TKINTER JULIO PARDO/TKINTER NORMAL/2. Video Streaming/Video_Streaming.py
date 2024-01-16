"""
Streaming Video (Python 3.6)
Paquetes necesarios:
pillow  >>pip install pillow

"""

from tkinter import *
import tkinter.ttk as ttk
import cv2
import numpy as np
from PIL import Image, ImageTk

def show_frame():
    global window
    _, img = cap.read()
    
    b,g,r = cv2.split(img)
    img_1 = cv2.merge((r,g,b))
    im = Image.fromarray(img_1)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.imgtk = imgtk
    #lbl.configure(text="hola")
    lbl.configure(image=imgtk)
    window.after(10, show_frame) 

    #lbl.pack()

cap = cv2.VideoCapture(0)    
window=Tk()
# aqui se adicionaran los widgets a utilizar
#--INICIAR VIDEO
btn=Button(window, text="Start")
btn.place(relx=0.394, rely=0.897, height=34, width=197)
btn.configure(activebackground="#ececec")
btn.configure(activeforeground="#000000")
btn.configure(background="#d9d9d9")
btn.configure(disabledforeground="#a3a3a3")
btn.configure(foreground="#000000")
btn.configure(highlightbackground="#d9d9d9")
btn.configure(highlightcolor="black")
btn.configure(pady="0")
btn.configure(width=197)
btn.configure(command=show_frame)

#--SEPARADOR
separador = ttk.Separator(window)
separador.place(relx=0.086, rely=0.867, relwidth=0.812)

#--LABEL
lbl=Label(window, text="IMAGE")
lbl.place(relx=0.098, rely=0.075, height=480, width=640)
#lbl.configure(background="#d8b18a")
lbl.configure(foreground="#000000")
lbl.configure(justify='left')
lbl.configure(text='''IMAGE''')
lbl.configure(width=690)
#...............................................
window.title('CARGAR IMAGEN')
window.geometry("813x669+1+7")
window.configure(background="#d9d9d9")

window.mainloop()

"""
geometry
dimensiones 300x200
ubicacion (100,20)
"""
