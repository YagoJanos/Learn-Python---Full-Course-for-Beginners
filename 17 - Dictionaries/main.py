
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Mar"])
# or
print(monthConversions.get("Dec"))

# We can create a default value for the case
# the key isn't in the dictionary
print(monthConversions.get("Luv", "Not a valid Key"))
# We can also use numbers as keys, as long as they
# continue being unique
