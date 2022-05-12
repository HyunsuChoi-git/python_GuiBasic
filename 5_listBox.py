from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)

listbox = Listbox(root, selectmode="extended", height=0) #높이를 0으로 하면 리스트 크기만큼의 박스가 지정됨.
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(END) # 맨 뒤 항목 삭제
    #listbox.delete(0) # 맨 앞 항목 삭제

    #갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요.")

    #항목 확인 (.get(startIdx, endIdx))
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    #선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection()) #선택된 값을 인덱스로 반환


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()   #창이 닫히지 않도록 해줌
