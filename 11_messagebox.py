from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)

def info():
    msgbox.showinfo("알림", "정상적으로 예매가 완료되었습니다.")  #타이틀, 내용 

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("오류", "결제 오류가 발생하였습니다.")
    
def ask():
    response = msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    print(response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    
def canclel():
    response = msgbox.askretrycancel("재시도/취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    print(response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    
def yesno():
    response = msgbox.askyesno("예 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")
    print(response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")

        
def yesnocancle():
    response = msgbox.askyesnocancel("예/아니오/취소", "예매 내역이 저장되지 않았습니다. \n저장하시겠습니까?")
    #True, False, None
    print(response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="오류").pack()
Button(root, command=ask, text="확인 취소").pack()
Button(root, command=canclel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancle, text="예 아니오 취소").pack()


root.mainloop()