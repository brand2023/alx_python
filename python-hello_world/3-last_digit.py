import random
number = random.randint(-10000, 10000)
last_digit=abs(number)%10
if number<0:
    last_digit=-last_digit
if last_digit>5:
    a="and is greater than 5"
elif last_digit==0:
    a="and is 0"
else:
    a="and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number,last_digit,a))
