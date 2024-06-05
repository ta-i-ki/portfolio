import random
import tkinter as tk

#ウィンドウの作成
root=tk.Tk()
#root.geometry('')
#root.resizable(True,True)


#ウィンドウを閉じるボタン
def close_window():
    root.destroy()


stop_number=[0]*3
#スロットの目
def randnum0():
    if stop_number[0]!=0: print('rerollしてください')
    if stop_number[1]==0 or stop_number[2]==0:
        stop_number[0]=random.randint(1,9)
        reel1.config(text=f"{stop_number[0]}")
    if stop_number[1]==1 and stop_number[2]==1:
        stop_number[0]=random.randint(1,2)
    if stop_number[1]==9 and stop_number[2]==9:
        pass
   


def randnum1():
    stop_number[1]=1
    reel2.config(text=f'{stop_number[1]}')
def randnum2():
    stop_number[2]=1
    reel3.config(text=f'{stop_number[2]}')
def reset():
    for i in range(3):
        stop_number[i]=0
    reel1.config(text=f'{stop_number[0]}')
    reel2.config(text=f'{stop_number[1]}')
    reel3.config(text=f'{stop_number[2]}')




#スロットウィジェットの作成
stop=tk.Button(root,text='slot',command=randnum0)
stop.place(x=30,y=60)
stop=tk.Button(root,text='slot',command=randnum1)
stop.place(x=80,y=60)
stop=tk.Button(root,text='slot',command=randnum2)
stop.place(x=130,y=60)

clean_btn=tk.Button(root,text="close",command=close_window)
clean_btn.place(x=0,y=0)
rerool=tk.Button(root,text="reroll",command=reset)
rerool.place(x=0,y=90)

reel1=tk.Label(root,text=stop_number[0])
reel1.place(x=40,y=30)
reel2=tk.Label(root,text=stop_number[1])
reel2.place(x=90,y=30)
reel3=tk.Label(root,text=stop_number[2])
reel3.place(x=140,y=30)


root.mainloop()