import functions

functions.welcome_user()
functions.get_input()
score = 0
num_of_questions = 0
fhand = open("ques_ans.txt")
for line in fhand:
    num_of_questions += 1
    line = line.rstrip()
    question = line[:line.find("-")]
    ans = input(question)
    if ans.lower() == line[line.find("-") + 2 :].lower():
        print("Correct\U0001F44D")
        score += 1
    else:
        print("Not exactly\U0001F44E")
print("=====================================")
print(f"You got {score} questions correct out of {num_of_questions}")
print(f"Your final score is: {score*10}%")
