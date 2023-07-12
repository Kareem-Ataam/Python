num = int(input())
text = input()
num_lst = list()
l = text.split()
for i in l:
    i = int(i)
    num_lst.append(i)
num_lst.sort()
temp = num_lst[len(num_lst)-1]

i = -2
while i >= -len(num_lst):
    if num_lst[i] < temp:
        print(num_lst[i])
        break
    i -= 1


