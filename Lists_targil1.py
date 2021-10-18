'''
create a list with 4 details about you: name, age, mail and phone number and print all details to the screen.
Then create another list with 2 IPs, add 3 more IPs, pop the 3rd IP annd print how many IPs do we have and print them.
'''

list = ["guy shavit", 39, "guy@gmail.com", "0541234567"]
list2 = ["192.168.1.2","193.168.2.1"]
print("\nMy name: " + list[0] + "\nMy age: " + str(list[1]) + "\nMy mails: " + list[2] + "\nMy phone number: " + list[3] + "\n")
print("the IPs in the list are " + list2[0] + " and " + list2[1])
print("\nadding another ips to the list")
list2.append("3.3.3.3")
list2.append("4.4.4.4")
list2.append("5.5.5.5")
print(list2)
print("\n removing the 3rd IP from the list")
list2.pop(2)
print("\nthe new IP list is\n" + str(list2) + "\n")
print("the IP list length is " + str(len(list2)))




