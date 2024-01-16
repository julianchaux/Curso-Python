"""
Objetivo: adicionar widget - Button
"""

from tkinter import *
import tkinter.ttk as ttk
import cv2
import numpy as np
from PIL import Image, ImageTk

def cargar_imagen():
    global window
    img = cv2.imread('1.jpg')
    #OpenCV lee imágenes en el formato (B,G,R)
    b,g,r = cv2.split(img)
    img_1 = cv2.merge((r,g,b))
    im = Image.fromarray(img_1)
    #TKinter muestra imágenes en formato (R,G,B)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.imgtk = imgtk
    #lbl.configure(text="hola")
    lbl.configure(image=imgtk)
    #lbl.pack()

    
window=Tk()
# aqui se adicionaran los widgets a utilizar
#--BOTON CARGAR IMAGEN
btn=Button(window, text="Load Image")
btn.place(relx=0.394, rely=0.897, height=34, width=197)
btn.configure(activebackground="#ececec")
btn.configure(activeforeground="#000000")
btn.configure(background="#d9d9d9")
btn.configure(disabledforeground="#a3a3a3")
btn.configure(foreground="#000000")
btn.configure(highlightbackground="#d9d9d9")
btn.configure(highlightcolor="black")
btn.configure(pady="0")
btn.configure(text='''Load Image''')
btn.configure(width=197)
btn.configure(command=cargar_imagen)

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
