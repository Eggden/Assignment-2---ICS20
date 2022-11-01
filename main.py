from colorama import Fore, Back, Style
import math
print(Fore.WHITE + "Calculator: Your Helpful Calculator Here!")
PI = 3.14
r = float(input(Fore.BLUE + 'Insert A Circle Radius To Continue <NUMBERS ONLY> '))
area = PI*r*r
circumference = 2*PI*r
print(Fore.BLUE + "___________________")
print(Fore.RED + "Circle Area = %.2f" %area)
print("Circumference Of A Circle = %.2f" %circumference)
print(Fore.WHITE + "Available Calculator below")
print(Fore.BLUE + "___________________")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print(Fore.RED + "SELECT OPERATION ")
print(Fore.WHITE + "1.Addition")
print(Fore.BLUE + "2.Subtraction")
print(Fore.YELLOW + "3.Multiplication")
print(Fore.RED + "4.Division")

while True:
    choice = input(Fore.WHITE + "Enter Operation Number: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input(Fore.BLUE + "Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Would you like the calculate something else? (yes/no): ")
        if next_calculation == "no":
          print(Fore.WHITE + "Thank You For Using The Calculator!")
          break
        
    
    else:
        print(Fore.RED + "Try Again")