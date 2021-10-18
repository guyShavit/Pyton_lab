from time import sleep
from random import randint

num1 = randint(1,37)
num2 = randint(1,37)
print("num1 is: " + str(num1) + "\nnum2 is: " + str(num2) + "\n")
if num1 == num2:
    print("the numbers match! you won 1,000,000$")
else:
    print("you didn't win this time\n")

fruits = ["banana","apple","mango"]
for i in range(len(fruits)):
    print(fruits[i])