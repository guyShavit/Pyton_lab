'''
Create a dictionary with 5 names & money
Then sum the money of the first and last names and pront it to the screen.
then, add a new name with sum of the money you calculated before.
At the end, print the number of entries and check if "Guy" is inside.
'''

dict1 = {"guy":10,"nadav":20,"yaron":30,"aharon":40,"ehud":50}
sum = dict1["guy"] + dict1["ehud"]
print("the sum of guy and ehud is " + str(sum))
dict1.update({"yoel": sum})
print(dict1)
print("the number of entries in the dictionary: " + str(len(dict1)))
print("guy" in dict1)
