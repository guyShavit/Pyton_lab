# the program checks if a list is in fibonacci order or not

while True:
    fibo = []
    fibo.append(int(input("enter a number to the list: ")))
    fibo.append(int(input("enter a number to the list: ")))
    fibo.append(int(input("enter a number to the list: ")))
    addMore = input("do you want to add more numbers? y/n ")
    while True:
        if addMore == "y":
            fibo.append(int(input("enter a number to the list: ")))
            addMore = input("do you want to add more numbers? y/n ")
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
for i in range(2,len(fibo)):
    if fibo[i] == fibo[i-1] + fibo[i-2]:
        continue
    else:
        isFibo = False
        break
if isFibo:
    print("the list is in Fibonacci order!\n")
else:
    print("The list is not in Fibonacci order\n")

print("Thank you and Bye Bye!")












