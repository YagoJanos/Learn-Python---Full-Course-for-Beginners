def cube(num):
    return pow(num, 3)
    print("It will be ignored because it is after return")

print(cube(3))

#Notice that return is not print, and to print a return we have
#to pass it to print's parentheses

result = cube(4)
# This variable is going to store the value that gets returned
# from the cube function
print(result)