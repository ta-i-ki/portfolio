# seven-decoda
print(" --")
print("|",end="")
print("  |")
print(" --")
print("|",end="")
print("  |")
print(" --")

import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self,master):
        #super().__init__(master)
        #self.pack()

        self.master.geometry("300x300")
        self.master.title("Tkinter with Class Template")

        self.create_widgets()

    def create_widgets(self):
        pass

    def callBack(self):
        pass

def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()