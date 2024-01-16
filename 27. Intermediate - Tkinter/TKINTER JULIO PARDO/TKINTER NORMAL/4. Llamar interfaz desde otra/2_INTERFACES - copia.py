import tkinter as tk

master = tk.Tk()
master.geometry("300x300")
master.title("SoftwareSamples #3")

def funcion():
    lbl.configure(text='''hola desde la otra''')   
    
def command():
    master2 = tk.Tk()
    master2.geometry("300x300")
    master2.title("New Window")
    label = tk.Label(master2, text="This is the new window")
    label.pack()
    btn = tk.Button(master2, text="Open New Window", command=funcion)
    btn.pack()
    #master2.mainloop()

lbl=tk.Label(master,text="esperando")
lbl.pack()
newwindow = tk.Button(master, text="Open New Window", command=command)
newwindow.pack()
master.mainloop()



