phrase = "Giraffe Academy"
print(phrase)

print("Giraffe\n\"\Academy\"")

#Concatenation

print(phrase + " is cool")

#Functions: We can use functions to modify our strings and we can also
#use functions to get information about our strings.

print(phrase.lower())
print(phrase.upper())
print()

print(phrase.isupper())
print(phrase.upper().isupper())
print()

print(len(phrase))
print(phrase[0])
print(phrase.index("G"))
print(phrase.index("a"))
print(phrase.index("Acad"))
#If I put an character or phrase that doesn't exist inside index() it
#will throw an error
print()
print(phrase.replace("Giraffe", "Elephant"))
#Even the replace() is not a permanent change with strings
print(phrase)

