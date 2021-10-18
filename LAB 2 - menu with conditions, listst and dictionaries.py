from time import sleep

choice = input("Menu\n1. Insert a number and ** in 3\n2. insert 4 IPs into list and print it\n3. Insert 4 entries to DNS_Dictionary and print it\n4. Check if a string is polindrom\n")
if choice == "1":
    number = int(input("enter a number:\n"))
    print(number**3)
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
        print("this is polindrom")
    else:
        print("this is not polindrom")
else:
    print("select 1-4 only!")

