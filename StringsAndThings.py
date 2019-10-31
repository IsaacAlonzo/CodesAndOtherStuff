# Strings
#       data that falls within" "

# Concatenation
# Put 2 or more strings together

firstname = "Billy"
lastname = "Bobby"

fullname = firstname + " " + lastname

print(fullname)

# Repetition
# repetition operator: *

print("Hip "*2 + "Hooray")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "John W. Cena"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#     slicing operator:   :
#     slicing lets us make substrings

print(name[0:4])
print(name[:7])
print(name[4:9])
print(name[5:])

for i in range(1, len(name)+1):
    print(name[0:i])

# Searching inside of Strings

print("john" in name)
print("w" not in name)

if "o" in name:
    print("The letter o is in name")
else:
    print("The letter o is not in name")

# String Methods to investigate:
# Method        Use Example         Explanation
# center        aStr.center(w)      it centers the string out how many vales you want it
print(name.center(15))
print(name.center(30))
# ljust         aStr.ljust(w)       it creates a space of how many spaces away from your string
x = name.ljust(21)
print(x, "is awesome")
y = name.ljust(40)
print(y, "is a dude")
# rjust         aStr.rjust(w)       it moved my string to the left to combine with my other string and
# realigned my string to the right 20 spaces
x = name.rjust(21)
print(x, "is cash money")
x = name.rjust(15)
print(x, "is cool")
# upper         aStr.upper()        makes everything uppercase within the string
print(name.upper())
x = "is a wrestler"
print(x.upper())
# lower         aStr.lower()        makes everything in the string lower case
print(name.lower())
x = "part of the WWE"
print(x.lower())
# index         aStr.index(item)    tells you where your the searched (w) is and gives you its location
print(name.index("Cena"))
print(name.index("John"))
# rindex        aStr.rindex(item)   also tells the same thing as index just another way of typing it
print(name.rindex("W."))
print(name.rindex("Cena"))
# find          aStr.find(item)     tells you where your the searched character(s) start
print(name.find('John'))
print(name.find("Cena"))
# rfind         aStr.rfind(item)    also finds the character(s) you want and returns location
print(name.rfind('e'
                 'na'))
print(name.rfind("W."))
# replace       aStr.replace(old, new)
x = name.replace("Cena", "Stamos")
print(x)
y = name. replace("John", "Juan")
print(y)

# Be sure to include multiple examples of all of them in use

# Character functions

print(ord('B'))

print(chr(97+13))

print(str(12548))

# testing functions from mapper.py

from mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

from crypto import *

print(scramble2Encrypt("GOOD MORNING LADIES AND GENTLEMEN"))

print(scramble2Decrypt("ODMRIGLDE N ETEEGO ONN AISADGNLMN"))

print(caesarEncrypt("Hello", 2))

print(caesarDecrypt("Jgnnq", 2))