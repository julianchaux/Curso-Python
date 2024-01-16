import tkinter as tk

master = tk.Tk()
master.geometry("300x300")
master.title("SoftwareSamples #3")
 
def command():
    master2 = tk.Tk()
    master2.geometry("300x300")
    master2.title("New Window")
    label = tk.Label(master2, text="This is the new window")
    label.pack()
    master2.mainloop()
     
newwindow = tk.Button(master, text="Open New Window", command=command)
newwindow.pack()
master.mainloop()
