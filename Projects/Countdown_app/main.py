import datetime

user_input = input("Enter your goal followed by the deadline:(goal:date)\n").split(":")
user_goal = user_input[0]
deadline_str = user_input[1]

# Converting the date in string format to a date format
deadline_date = datetime.datetime.strptime(deadline_str, "%d.%m.%Y")

days_till_deadline = (deadline_date - datetime.datetime.today()).days

if days_till_deadline < 0:
    print("Deadline must be in the future.")
    exit(-1)

print("\n######################################")
print("For the deadline of your goal \"{}\" there are {} days remaining.".format(user_goal,days_till_deadline))
print("######################################")

