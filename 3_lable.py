from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+1200+600")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="python_GuiBasic/btnImg1.png")
lable2 = Label(root, image=photo)
lable2.pack()

def change():
    label1.config(text="안녕!")

    global photo2 
    photo2 = PhotoImage(file="python_GuiBasic/btnImg2.png")
    lable2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()