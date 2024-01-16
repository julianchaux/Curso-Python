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
from threading import Thread, Lock

#..........................................................

class WebcamVideoStream :
    def __init__(self, src = 0, width = 640, height = 480) :
        self.stream = cv2.VideoCapture(src)
        self.stream.set(3, width) # esto no es necesario
        self.stream.set(4, height) # esto no es necesario
        (self.grabbed, self.frame) = self.stream.read()
        
        self.started = False
        self.read_lock = Lock()

    def start(self) :
        if self.started :
            print ("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self) :
        while self.started :
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self) :
        self.read_lock.acquire()
        frame = self.frame.copy()
        #frame = cv2.resize(frame,None, fx=0.5,fy=0.5,interpolation = cv2.INTER_CUBIC)
        self.read_lock.release()
        return frame

    def stop(self) :
        self.started = False
        if self.thread.is_alive():
            self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback) :
        self.stream.release()

#...........................................................

def show_frame():
    global window
    img = vs.read()
    #verificar lectura con if empty img
    
    b,g,r = cv2.split(img)
    img_1 = cv2.merge((r,g,b))
    im = Image.fromarray(img_1)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.imgtk = imgtk # esto fue definitivo
    #lbl.configure(text="hola")
    lbl.configure(image=imgtk)
    window.after(10, show_frame) 

    #lbl.pack()

#............................................................ 
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


vs = WebcamVideoStream().start()
window.mainloop()

"""
geometry
dimensiones 300x200
ubicacion (100,20)
"""
