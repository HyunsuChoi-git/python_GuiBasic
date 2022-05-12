from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar) #스크롤바 매핑
for i in range(1, 32):
    listbox.insert(END, str(i)+"일")
listbox.pack()

scrollbar.config(command=listbox.yview) #리스트박스 매핑

root.mainloop()   #창이 닫히지 않도록 해줌
