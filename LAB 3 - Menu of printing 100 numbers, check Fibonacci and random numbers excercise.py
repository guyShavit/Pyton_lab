"""
Menu:
1. print 100 numbers
2. check if a series of numbers in a list is Fibonacci
3. randint numbers until we get 12 or we count 10 times

"""
from random import randint
from random import seed
while True:
    choice = input("Menu\n------------\n1. Print 100 random numbers\n2. check Fibonacci list\n3. randint numbers until we get 12 or counter == 10:\n")
    if choice == "1":
        for i in range(1,101):
            print(str(i))
    elif choice == "2":
        while True:
            fibo = []
            fibo.append(int(input("enter a number to the list: ")))
            fibo.append(int(input("enter a number to the list: ")))
            fibo.append(int(input("enter a number to the list: ")))
            addMore = input("\ndo you want to add more numbers? y/n ")
            while True:
                if addMore == "y":
                    fibo.append(int(input("\nenter a number to the list: ")))
                    addMore = input("\ndo you want to add more numbers? y/n ")
                    if addMore == "y":
                        continue
                    elif addMore == "n":
                        break
                if addMore == "n":
                    break
            if addMore == "n":
                print("thank you for the list!")
                break

        print("your list is " + str(fibo) + "\n")

        isFibo = True
        for i in range(2, len(fibo)):
            if fibo[i] == fibo[i - 1] + fibo[i - 2]:
                continue
            else:
                isFibo = False
                break
        if isFibo:
            print("the list is in Fibonacci order!\n")
        else:
            print("The list is not in Fibonacci order\n")
    elif choice == "3":
        counter = 0
        cube = randint(1, 12)
        while cube != 12 and counter < 10:
            cube = randint(1, 12)
            counter += 1
            print("cube is " + str(cube) + "\nthe counter is " + str(counter) + "\n")
            if cube == 12 and counter != 0:
                print("\nyou hit 12! Well done!\n")
                break
            else:
                continue
        if counter == 0 and cube == 12:
            print("\nyou hit 12!\n")
        elif counter != 0 and cube != 12:
            print("\nyou didn't make it this time\n")

    else:
        print("Please enter 1-3 only!")
    exitProgram = input("\nDo you want to exit? y/n: ")
    if exitProgram == "y":
        print("\nThank you and Bye Bye")
        break
    elif exitProgram == "n":
        print("\nWelcome back!\n")
        continue
