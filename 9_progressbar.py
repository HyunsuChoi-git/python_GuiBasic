import time
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480")   #크기지정 ("가로x세로")
root.geometry("640x480+1200+600")  #크기지정 + 위치지정 ("가로x세로+x측+y측")
root.resizable(False, True) # 창 크기 변경 불가 (X측, Y측)

'''
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10) #지정한 밀리세컨드마자 움직임
progressbar.pack()
progressbar2.start(10) #지정한 밀리세컨드마자 움직임
progressbar2.pack()
'''
p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()


def btncmd():
    '''progressbar.stop()
    progressbar2.stop()'''

    for i in range(1, 101):
        time.sleep(0.01) #0.01초 대기
        p_var3.set(i)
        progressbar3.update
        print(p_var3.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()   #창이 닫히지 않도록 해줌
