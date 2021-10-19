"""
Menu:
1. Dogs details
2. Friends list
3. N Azzeret
"""

from random import randint
from time import sleep


def menu():
    while True:
        choice = input("Menu:\n----------------\n1. Dogs details\n2. Friends list\n3. N Azzeret\n")
        if choice == "1":
            dogs()
        elif choice == "2":
            friends()
        elif choice == "3":
            azzeret()
        else:
            print("select 1-3 only!\n")
            continue
        exit_menu = input("do you want to exit? y/n\n")
        if exit_menu == "y":
            break
        else:
            print("welcome back\n")
    print("Thank you and Bye Bye")


def dogs():
    name = input("enter dog's name: ")
    age = input("enter dog's age: ")
    print("\nDog's name is " + name + "\nDog's age is " + str((int(age)*7)) + "\n")


def friends():
    list_friends = []
    for i in range(5):
        list_friends.append(input("Please provide your friend's name: "))
    name = input("enter new name: ")
    if name in list_friends:
        print(name + " is inside the list")
    else:
        list_friends.append(name)

    print("\nyour friends list is " + str(list_friends))


def azzeret():
    summary = 1
    num = int(input("Enter a number: "))
    for i in range(1, num+1):
        summary = summary*i
    print(str(num) + " Azzeret is " + str(summary))












menu()
