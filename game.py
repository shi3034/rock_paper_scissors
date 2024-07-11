import random

#taking user's turn as input
choice=input("enter your choice: rock, paper or scissors:").lower()

#creating a dictionary of choices
choices={
    "rock":0,
    "paper":1,
    "scissors":-1
}

user=choices[choice]  #storing user's choice as 0,1 or -1

#creating a reverse dictionary of choices
rev_choices={
    0:"rock",
    1:"paper",
    -1:"scissors"
}

#generating computer's choice
comp=random.choice([0,1,-1])

print(f"You have chosen {choice} and the computer has chosen {rev_choices[comp]} ")

#evaluating the winner based on their choices
if user==comp:
    print("DRAW!!")
else:
    if user==0 and comp==1:
        print("YOU LOSE!!")
    elif user==0 and comp==-1:
        print("YOU WIN!!")
    elif user==1 and comp==0:
        print("YOU WIN!!")
    elif user==1 and comp==-1:
        print("YOU LOSE!!")
    elif user==-1 and comp==0:
        print("YOU LOSE!!")
    else:
        print("YOU WIN!!")
        

    
    

