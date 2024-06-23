import random

string = input()
length = len(string)
str_list = list(string)

for i in range(length // 3 + 1):
    rand = random.randint(0, length - 1)
    str_list[rand] = str_list[rand].upper()

string = ''.join(str_list)
print(string)