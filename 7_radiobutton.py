from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)

lable1 = Label(root, text="메뉴를 선택하세요.")
lable1.pack()

burger_var = StringVar()    # radio 그룹
btn_burger1 = Radiobutton(root, text="햄버거", value="햄버거", variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value="치즈버거", variable=burger_var)
btn_burger3 = Radiobutton(root, text="불고기버거", value="불고기버거", variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

def btncmd():
    print(burger_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()   #창이 닫히지 않도록 해줌
