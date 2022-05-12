from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")

Label(root, text="메뉴를 선택해 주세요.").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)


Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
frame_drink.pack(side="right", fill="both", expand=True) #side:위치, fill:위아래 공간 채우기, expand=가로 공간 채우기


root.mainloop()   #창이 닫히지 않도록 해줌
