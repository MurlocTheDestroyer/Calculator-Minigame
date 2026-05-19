import random
def generate_scores():
    try:
        open("History Saved Scores.txt","x")
    except FileExistsError:
        return(print("History Saved Scores.txt already exists. No preparation needed. Have Fun!"))
    else:
        #create 5 random scores for the new file to make it look like there are already players and scores in the file. This is just for fun and to make it look like the game has been played before.
        names=["Bob","John","Sally","Jane","Tom","Tim","Sara","Emily","Michael","Jessica","David","Daniel","Ashley","Megan","Chris","Amanda","James","Ryan","Lauren","Justin"]
        with open("History Saved Scores.txt","at") as g:
            for i in range(5):
                Name = random.choice(names)
                Score = random.randint(0,50)
                g.write(f"{Name} : {Score}\n")
        #sort the scores that were just generated
        with open("History Saved Scores.txt","rt") as f:
            lines = f.readlines()
            lines.sort(key=lambda x: int(x.split(":")[1].strip()), reverse=True)
        with open("History Saved Scores.txt","wt") as f:
            f.writelines(lines)
        return(print("Welcome new player!\nGeneric Saved Scores have been generated in the newly created file (History Saved Scores.txt)"))