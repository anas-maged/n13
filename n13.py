import random
rock = "🪨"
paper = "📃"
sci = "✂️"
cran = random.choice(["rock", "paper", "scissors"])
if cran == "rock": 
    vran = "🪨" 
elif cran == "paper":
    vran = "📃"
else:
    vran = "✂️"   
print("welcome to the rock , paper , scissors game: ")
us = input("press 'Enter' to contune or type [Help] for the rules help... \n").capitalize()
while True :
    if us == "Help":
        print("       ********* RULES *********")
        print("       1) you choose and the caputer chooses ")
        print("       2) rock smashes scissors ->  rock wins")
        print("       3) scissors cut paper -> sicssors wins")
        print("       4)paper cover rock -> paper wins")
        break

    elif us :
        print("sorry, choose 'Help' or press 'Enter'")

    else:
        break

print("")
while True:
    cho = input("Enter your choice [rock, paper, scissors]:  ").lower()
    if cho == "rock" :
        print("")
        print("your chose:")
        print("")
        print("")
        print(rock)
        print("")
        print("camputer chose:")
        print("")
        print(vran)
        if vran == rock:
            print("")
            print(f"the result: draw, the camputer result was: {vran}")
        elif vran == "✂️":
            print("")
            print(f"good you win, the camputer result: {vran}")
        else:
            print("")
            print(f"sorry you lose, the camputer result was: {vran}")
        break
    elif cho == "paper":
        print("")
        print("your chose:")
        print("")
        print("")
        print(paper)
        print("")
        print("camputer chose:")
        print("")
        print(vran)
        if vran == paper :
                    print("")
                    print(f"the result: draw, the camputer result was: {vran}")
        elif vran == "🪨":
                    print("")
                    print(f"good you win, the camputer result: {vran}")
        else:
                    print("")
                    print(f"sorry you lose, the camputer result was: {vran}")
        break
    elif cho == "sicssor":
        print("")
        print("your chose:")
        print("")
        print("")
        print(sci)
        print("")
        print("camputer chose:")
        print("")
        print(vran)
        if vran == sci:
                    print("")
                    print(f"the result: draw, the camputer result was: {vran}")
        elif vran == "📃":
                    print("")
                    print(f"good you win, the camputer result: {vran}")
        else:
                    print("")
                    print(f"sorry you lose, the camputer result was: {vran}")
        break
    else:
        print("")
        print("sorry, choice [rock, paper, scissors]: ")
