import time

#welcome_user -- Display a welcome message to the user and make him wait for five seconds
def welcome_user():
    print("Welcome to the computer quiz game")
    for _ in range(5):
        time.sleep(1)
        print("*")


# get_input - Ask the user if he wants to play or not and print a message according to the answer
def get_input():
    while True:
        answer = input("Do you want to play:(Y/N): ")
        match answer.lower():
            case "y":
                print("Good! Let' start, Get Ready:)")
                for _ in range(5):
                    time.sleep(1)
                    print("*")
                break
            case "n":
                print("Sad! See you later:(")
                quit()
            case _:
                print("Invalid option")
