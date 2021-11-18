lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#All functions with list cause permanent changes

friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.index("Kevin") #If Kevin wasn't in the list, we would
#get an error
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.reverse()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)


