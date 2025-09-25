## stone paper seisor game ##

import random

dict={"s":1, "p":0, "si":-1,}
revdict={1:"stone",0:"paper",-1:"seisor"}

print("="*41)
print("🎮 Welcome to Stone, Paper, Scissor Game!")
print("="*41)
print("-"*42)
print("INSTRUCTION ARE:")
print("🏁 The Tournament is of 10 rounds")
print("choose from (s=stone, p=paper , si=seisor)")
print("Type 'exit' to leave the game")
print("-"*42)


rounds = 0
max_rounds = 10
wins=0
looses=0
draws=0

while True:
    if rounds >= max_rounds:
        print("\n")
        print("🏁"*31)
        print("🏁 10 rounds completed.")
        print(f"✅ Wins: {wins}")
        print(f"❌ Losses: {looses}")
        print(f"🤝 Draws: {draws}")
        if(wins>looses):
            print(f"📊 Final decision: You win the tournament by {wins} wins.")
        elif(wins<looses):
            print(f"📊 Final decision: You loose the tournament by {looses} losses.")
        else:
            print(f"📊 Final decision: The tournament is draw by {wins} wins & {looses} looses")
        print("👋 Thank you for playing!")
        print("🏁"*31)
        break
    print("\n")
    comp=random.choice([1,0,-1])
    youstr=input(f"Round {rounds+1} - Enter your choice:").strip().lower()
    
    if(youstr=="exit"):
        print("\n")
        print("🏁"*31)
        print("Exited manually.")
        print(f"✅ Wins: {wins}")
        print(f"❌ Losses: {looses}")
        print(f"🤝 Draws: {draws}")
        if(wins>looses):
            print(f"📊 Final decision: You win the tournament by {wins} wins.")
        elif(wins<looses):
            print(f"📊 Final decision: You loose the tournament by {looses} losses.")
        elif(wins==looses):
            print(f"📊 Final decision: The tournament is draw by {wins} wins & {looses} looses")
        print("👋 Thank you for playing!")
        print("🏁"*31)
        break

    
    if youstr not in dict:
        print("❌ Invalid input. Please enter 's=stone', 'p=paper', or 'si=scissor'.")
        continue

    you= dict[youstr]
    print(f"🧑 you choice: {revdict[you]}\n💻 computer choice: {revdict[comp]}")

    if (comp==you):
        print("it's draw 🤝.")
        draws+=1
    elif (comp==1 and you==0)or\
            (comp==0 and you==-1)or\
            (comp==-1 and you==1):
        print("you win! ✅")
        wins+=1  
    else:
        print("you loose! ❌")
        looses+=1

    rounds += 1    

            
        





            


            
            
            

                    