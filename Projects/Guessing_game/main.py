import random
def get_number():
    while True:
        try:
            num = int(input("Guess a number between 0 and 50: "))
            break
        except ValueError:
            print("Must enter a number")
    return num

random_number  = random.randint(0,50) #Generate a number between 1 and 50 (iclusive) (1:50)
number_of_guesses = 0
while True:
    guessed_num =  get_number()
    if guessed_num == random_number:
        print(f"Correct, You get it after {number_of_guesses + 1} guesses")
        quit()
    elif guessed_num > random_number :
        print("You are above the number")
        number_of_guesses += 1
    else:
        print("You are below the number")
        number_of_guesses += 1
