
# The first thing I have to do is actually open that file from inside python so I can use a special command called
# open() inside parentheses I type in the name of the file I want to open and this is either
# going to be a relative path to the file, an absolute path to the file or just the file's name
# with both files are in the same directory. I have to put one more thing inside of this open function and it's going
# to be the mode that I want to open the file in which you could actually open files in a couple
# different modes and the first mode is called read, so we just put "r", that stands for "read", and this basically
# means that I only want to read the information inside the file, I don't want to modify it. Another mode is called
# "w", that stands for "write", and "write" basically mean that you can change the file, you can write new information,
# you can change existing information. There's an another one called "a" and it stands for append, and this basically
# mean you can append information onto the end of the file, so you can't modify any of the information in the file,
# you can't change any information, but you can add new information. And there's one more that is "r+", and this
# basically means read and write so this will give you all the power of reading and writing.
employee_file = open("employees.txt", "r")
# Generally we're going to want store this inside of a variable
# Whenever you open a file you want to make sure that you close the file as well
# Before we do anything else generally is a good idea to make sure that it's possible to read this file
# To do that, we use the readable function:
print(employee_file.readable())
print()
# If we change the second argument of open function to "w", the readable function will return False
# instead of True, because we can no longer read the file, we can only write to the file
# So once we figure out whether or not the file can be read from, let's actually read it.
print(employee_file.read())
print()
# The read function will spit out all the information in the file
# We could also read an individual line inside this file:
employee_file.close()
employee_file = open("employees.txt", "r")

print(employee_file.readline())
# The line above just read the first line, but this readline function basically move a little
# cursor onto the next line, so if we use the readline function one more time it will print the second line

print(employee_file.readline())
# That can be pretty useful for reading multiple lines in a file but there's actually another function that is
# better at doing that, the readlines function. What this is gonna do is it's going to take
# all of the lines inside of our file and put them inside a list:

print(employee_file.readlines())
# So if I want to access a specific line I can just refer to it by it's index in the list:

employee_file.close()
employee_file = open("employees.txt", "r")

print()
print(employee_file.readlines()[1])

employee_file.close()
employee_file = open("employees.txt", "r")

# We can also use this readlines function with a for loop:
for line in employee_file.readlines():
    print(line)

employee_file.close()
