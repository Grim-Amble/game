
playername=input("What would you like your chaceters name to be ")
gamestarter=input("would you like to continue (y/n)")

if gamestarter==("y"):
    gamestarted=(True)

elif gamestarter==("n"):
    gamestarted=(False)

def taxi():
    print("you call a Tox (like an uber but uber was bought and killed by microsoft in 2036)")
    print('He askes you where you want to go')
def game():
    if gamestarted==(True):
        print("started")
        taxi()

        first=input(" ")
        if first==("left"):
            print("you went left")
        elif first==("right"):
            print("you went right")  
        else:
            quit=input("Do you want to quit?(y/n) ")
        if quit==("y"):
            print("quited")

game()