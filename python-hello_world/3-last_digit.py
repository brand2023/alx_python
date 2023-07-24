import random
number = random.randint(-10000, 10000)
if number[4]>5:
    a="and is greater than 5"
elif number[4]==0:
    a="and is 0"
elif number[4]<6 and number[4]!=0:
    a="and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number,number[4],a))
