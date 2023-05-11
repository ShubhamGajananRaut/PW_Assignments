import random


exlist = [random.randint(0, 100) for _ in range(25)]


for num in exlist:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by 3")