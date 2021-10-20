"""
file handling permissions:
"r" only read from file
"w" only write to file (overwrites)
"a" only adding to file(not overwrites, adding to the file)
"r+" read and write
"a+" read and append
"x" creates a file
"""


#file = open("hello.txt", "x")
#file.close()

file = open("hello.txt", "a+")
file.write("192.168.1.2\n192.168.3.1")
print(file.read())
file.close()

file = open("hello.txt", "r")
print((file.readlines()[0]))  # prints the first line in the file

