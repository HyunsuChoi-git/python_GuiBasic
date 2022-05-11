from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)


txt = Text(root, width=30, heigh=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)    # 한줄짜리. 엔터 불가능
e.pack()
e.insert(0, "한 줄만 입력하세요")


def btncmd():
    print(txt.get("1.0", END))  # 1.0 --> 1: 라인수, 0:글자위치  부터 글자를 추출하는 것. END -> 어디까지
    print(e.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()   #창이 닫히지 않도록 해줌
