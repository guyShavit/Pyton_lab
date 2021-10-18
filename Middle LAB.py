import os
# prints current date and time
from datetime import datetime

now = datetime.now()
date = now.date()
print(str(date) + " " + now.strftime("%H:%M:%S"))

# Accept full name and print in reversed order with space between the letters
print("\n------------------------------\n")
firstName = input("enter your first name: ")
lastName = input("enter your last name: ")
print(' '.join(firstName[::-1]) + " " + ' '.join(lastName[::-1]))

# input a filename with extension and print only the extension

fileName = input("please provide a filename with extension: ")
list_extension = fileName.split(".")
print("the extension of your file is " + str(list_extension[-1]))

# input an integer (n) and compute the value of n+nn+nnn

num = input("enter an integer: ")
num1 = int(num + num)
num2 = int(num + num + num)
print(int(num) + num1 + num2)

# input a number from user and check if it is even or odd

num = int(input("please enter a number: "))
if num % 2 == 0 and num != 0:
    print("your number is even")
elif num == 0:
    print("your number is zero")
else:
    print("your number is odd")

# sum all the values in existing list

list1 = [1, 4, 26, 333, 4, 88]
sum1 = 0
for i in range(len(list1)):
    sum1 = sum1 + list1[i]
print("the sum of the items in the list is " + str(sum1))


