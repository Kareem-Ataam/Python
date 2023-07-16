import random
print("Welcome to the Rock, Paper, Scissors game:)")
game_options = ["rock","papper","scissors"]
user_score = 0
computer_score  = 0
while True:
    user_choice = input("Type Rock or Papper or Scissors or Q to quit the game: ")
    computer_choice  = random.choices(game_options)
    match user_choice.lower():
        case "rock":
            if computer_choice[0] == "paper":
                computer_score += 1
                print("Computer chose papper and win")
            elif computer_choice[0] == "scissors":
                user_score += 1
                print("Computer chose scissors and you win")
            else:
                print("Computer also chose rock, no one win") 
        case "papper":
            if computer_choice[0] == "scissors":
                computer_score += 1
                print("Computer chose scissors and win")
            elif computer_choice[0] == "rock":
                user_score += 1
                print("Computer chose rock and you win")
            else:
                print("Computer also chose papper, no one win") 
        case "scissors":
            if computer_choice[0] == "rock":
                computer_score += 1
                print("Computer chose rock and win")
            elif computer_choice[0] == "papper":
                user_score += 1
                print("Computer chose papper and you win")
            else:
                print("Computer also chose scissors, no one win")
        case "q":
            break
        case "_":
            print("Invalid Option")
if user_score > computer_score:
    print(f"Your score:    {user_score} \U0001F947")
    print(f"Computer score:{computer_score}")
elif user_score < computer_score:
    print(f"Your score:    {user_score}")
    print(f"Computer score:{computer_score} \U0001F947")
else:
    print(f"Your score:    {user_score}")
    print(f"Computer score:{computer_score}") 
print("Thanks for participating in our game\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f")