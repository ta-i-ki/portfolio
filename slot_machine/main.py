import tkinter as tk
import random

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")

        # リールの設定
        self.reel_symbols = ["🍒", "🔔", "🍋", "⭐", "🍉", "7"]
        self.reels = [tk.Label(root, text="", font=("Helvetica", 48)) for _ in range(3)]
        
        for i, reel in enumerate(self.reels):
            reel.grid(row=0, column=i, padx=10)

        self.stop_buttons = [tk.Button(root, text=f"Stop Reel {i+1}", command=lambda i=i: self.stop_reel(i), state="disabled", font=("Helvetica", 16)) for i in range(3)]
        
        for i, button in enumerate(self.stop_buttons):
            button.grid(row=1, column=i, pady=10)
        
        # コントロールパネルの設定
        self.credit = 100
        self.credit_label = tk.Label(root, text=f"Credits: {self.credit}", font=("Helvetica", 24))
        self.credit_label.grid(row=2, column=0, columnspan=3)

        self.spin_button = tk.Button(root, text="Spin", command=self.spin, font=("Helvetica", 24))
        self.spin_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 24))
        self.exit_button.grid(row=3, column=2, pady=10)

    def spin(self):
        if self.credit <= 0:
            self.credit_label.config(text="Credits: 0 - Game Over")
            return
        
        self.credit -= 1
        self.credit_label.config(text=f"Credits: {self.credit}")
        
        self.results = [None] * 3
        for i, button in enumerate(self.stop_buttons):
            button.config(state="normal")
        
        self.spin_button.config(state="disabled")
    
    def stop_reel(self, index):
        self.results[index] = random.choice(self.reel_symbols)
        self.reels[index].config(text=self.results[index])
        self.stop_buttons[index].config(state="disabled")

        if all(result is not None for result in self.results):
            self.spin_button.config(state="normal")
            if len(set(self.results)) == 1:
                self.credit += 10
                self.credit_label.config(text=f"Credits: {self.credit} - You Win!")
            else:
                self.credit_label.config(text=f"Credits: {self.credit}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
