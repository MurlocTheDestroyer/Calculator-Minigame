import random
import os
import time
class Main :
    def __init__(self,Name,Score=0,BeastMode=False,BeastCounter=0):
        self.Name = Name
        self.Score = Score
        self.BeastMode = BeastMode
        self.BeastCounter = BeastCounter
    
    def OperatingCommand(command):
        operatingSystem = os.name.lower()
        if command == "Clear":
            match operatingSystem:
                case "posix":
                    os.system("Clear")
                case _:
                    os.system('cls')
    
    def generate_scores():
        try:
            open("History Saved Scores.txt","x")
        except FileExistsError:
            return(input("History Saved Scores.txt already exists. No preparation needed. Have Fun!\n\nPlease hit the Enter key to continue: "))
        else:
            #Create 5 random scores for the new file to make it look like there are already players and scores in the file. 
            #This is just for fun and to make it look like the game has been played before.
            names=["Bob","John","Sally","Jane","Tom","Tim","Sara","Emily","Michael","Jessica","David","Daniel","Ashley","Megan","Chris","Amanda","James","Ryan","Lauren","Justin"]
            duplicates = []
            with open("History Saved Scores.txt","at") as g:
                for i in range(5):
                    Name = random.choice(names)
                    while Name in duplicates:
                        Name = random.choice(names)
                    duplicates.append(Name)
                    Score = random.randint(0,50)
                    g.write(f"{Name} : {Score}\n")
            #sort the scores that were just generated
            with open("History Saved Scores.txt","rt") as f:
                lines = f.readlines()
                lines.sort(key=lambda x: int(x.split(":")[1].strip()), reverse=True)
            with open("History Saved Scores.txt","wt") as f:
                f.writelines(lines)
            return(input("\nWelcome new player!\nGeneric Saved Scores have been generated in the newly created file (History Saved Scores.txt)\n\nPlease hit the Enter key to continue: "))
        
    def WinnerZone(self,Name):
        try:
            open("Slayer History.txt","x")
        except FileExistsError:
            with open("Slayer History.txt","at") as f:
                f.write(f"B3AST SL4Y3R : {Name}\n")
            return(print(f"Congratulations B3AST SL4Y3R {Name}!\n\nYour name has just been added to your existing Slayer History.txt file!\n"))
        else:
            with open("Slayer History.txt","at") as f:
                f.write("B3AST SL4Y3RS\n")
                f.write("________________________\n")
            with open("Slayer History.txt","at") as f:
                f.write(f"B3AST SL4Y3R : {Name}\n")
            return(print(f"Congratulations B3AST SL4Y3R {Name}!\n\nYour name has just been added to the newly created Slayer History.txt file!\n"))
        
    def quit(self, Name, Score, BeastMode, BeastCounter):
        self.OperatingCommand("Clear")
        choice = input("Are you sure you would like to quit?\n(If you do, your score will not be saved)\n(y/n): ").lower()
        match choice:
            case "y" | "yes":
                print("Starting emergency exit Program")
                return os.system('exit')
            case "n" | "no":
                print("Ok let me put you back to where you are")
                return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
            case _:
                print("Bro make a choice 1 or 2")
                return Main.quit(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)

    def ActivatedBeastMode (self, Name, Score, BeastMode, BeastCounter):
        if Score < 50:
            difficulty = random.randint(1,5)
        elif 50 <= Score <= 100:
            difficulty = random.randint(2,5)
        elif 100 < Score <= 200:
            difficulty = random.randint(3,5)
        elif 200 < Score <= 300:
            difficulty = random.randint(4,5)
        elif 300 < Score <= 400:
            difficulty = random.randint(4,5)
        elif 400 < Score <= 500:
            difficulty = 5
        else:
            pass
        match difficulty:
        
            case 1:
                X=random.randint(1,99)
                Y=random.randint(1,99)
                Reward=3*4
            case 2:
                X=random.randint(100,499)
                Y=random.randint(100,499)
                Reward=5*4
            case 3:
                X=random.randint(500,999)
                Y=random.randint(500,999)
                Reward=8*4
            case 4:
                X=random.randint(1000,2499)
                Y=random.randint(1000,2499)
                Reward=13*4
            case 5:
                X=random.randint(2500,5000)
                Y=random.randint(2500,5000)
                Reward=21*4
            case _:
                print("Invalid difficulty level.")
                return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
        Symbols=["+","-","*","/"]
        Mode = Symbols[random.randint(0,3)]
        match Mode:
            case "+":
                Total=X+Y
            case "-":
                Total=X-Y
            case "*":
                Total=X*Y
            case "/":
                Total=round(X/Y,2)
            case _:
                print("Yikes. Something went wrong. Lets try this again")
                return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
        Main.OperatingCommand("Clear")
        print ("SoRrY bUt IlL Be TaKiNg ThE ReInS FoR a BiT. I Am ThE BEAST, I HoPe YoU ArE ReAdY To MeEt ThE SaMe FaTe as HiM!\n\n")
        print("LeTs SeE HoW YoU Do WiTh ThIs PrObLeM!\n")
        print (f"Difficulty: {difficulty} \nCurrent Score: ({Score} / 500) points\n\n")
        time.sleep(3)
        if Mode == "/":
            print("Round to the nearest hundredth if necessary\n")
        Guess = input(f"What does {X} {Mode} {Y} = ? :\t")
        time.sleep(2)
        try:
            if Mode == "/":
                Guess=float(Guess)
            else:
                Guess=int(Guess)
        except ValueError:
            Guess = Guess.lower()
            if Guess == "quit" or Guess == "q":
                print("IM SORRY BUT YOU CANT QUIT NOW! YOU ARE IN BEAST MODE!")
                time.sleep(2)
                return Main.ActivatedBeastMode(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
            else:
                print(f"Wrong the answer is {Total}. No Second Chances Here!")
                time.sleep(2)
                Score=0
                return Main.BeastReplay(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
        else:
            if Guess == Total:
                time.sleep(2)
                print("Correct!")
                Score+=Reward*4 
            else:
                time.sleep(2)
                print(f"Wrong the answer is {Total}. No Second Chances Here!")
                time.sleep(2)
                Score=0
            return Main.BeastReplay(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)

    def BeastReplay(self,Name,Score,BeastMode,BeastCounter):
        if Score == 0:
            time.sleep(1)
            print (Name + " has been defeated by the BEAST!\n\nBetter luck next time!")
            BeastMode = False
            time.sleep(3)
            return
        elif Score >= 500:
            time.sleep(1)
            print (Name + " has defeated the BEAST! YOU WIN!\n\nYou have earned the title of ( B3AST SL4Y3R ) !")
            Main.WinnerZone(Main, Name=Name)
            time.sleep(5)
        else:
            time.sleep(1)
            print ("LuCkY GuEsS, BuT YoU HaVeNt BeAtEn Me YeT!")
            time.sleep(5)
            return Main.ActivatedBeastMode(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
        input("Please hit the Enter key to continue: ")

    def Calculator(self, Name, Score, BeastMode, BeastCounter):
        Symbols=["+","-","*","/"]
        print("\n\tThe Bestest Coolest Difficulty Meter Of All Time!\n" +
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
            difficulty = difficulty.lower()
            if difficulty == "q" or difficulty == "quit":
                return Main.quit(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
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
                print("Lets try this again\n")
                if BeastMode == False:
                    #Beast indincator step 1
                    if BeastCounter >= 1:
                        print("Hey, Im guessing that you are new to this game all you have to do is input a number between 1 and 5 and press Enter.\n\n")
                        input("Please hit the Enter key to continue: ")
                        Main.OperatingCommand("Clear")
                        pass
                    else:
                        BeastCounter+=1
                return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)

            
        Main.OperatingCommand("Clear")
        if BeastMode == False:
            #Beast indincator step 2
            BeeMode=input("Sorry but I put this in to control the flow of the game. Please hit the Enter key and we can continue: ")
            if BeeMode == "Call His Name" and BeastCounter == 1:
                BeastCounter+=1
                print(f"Haha, Let's not do AnYtHiNg CrAzY B0DAK!")
                time.sleep(5)
                return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
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
                print("Yikes. Something went wrong. Lets try this again")
                return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)

        Main.OperatingCommand("Clear")
        print("Please answer the following problem:\n")
        print (f"Difficulty: {difficulty} \nCurrent Score: {Score} points\n")
        Guess = input(f"What does {X} {Mode} {Y} = ? :\t")
        time.sleep(2)
        try:
            if Mode == "/":
                Guess=float(Guess)
            else:
                Guess=int(Guess)
        except ValueError:
            if Guess == "quit" or Guess == "q" or Guess == "Quit" or Guess == "Q":
                Main.quit(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
            if Guess == "B0DAK IS GONE":
                #Beast indincator step 3
                print("You are correct! Oh No! No Wait! What have you done! Youve Doomed Us All!\n")
                BeastMode = True
                time.sleep(5)
                return Main.ActivatedBeastMode(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
        else:
            if Guess == Total:
                print("Correct!")
                Score+=Reward
                return Main.Replay(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
            else:
                print(f"Wrong the answer is {Total}. Your Score of {Score} has now been reset!")
                Score=0
                return Main.Replay(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
            
    def Replay(self,Name,Score,BeastMode,BeastCounter):
        print("______________________________________________________________________________")
        time.sleep(2)
        print(f"{Name} has a total of {Score} points!\n")
        time.sleep(1)
        rematch=input("Go another round and risk it for more points? \n1. I'm no Chump!\n2. Spare Me!\n")
        try:
            rematch=int(rematch)
        except ValueError:
            print("Get load of this guy. He cant even pick 1 or 2. Lets try this again")
            return Main.Replay(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
        else:
            time.sleep(1)
            match rematch:
                case 1:
                    Main.OperatingCommand("Clear")
                    print("Youve got the spunk kid!\n")
                    return Main.Calculator(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
                case 2:
                    if Score == 0:
                        print("Womp Womp, no score to save! See ya later!")
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
                        print("Top Scores:\n")
                        print("______________________________________________________________________________\n")
                        with open("History Saved Scores.txt","rt") as f:
                            for i in range(10):
                                line = f.readline()
                                if line:
                                    print(f"{i+1}. {line.strip()}")
                        print("\n______________________________________________________________________________")
                    input("Please press enter to close program")
                case _:
                    print("Yikers. Pick 1 or 2")
                    return Main.Replay(Main,Name=Name, Score=Score, BeastMode=BeastMode, BeastCounter=BeastCounter)
Main.OperatingCommand("Clear")
Main.generate_scores()
Player=input("What is your name before we begin:\n")
print(f"Hello, {Player}!\n")
time.sleep(2)
Main.Calculator(Main,Name=Player, Score=0, BeastMode=False, BeastCounter=0)