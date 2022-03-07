# create simple calculator

# addition

print("Choose a menu option: ")
menuOption = input(
    "+  add \n - subtract  \n * multiply  \n / divide \n power ** \n modulo // \n"
)

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))

if menuOption == "+":
    print(firstNumber + secondNumber)
elif menuOption == "-":
    print(firstNumber - secondNumber)
elif menuOption == "*":
    print(firstNumber * secondNumber)
elif menuOption == "**":
    print(firstNumber ** secondNumber)
elif menuOption == "//":
    print(firstNumber // secondNumber)
elif menuOption == "/":
    if secondNumber > 0:
        print(firstNumber / secondNumber)
    elif secondNumber == 0:
        print("Sorry, cannot divide by zero as gives infinity!")
