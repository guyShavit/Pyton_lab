from time import sleep
while True:
    choice = input("Menu\n1. Insert a number and ** in 3\n2. insert 4 IPs into list and print it\n3. Insert 4 entries to DNS_Dictionary and print it\n4. Check if a string is polindrom\n")
    if choice == "1":
        number = int(input("enter a number:\n"))
        print("your number powered in 3 is " + str(number**3) + "\n")
    elif choice == "2":
        list_ip=[]
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        print("the new list is:\n----------------\n" + str(list_ip))
    elif choice == "3":
        DNS_Dictionary = {}
        DNS_Dictionary.update({input("enter URL: "): input("enter IP: ")})
        DNS_Dictionary.update({input("enter URL: "): input("enter IP: ")})
        DNS_Dictionary.update({input("enter URL: "): input("enter IP: ")})
        DNS_Dictionary.update({input("enter URL: "): input("enter IP: ")})
        print("the new dictionary is\n------------------\n" + str(DNS_Dictionary))
    elif choice == "4":
        word = input("enter a word: ")
        if word == word[::-1]:
            print("this is polindrom\n")
        else:
            print("this is not polindrom\n")
    else:
        print("select 1-4 only!\n")
    while True:
        exitMenu = input("Do you want to return to menu? y/n: ")
        if exitMenu == "y":
            print("\nwelcome back!\n")
            break
        elif exitMenu == "n":
            break
        else:
            print("please enter y/n only!\n")
    if exitMenu == "y":
        continue
    else:
        print("\nThank you and Bye Bye!")
        break








