import random
cc=["rock","paper","scissors"]
rc= random.choice(cc)

def rock(uc):
    if rc== "rock":
        if uc=="rock":
            print("You tied!")
        elif uc=="paper":
            print("You won!")
        elif uc=="scissors":
            print("You Lose!")
        else:
            print("Invalid Option! Please select the answer through the following.")
            
def paper(uc):
    if rc== "paper":
        if uc=="rock":
            print("You Lose!")
        elif uc=="paper":
            print("You tied!")
        elif uc=="scissors":
            print("You Won!")
        else:
            print("Invalid Option! Please select the answer through the following.")
            
def scissors(uc):
    if rc== "scissors":
        if uc=="rock":
            print("You Won!")
        elif uc=="paper":
            print("You Lose!")
        elif uc=="scissors":
            print("You Tied!")
        else:
            print("Invalid Option! Please select the answer through the following.")
            

def game():
    choice=input("Enter your Choice!")
    while True:
        if choice.lower() == "rock":
            rock(choice)
        elif choice.lower() == "paper":
            paper(choice)
        elif choice.lower() == "scissors":
            scissors(choice)
        else:
            print("Invalid Option! Please select the answer throught the following.")
        print("Do you want to Continue the Game?")
        option=input("Yes/No")
        if option.lower=="yes":
            game()
        else:
            print("Thank you for playing the Game!")
            break

if __name__=="__main__":
    print("Rock, Paper and Scissor Game!")
    print("To play just enter the item you want to choose.")
    game()