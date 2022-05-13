from operator import truediv
from tkinter import *
import os

filename = "mynote.txt"

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(True, True)

#스크롤
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#텍스트공간
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

def save_file():
    with open(filename, "w", encoding="UTF8") as write_file:
        write_file.write(txt.get("0.1", END))

menubar = Menu(root)

def open_file():
    if os.path.isfile(filename):
        txt.delete("1.0", END)
        with open(filename, "r", encoding="UTF8") as file:
            txt.insert(END, file.read())

menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="열기(O)", command=open_file)
menu_file.add_command(label="저장(S)", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command=root.quit)

menubar.add_cascade(label="파일(F)", menu=menu_file)
menubar.add_cascade(label="편집(E)")
menubar.add_cascade(label="서식(O)")
menubar.add_cascade(label="보기(V)")
menubar.add_cascade(label="도움말(H)")


root.config(menu=menubar)

root.mainloop()