import random
import tkinter as tk

RandLeft=0
RandMiddle=0
RandRight=0

#ウィンドウの作成
root=tk.Tk()
#root.geometry('')
#root.resizable(True,True)

#ウィンドウを閉じるボタン
def close_window():
    root.destroy()


#スロットの目
def StopLeft():
    global RandLeft,RandMiddle,RandRight
    if RandMiddle==1 and RandRight==1:
        RandLeft=random.randint(1,2)
        return left.config(text=f"{RandLeft}")
    if RandMiddle==9 and RandRight==9:
        RandLeft=random.randint(8,9)
        return left.config(text=f"{RandLeft}")
    if RandLeft!=0: return print('rerollしてください')
    else:
        RandLeft=random.randint(1,9)
        return left.config(text=f"{RandLeft}")

def StopMiddle():
    global RandLeft,RandMiddle,RandRight
    if RandLeft==1 and RandRight==1:
        RandMiddle=random.randint(1,2)
        return middle.config(text=f"{RandMiddle}")
    if RandLeft==9 and RandRight==9:
        RandMiddle=random.randint(8,9)
        return middle.config(text=f"{RandMiddle}")
    if RandMiddle!=0: return print('rerollしてください')
    else:
        RandMiddle=random.randint(1,9)
        return middle.config(text=f"{RandMiddle}")

def StopRight():
    global RandLeft,RandMiddle,RandRight
    if RandLeft==1 and RandMiddle==1:
        RandRight=random.randint(1,2)
        return right.config(text=f"{RandRight}")
    if RandLeft==9 and RandMiddle==9:
        RandRight=random.randint(8,9)
        return right.config(text=f"{RandRight}")
    if RandRight!=0: return print('rerollしてください')
    else:
        RandRight=random.randint(1,9)
        return right.config(text=f"{RandRight}")
def reset():
    global RandLeft,RandMiddle,RandRight
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

root.mainloop()
