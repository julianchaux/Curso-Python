"""
Objetivo: adicionar widget - Button
"""

from tkinter import *
window=Tk()
# aqui se adicionaran los widgets a utilizar
btn=Button(window, text="Este es un widget", fg='blue')
btn.place(x=80, y=100)

window.title('Hello Python')
window.geometry("300x200+100+20")
window.mainloop()

"""
geometry
dimensiones 300x200
ubicacion (100,20)
"""
