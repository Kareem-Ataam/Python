"""
List summation script
Input:
    -- Number of list elements
    -- Elements of the list
Output:
    -- Summation of the list elements
"""
#Function that performs the summation
def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

numbers = list()

# Take the number of elements from the user
while True:
    try:
        num_of_list_elements = int(input("How many elements in the list: "))
        break
    except:
        ValueError
        print("Number of elements must be an integer")

i = 0

# Take the elements from the user
while i < num_of_list_elements:
    while True:
        list_num = input(f"Enter element number {i+1}: ")
        try:
            list_num = float(list_num)
            break
        except:
            ValueError
            print("Number are only allowed!!")
    numbers.append(list_num)
    i += 1
# Printing the result
print(f"The sum of the list elements is {sum_list(numbers)}")