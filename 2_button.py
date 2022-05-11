from tkinter import *

root = Tk()
root.title("Nado GUI")

### 소스코드 작성
btn1 = Button(root, text="버튼1")
btn1.pack()              #pack을 호출해야만 실제 버튼이 보임

btn2 = Button(root, padx=5, pady=10, text="버튼2")      #padx, pady  버튼 내부 여백 조절 (글자 상하 좌우 크기)
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()
btn4 = Button(root, width=10, height=3, text="버튼44444444444444444")   #width, height 버튼의 고정 크기 지정
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")    # fg 글자색, bg 배경색 지정
btn5.pack()

photo = PhotoImage(file="python_GuiBasic/btnImg1.png")
btn6 = Button(root, image=photo)    # image 이미지를 버튼으로 지정
btn6.pack()

def btncmd():
    print("버튼 클릭")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()   #창이 닫히지 않도록 해줌




