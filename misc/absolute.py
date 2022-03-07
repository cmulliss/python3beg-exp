# program to give absolute version of a number

from numpy import int16


myNumber = int(input("Enter a number: "))

if myNumber >= 0:
    print(myNumber)
elif myNumber < 0:
    print(f"Your number is {-myNumber} as an absolute number.")
