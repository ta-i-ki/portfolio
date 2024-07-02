import random
import tkinter as tk
from tkinter import messagebox

class SlotMachine(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('300x150')
        self.master.resizable(False, False)
        self.master.title("Slot Machine")
        
        self.randLeft = 0
        self.randMiddle = 0
        self.randRight = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        # スロットウィジェットの作成
        self.left = tk.Label(self, text=f"{self.randLeft}")
        self.left.place(x=40, y=30)
        
        self.middle = tk.Label(self, text=f"{self.randMiddle}")
        self.middle.place(x=90, y=30)
        
        self.right = tk.Label(self, text=f"{self.randRight}")
        self.right.place(x=140, y=30)
        
        stop_left_btn = tk.Button(self, text='slot', command=self.stop_left)
        stop_left_btn.place(x=30, y=60)
        
        stop_middle_btn = tk.Button(self, text='slot', command=self.stop_middle)
        stop_middle_btn.place(x=80, y=60)
        
        stop_right_btn = tk.Button(self, text='slot', command=self.stop_right)
        stop_right_btn.place(x=130, y=60)
        
        reroll_btn = tk.Button(self, text="reroll", command=self.reset)
        reroll_btn.place(x=0, y=90)
        
        close_btn = tk.Button(self, text="close", command=self.master.destroy)
        close_btn.place(x=0, y=0)
        
        self.pack()

    def stop_left(self):
        if self.randLeft != 0:
            return self.show_information()
        if self.randMiddle == 0 or self.randRight == 0:
            self.randLeft = random.randint(1, 9)
            return self.left.config(text=f"{self.randLeft}")
        if self.randMiddle == 1 and self.randRight == 1:
            self.randLeft = random.randint(1, 2)
        elif self.randMiddle == 9 and self.randRight == 9:
            self.randLeft = random.randint(8, 9)
        self.left.config(text=f"{self.randLeft}")

    def stop_middle(self):
        if self.randMiddle != 0:
            return self.show_information()
        if self.randLeft == 1 and self.randRight == 1:
            self.randMiddle = random.randint(1, 2)
        elif self.randLeft == 9 and self.randRight == 9:
            self.randMiddle = random.randint(8, 9)
        else:
            self.randMiddle = random.randint(1, 9)
        self.middle.config(text=f"{self.randMiddle}")
        
    def stop_right(self):
        if self.randRight != 0:
            return self.show_information()
        if self.randLeft == 1 and self.randMiddle == 1:
            self.randRight = random.randint(1, 2)
        elif self.randLeft == 9 and self.randMiddle == 9:
            self.randRight = random.randint(8, 9)
        else:
            self.randRight = random.randint(1, 9)
        self.right.config(text=f"{self.randRight}")
        
    def show_information(self):
        messagebox.showinfo("注意・警告", "rerollをしてください")

    def reset(self):
        self.randLeft = 0
        self.randMiddle = 0
        self.randRight = 0
        self.left.config(text=f'{self.randLeft}')
        self.middle.config(text=f'{self.randMiddle}')
        self.right.config(text=f'{self.randRight}')

if __name__ == '__main__':
    root = tk.Tk()
    app = SlotMachine(master=root)
    app.create_widgets()
    app.mainloop()
