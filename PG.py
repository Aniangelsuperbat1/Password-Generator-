import random

capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower = capital.lower()

nums = "0123456789"

special = "!@#$%^&*()-+<>?/"

uppercase, lowercase, numbers, SP = True, True, True, True

all = ""

if uppercase:
    all += capital
if lowercase:
    all += lower
if numbers:
    all += nums
if SP:
    all += special

length = 15

for i in range(10):
    password = "".join(random.sample(all, length))
    print(password)
