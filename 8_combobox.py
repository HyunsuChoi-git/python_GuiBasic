from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly")  #readonly 글입력 막기
combobox.current(0) # 0번째 인덱스 값 default 선택
combobox.pack()

#combobox.set("날짜를 선택하세요.") # 목록의 제목을 선택할 수 있다.

def btncmd():
    print(combobox.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()   #창이 닫히지 않도록 해줌
