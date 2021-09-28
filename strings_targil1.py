"""
Create 2 variables:
string with my name
string with my email
integer with my age

objectives:
1. print all of them to the screen in a nice way
2. print my name backwards
3. print my age*3
4. check if my full name is stored inside this full string:
    "idan ben yuval shimon yael gal adam shahar yana"
"""

name = "guy shavit"
email = "guy@gmail.com"
age = 39
names = "idan ben yuval shimon yael gal adam shahar yana"

print("\nmy name: " + name + "\nMy email: " + email + "\nMy age: " + str(age) + "\n")
print(name[::-1] + " " + str(age*3))

print(name in names)
