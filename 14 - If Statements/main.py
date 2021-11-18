is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are not a male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are not tall but are male")
elif not(is_male) and is_tall:
    print("You are not male but are short")
else:
    print("You are either not male or nor tall or both")