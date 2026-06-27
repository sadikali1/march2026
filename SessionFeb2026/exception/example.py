
i = 0
'''
try:
    result = 10 / i
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


'''
a = input("Enter a number: ")
try:
    num = int(a)
    num1 = 10 / num
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except NotImplementedError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always execute.")
print("Program continues after handling the exception.")