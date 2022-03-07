firstName = "Cherry"
lastName = "Mulliss"

fullName = firstName + " " + lastName

print(fullName)

print(f"My name is {fullName}")

longString = """This is a very long string
that I wrote to help somebody
who had a question about
writing long strings in Python"""
print(longString)

# fourth character
print(longString[3])

# last element
print(longString[-1])

# everything up to but not including 4th character
print(firstName[:3])

# excluding last 2 chars
print(firstName[:-2])

# position 1 to 3
print(firstName[1:3])

# exercise
link = "https://domain.py"
first = link[0:5]

if first == ("https"):

    print("the link starts with", first)
