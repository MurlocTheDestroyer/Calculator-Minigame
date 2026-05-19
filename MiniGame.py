import random
import os
import time
import NewPlayerConfig as NPC
#^ haha get it? I imported the function that generates the scores for new players and they are non playable characters. I am so funny.
class Main :
    
    def __init__(self,Name,Score):
        self.Name = Name
        self.Score = Score
        
    global operatingSystem
    operatingSystem = os.name.lower()
    
    def OperatingCommand(command):
        if command == "Clear":
            match operatingSystem:
                case "posix":
                    os.system("Clear")
                case _:
                    os.system('cls')
    
    def quit(Name,Score):
        Main.OperatingCommand("Clear")
        choice = input("Are you sure you would like to quit?\n(If you do, your score will not be saved)\n(y/n): ").lower()
        match choice:
            case "y" | "yes":
                print("Starting emergency exit Program")
                os.system('exit')
            case "n" | "no":
                print("Ok let me put you back to where you are")
                Main.Calculator(Name,Score)
            case _:
                print("Bro make a choice 1 or 2")

    def Calculator(Name, Score):
        Symbols=["+","-","*","/"]
        print("\tThe Bestest Coolest Difficulty Meter Of All Time!\n" +
        "_____________________________________________________________________\n" +
        "\t1. Im too young to be losing! (+3)\n" +
        "\t2. Be Gentle! (+5)\n" +
        "\t3. Hey, not too rough! (+8)\n" +
        "\t4. Watch me lose! (+13)\n" +
        "\t5. I Own This Game! (+21)\n" +
        "_____________________________________________________________________\n")

        difficulty=(input("Please enter the number of the desired difficulty: "))
        try:
            difficulty=int(difficulty)
        except ValueError:
            if difficulty == "q" or difficulty == "quit":
                Main.quit(Name, Score)
        else:
            X=0
            Y=0
            match difficulty:

                case 1:
                    X=random.randint(1,25)
                    Y=random.randint(1,25)
                    Reward=3
                case 2:
                    X=random.randint(26,99)
                    Y=random.randint(26,99)
                    Reward=5
                case 3:
                    X=random.randint(100,249)
                    Y=random.randint(100,249)
                    Reward=8
                case 4:
                    X=random.randint(250,499)
                    Y=random.randint(250,499)
                    Reward=13
                case 5:
                    X=random.randint(500,1000)
                    Y=random.randint(500,1000)
                    Reward=21
                case _:
                    print("Lets try this again")
                    Main.Calculator(Name, Score)
            
            Main.OperatingCommand("Clear")
            Mode = Symbols[random.randint(0,3)]
            match Mode:
                case "+":
                    Total=X+Y
                case "-":
                    Total=X-Y
                case "*":
                    if Reward == 3:
                        X = random.randint(1,12)
                        Y = random.randint(1,12)
                    Total=X*Y
                case "/":
                    if Reward == 3:
                        X = random.randint(1,12)
                        Y = random.randint(1,12)
                    Total=round(X/Y,1)
                case _:
                    print("Thats it")
                    Main.Calculator(Name, Score)

            Main.OperatingCommand("Clear")
            Guess = input(f"What does {X} {Mode} {Y} = ? :\t")
            time.sleep(2)
            try:
                if Mode == "/":
                    Guess=float(Guess)
                else:
                    Guess=int(Guess)
            except ValueError:
                if Guess == "quit" or Guess == "q":
                    Main.quit(Name,Score)
            else:
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
        time.sleep(1)
        rematch=input("Go another round and risk it for more points? \n1. I'm no Chump!\n2. Spare Me!\n")
        try:
            rematch=int(rematch)
        except ValueError:
            print("Get load of this guy. He cant even pick 1 or 2. Lets try this again")
            Main.Replay(Name,Score)
        else:
            time.sleep(1)
            match rematch:
                case 1:
                    Main.OperatingCommand("Clear")
                    print("Youve got the spunk kid!\n")
                    Main.Calculator(Name,Score)
                case 2:
                    if Score == 0:
                        print("Womp Womp Chump!")
                    else:
                        with open("History Saved Scores.txt","at") as f:
                            f.write(f"{Name} : {Score}\n")
                        #sort the scores in the file as well as correctly sorting in the new score
                        with open("History Saved Scores.txt","rt") as f:
                            lines = f.readlines()
                            lines.sort(key=lambda x: int(x.split(":")[1].strip()), reverse=True)
                        with open("History Saved Scores.txt","wt") as f:
                            f.writelines(lines)
                        print("Score saved! See ya later!")
                        print("Top 5 Scores:")
                        with open("History Saved Scores.txt","rt") as f:
                            for i in range(5):
                                line = f.readline()
                                if line:
                                    print(line.strip())
                    q=input("Please press enter to close program")
                case _:
                    print("Yikers. Pick 1 or 2")
                    Main.Replay(Name,Score)
Main.OperatingCommand("Clear")
print("Version 2.5")
Player1=input("What is your name before we begin:\n")
print(f"Hello, {Player1}!\n")
time.sleep(2)
NPC.generate_scores()
Main.Calculator(Player1,0)
