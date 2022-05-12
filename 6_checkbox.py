from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)

chkvar = IntVar()   #int형으로 값을 저장한다.
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
#checkbox.select()   #default 선택
#checkbox.deselect()  #default 선택X
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
checkbox2.pack()

def btncmd():
    #체크박스 상태 추출
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()   #창이 닫히지 않도록 해줌
