import random
number = random.randint(-10000, 10000)
n=str(number)
b=int(n)
if b>5:
    a="and is greater than 5"
elif b==0:
    a="and is 0"
elif b and b!=0:
    a="and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number,b,a))
