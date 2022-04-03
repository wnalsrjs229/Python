from tkinter import *

root = Tk() 
root.title("GUI test")
root.geometry("540x380+200+100")
root.resizable(False, False)

btn1 = Button(root, text="버튼1")
btn1.grid(row=0, column=0)

btn2 = Button(root, padx=10, pady=10, text="버튼2")
btn2.grid(row=1, column=0)

btn3 = Button(root, fg="green", bg="yellow", text="버튼3")
btn3.grid(row=2, column=0)

def btncmd():
    print("버튼이 클릭되었습니다!")

btn4 = Button(root, text="동작하는 버튼", command=btncmd)
btn4.grid(row=3, column=0)

label1 = Label(root, text="Hi, 안녕하세요")
label1.grid(row=0, column=1)

photo=PhotoImage(file="C:/Users/WINDOWS10/Desktop/python_projects/pygame/GUI/balloon4.png")
label2 = Label(root, image = photo)
label2.grid(row=1, column=1)

def change():
    label1.config(text="한국에 오신걸 환영합니다!")

btn5 = Button(root, text="클릭", command=change)
btn5.grid(row=4, column=0)

txt=Text(root, width=30, height=10)
txt.grid(row=5, column=0)

txt.insert(END, "글자를 입력하세요")
root.mainloop()

ent = Entry(root, width=30)
ent.grid(row=6, column=0)

root.mainloop()

