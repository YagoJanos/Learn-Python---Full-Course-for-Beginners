def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# We use == to see if the two values are equal
# and != to see if they are different
print(max_num(300,4,5))