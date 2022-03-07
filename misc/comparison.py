a = int(input("enter a number: "))
b = int(input("enter another number: "))

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a is equal to b")
print("That's it!")

# indentation matters
# if not using int, will compare ascii codes for the numbers instead
