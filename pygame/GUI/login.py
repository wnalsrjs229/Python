from tkinter import *
window = Tk()
window.title("LOGIN")
window.geometry("300x150")
window.resizable(False, False)

frame1 = Frame(window)
frame2 = Frame(window)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")

L = list()

def openFrame(frame):
    frame.tkraise()

def btncmd1(ID, PW):
    ID1 = ID.get()
    PW1 = PW.get()
    STR = (ID1,PW1)
    print("Id: %s \nPw: %s" %(ID1,PW1))

    for x in range(len(L)):
        if L[x] == STR :
            openFrame(frame2)
            print("로그인에 성공했습니다")
    
    

def btncmd2(ID, PW):
    ID1 = ID.get()
    PW1 = PW.get()
    global L
    L.append((ID1,PW1))
    print(L)

# 프레임 1
label1 = Label(frame1, text="ID : ")
label1.grid(row=0, column=0)

ent1 = Entry(frame1, width=20)
ent1.grid(row=0, column=1)
ent1.insert(1,"")

label2 = Label(frame1, text="Password : ")
label2.grid(row=1, column=0)

ent2 = Entry(frame1, width=20)
ent2.grid(row=1, column=1)
ent2.insert(1,"")

btn1 = Button(frame1, padx=6, pady=6, text="로그인", command=lambda:[btncmd1(ent1, ent2)])
btn1.grid(row=2, column=1)

btn2 = Button(frame1, padx=6, pady=6, text="회원가입",command=lambda:[btncmd2(ent1, ent2)])
btn2.grid(row=2, column=0)



# 프레임 2
label3 = Label(frame2, text="로그인 되었습니다 !!")
label3.grid(row=0, column=0)

openFrame(frame1)
window.mainloop()
