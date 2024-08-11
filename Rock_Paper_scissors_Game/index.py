import random

while True:
    choice=['rock','paper','scissors']
    computer=random.choice(choice)
    player=None
    while player not in choice:
        player=input("rock,paper, or scissors?: ")
    if player== computer:
        print("Computer: "+computer)
        print("Player: "+player)
        print("Tie!!")
    elif player=="rock":
        if computer=="paper":
            print("Computer: "+computer)
            print("Player: "+player)
            print("You lose!!")
        if computer=="scissors":
            print("Computer: "+computer)
            print("Player: "+player)
            print("You won!!")
    elif player=="paper":
        if computer=="rock":
            print("Computer: "+computer)
            print("Player: "+player)
            print("You win!!")
        if computer=="scissors":
            print("Computer: "+computer)
            print("Player: "+player)
            print("You lose!!")
    elif player=="scissors":
        if computer=="paper":
            print("Computer: "+computer)
            print("Player: "+player)
            print("You win!!")
        if computer=="rock":
            print("Computer: "+computer)
            print("Player: "+player)
            print("You lose!!")
    play_again=input("Play again? (yes/no): ").lower()

    if play_again !="yes":
        break
print("Bye")
