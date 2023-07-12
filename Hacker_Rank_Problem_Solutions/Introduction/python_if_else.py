num = input('')
num = int(num)
if (num % 2 != 0) or (num % 2 == 0 and 6 <= num <= 20):
    print("Weird")
elif (num % 2 == 0 and 2 <= num <= 5) or (num % 2 == 0 and num > 20):
    print('Not Weird')

