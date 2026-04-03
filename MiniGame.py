import random
import os
import time
class Main :
    def __init__(self,Name,Score):
        self.Name = Name
        self.Score = Score

    def ClearScreen ():
        if (os.name.lower() == "posix"):
            return (os.system('clear'))
        else:
            return (os.system('cls'))
        
    def quit(Name,Score):
        Main.ClearScreen()
        choice = input("Would you like to quit?").lower()
        if choice == "y" or choice == "yes":
            print("exiting Program")
            os.system('exit')
        elif choice == "n" or choice == "no":
            print("Ok let me put you back to where you are")
            Main.Calculator(Name,Score)

    def Calculator(Name, Score):
        print("\t\tThe Bestest Coolest Difficulty Meter Of All Time!")
        print("_____________________________________________________________________")
        print("1. Im too young to be losing! (+1)")
        print("2. Be Gentle! (+2)")
        print("3. Hey, not too rough! (+5)")
        print("4. Watch me lose! (+8)")        
        print("5. I Own This Game! (+13)")
        print("_____________________________________________________________________")
        difficulty=(input("Please enter the number of the desired difficulty: "))
        if difficulty == "q" or difficulty == "quit":
            Main.quit(Name, Score)
        else:
            difficulty=int(difficulty)
            X=0
            Y=0
            if difficulty == 1:
                X=random.randint(1,25)
                Y=random.randint(1,25)
                Reward=1
            elif difficulty == 2:
                X=random.randint(26,99)
                Y=random.randint(26,99)
                Reward=2
            elif difficulty == 3:
                X=random.randint(100,249)
                Y=random.randint(100,249)
                Reward=5
            elif difficulty == 4:
                X=random.randint(250,499)
                Y=random.randint(250,499)
                Reward=8
            elif difficulty == 5:
                X=random.randint(500,1000)
                Y=random.randint(500,1000)
                Reward=13
            else:
                print("Lets try this again")
                Main.Calculator(Name, Score)
        Main.ClearScreen()
        Mode = random.randint(1,4)
        if Mode == 1:
            Total=Y+X
            symbol="+"
        elif  Mode == 2:
            Total=Y-X
            symbol="-"
        elif Mode == 3:
            Total=Y*X
            symbol="*"
        elif Mode == 4:
            Total=round(Y/X,1)
            symbol="/"
        
        else:
            print("Thats it")
            Main.Calculator(Name, Score)

        Main.ClearScreen()
        Guess= input(f"What does {Y} {symbol} {X} = ? :\t")
        time.sleep(2)
        if Guess == "quit" or Guess == "q":
            Main.quit(Name,Score)
        elif symbol == "/":
            Guess=float(Guess)
        else:
            Guess=int(Guess)

        if Guess == Total:
            print("Correct!")
            Score+=Reward
            Main.Replay(Name,Score)
        else:
            print(f"Wrong the answer is {Total}. Your Score of {Score} has now been reset!")
            Score=0
            Main.Replay(Name,Score)
            
    def Replay(Name,Score):
        print("______________________________________________________________________________")
        time.sleep(2)
        if Score == 1:
            print(f"{Name} has a total of {Score} point!\n")
        else:
            print(f"{Name} has a total of {Score} points!\n")
        time.sleep(2)
        Huh=int(input("Go another round and risk it for more points? \n1. I'm no Chump!\n2. Spare Me!\n Your Choice: "))
        time.sleep(2)
        if Huh == 1:
            Main.ClearScreen()
            print("Youve got the spunk kid!\n")
            Main.Calculator(Name,Score)
        elif Huh == 2:
            if Score == 0:
                print("Womp Womp Chump!")
            else:
                g=open("History Saved Scores.txt","at")
                g.write(f"{Name} : {Score}")
                print("See ya later!")
            q=input("Please press enter to close program")
        else:
            print("Yikers. Pick 1 or 2")
            Main.Replay(Name,Score)
Main.ClearScreen()
print("Version 2.3")
Player1=input("What is your name before we begin:\n")
print(f"Hello, {Player1}!\n")
time.sleep(3)
Main.Calculator(Player1,0)