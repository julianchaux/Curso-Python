import tkinter

window = tkinter.Tk()
window.title("GUI")
window.geometry("500x262+369+162")

# creating a function with an arguments 'event'
def say_hi(event): # you can rename 'event' to anything you want
    tkinter.Label(window, text = "Hi", background="#d9d9d9").pack()

btn = tkinter.Button(window, text = "Click Me!", background="#d9d9d9")
btn.bind("<Button-1>", say_hi) # 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
btn.pack()

window.mainloop()
