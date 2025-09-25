import random
import time
import sys
import os

# For Windows terminals - sets UTF-8 encoding
if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleOutputCP(65001)
    sys.stdout.reconfigure(encoding='utf-8')


choices = {"s": 1, "p": 0, "si": -1}
names = {1: "🪨 Stone", 0: "📄 Paper", -1: "✂️ Scissor"}

def print_banner():
    print("=" * 45)
    print("🎮 Welcome to Stone, Paper, Scissor Game!")
    print("=" * 45)
    print("📜 INSTRUCTIONS:")
    print("🔢 Tournament of 10 rounds")
    print("✍️ Choose from: (s = stone, p = paper, si = scissor)")
    print("❌ Type 'exit' anytime to quit")
    print("=" * 45)

def get_result(user, comp):
    if user == comp:
        return "draw"
    elif (user == 1 and comp == -1) or (user == 0 and comp == 1) or (user == -1 and comp == 0):
        return "win"
    else:
        return "lose"

def display_summary(wins, losses, draws):
    print("\n" + "🏁" * 31)
    print("🏁 Tournament Over")
    print(f"✅ Wins: {wins} | ❌ Losses: {losses} | 🤝 Draws: {draws}")
    if wins > losses:
        print(f"🏆 You win the tournament by {wins} wins!")
    elif wins < losses:
        print(f"😞 You lose the tournament by {losses} losses.")
    else:
        print(f"⚖️ It's a draw with {wins} wins each.")
    print("👋 Thank you for playing!")
    print("🏁" * 31 + "\n")

def main():
    print_banner()
    rounds, wins, losses, draws = 0, 0, 0, 0
    max_rounds = 10

    while rounds < max_rounds:
        user_input = input(f"\n🎯 Round {rounds + 1} - Enter your choice: ").strip().lower()
        
        if user_input == "exit":
            display_summary(wins, losses, draws)
            return
        
        if user_input not in choices:
            print("🚫 Invalid input. Use: s = stone, p = paper, si = scissor")
            continue
        
        user_choice = choices[user_input]
        comp_choice = random.choice(list(choices.values()))

        print(f"🧑 You chose: {names[user_choice]}")
        time.sleep(0.5)
        print(f"💻 Computer chose: {names[comp_choice]}")
        time.sleep(0.5)

        result = get_result(user_choice, comp_choice)
        if result == "win":
            print("✅ You win this round!")
            wins += 1
        elif result == "lose":
            print("❌ You lose this round!")
            losses += 1
        else:
            print("🤝 It's a draw!")
            draws += 1

        rounds += 1

    display_summary(wins, losses, draws)

if __name__ == "__main__":
    main()
