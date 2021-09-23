# This task is to get as an input list, calculate the cost and print the total amount as an integer.
print("Now we will calculate the price of your groceries list:\n\nPrices:\n----------\nTomato= 3 NIS\nCucumber = 2 NIS\nCola= 5 NIS\nChicken=20 NIS per KG\n")

tomato = input("Please enter how many tomatoes do you want: ")
cucumber = input("Please enter how many cucumbers do you want: ")
cola = input("Please enter how many Coca Cola do you want: ")
chicken = input("Please enter the weight of chicken you want: ")

print("\nYour order summary is:\n--------------\nTomatoes: " +str(tomato) + "\nCucumbers: " + str(cucumber) + "\nColas: " + str(cola) + "\nChicken: " + str(chicken) + " KG")

summary = (tomato * 3) + (cucumber * 2) + (cola * 5) + (chicken * 20)
