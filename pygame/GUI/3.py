from tkinter import *
window = Tk()
window.title("Frame_Change")
window.geometry("600x600+200+200")


frame1 = Frame(window)
frame2 = Frame(window)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")

def openFrame(frame):
    frame.tkraise()

btnToFrame1 = Button(frame2,
    text="Change To Frame1",
    padx=10,
    pady=10,
    command=lambda:[openFrame(frame1)])

btnToFrame2 = Button(frame1,
    text="Change To Frame2",
    padx=10,
    pady=10,
    command=lambda:[openFrame(frame2)])

btnToFrame1.pack()
btnToFrame2.pack()

window.mainloop()