from tkinter import *

root = Tk() 
root.title("GUI test")
root.geometry("540x380+200+100")
root.resizable(False, False)

txt=Text(root, width=30, height=10)
txt.pack()

txt.insert(END, "글자를 입력하세요")


ent = Entry(root, width=30)
ent.pack()
ent.insert(1,"한 줄만 입력됩니다!")

def btncmd():
    print(txt.get("1.0", END))
    print(ent.get())
    txt.delete("1.0", END)
    ent.delete(0, END)

btn = Button(root, text = "CLICK", command=btncmd)
btn.pack()

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "대한민국")
listbox.insert(1, "독일")
listbox.insert(2, "미국")
listbox.insert(END, "호주")
listbox.insert(END, "뉴질랜드")
listbox.pack()

root.mainloop()

