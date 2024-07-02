import random
import tkinter as tk


class WindowCreate():
    def __init__(self):
        root=tk.Tk()
        root.geometry('')
        root.resizable(False,False)
        root.mainloop()


class SlotNum():
    def Stopleft():
        if randLeft!=0: return print('reroll')
        if randMiddle==0 or randRight==0:
            randLeft=random.randint(1,9)
            return left.config(text=f"{randLeft}")
        if randMiddle==1 and randRight==1:
            randLeft=random.randint(1,2)
            if randMiddle==9 and randRight==9:
                pass
    
    def StopMiddle():
        def StopMiddle():
    global RandLeft,RandMiddle,RandRight
    RandMiddle=random.randint(1,9)
    middle.config(text=f'{RandMiddle}')
def StopRight():
    global RandLeft,RandMiddle,RandRight
    RandRight=1
    right.config(text=f'{RandRight}')
def reset():
    RandLeft=0
    RandMiddle=0
    RandRight=0
    left.config(text=f'{RandLeft}')
    middle.config(text=f'{RandMiddle}')
    right.config(text=f'{RandRight}')


    #スロットウィジェットの作成
    stop=tk.Button(root,text='slot',command=StopLeft)
    stop.place(x=30,y=60)
    stop=tk.Button(root,text='slot',command=StopMiddle)
    stop.place(x=80,y=60)
    stop=tk.Button(root,text='slot',command=StopRight)
    stop.place(x=130,y=60)

    clean_btn=tk.Button(root,text="close",command=close_window)
    clean_btn.place(x=0,y=0)
    rerool=tk.Button(root,text="reroll",command=reset)
    rerool.place(x=0,y=90)

    #出目ラベルの作成
    left=tk.Label(root,text=RandLeft)
    left.place(x=40,y=30)
    middle=tk.Label(root,text=RandMiddle)
    middle.place(x=90,y=30)
    right=tk.Label(root,text=RandRight)
    right.place(x=140,y=30)