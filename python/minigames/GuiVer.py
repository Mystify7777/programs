import tkinter as tk
from tkinter import messagebox
import random

choices = ["Stone", "Paper", "Scissor"]

def get_winner(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "Stone" and comp == "Scissor") or \
         (user == "Paper" and comp == "Stone") or \
         (user == "Scissor" and comp == "Paper"):
        return "Win"
    else:
        return "Lose"

class GameApp:
    def __init__(self, master):
        self.master = master
        self.round = 0
        self.max_rounds = 10
        self.wins = 0
        self.losses = 0
        self.draws = 0

        master.title("Stone Paper Scissor Game")
        master.geometry("400x300")
        master.configure(bg="#f0f0f0")

        self.label = tk.Label(master, text="🎮 Choose your move:", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(master, bg="#f0f0f0")
        self.buttons_frame.pack()

        for choice in choices:
            btn = tk.Button(self.buttons_frame, text=choice, width=10,
                            command=lambda c=choice: self.play_round(c))
            btn.pack(side="left", padx=10, pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="#f0f0f0")
        self.result_label.pack(pady=20)

    def play_round(self, user_choice):
        if self.round >= self.max_rounds:
            return

        comp_choice = random.choice(choices)
        result = get_winner(user_choice, comp_choice)

        if result == "Win":
            self.wins += 1
        elif result == "Lose":
            self.losses += 1
        else:
            self.draws += 1

        self.round += 1
        self.result_label.config(text=f"You: {user_choice} | Computer: {comp_choice}\nResult: {result}")

        if self.round == self.max_rounds:
            self.show_summary()

    def show_summary(self):
        messagebox.showinfo("🏁 Tournament Over",
                            f"Wins: {self.wins}\nLosses: {self.losses}\nDraws: {self.draws}\n\n"
                            f"{'You Win! 🏆' if self.wins > self.losses else 'You Lose 😞' if self.losses > self.wins else 'Draw ⚖️'}")
        self.master.quit()

root = tk.Tk()
game = GameApp(root)
root.mainloop()
