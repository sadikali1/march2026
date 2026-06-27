# operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# 1. Arithmetic operators +, -, *, /, %, 
# 2. Comparison operators ==, !=, >, <, >=, <=
# 3. Logical operators and, or, not
# 4. Assignment operators =, +=, -=, *=, /=, %=
# 5. Identity operators is, is not
# 6. Membership operators in, not in


#1. Arithmetic operators +, -, *, /, %, ** (exponentiation), // (floor division)
a = 10
b = 3
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

#2. Comparison operators ==, !=, >, <, >=, <=
x = 5   
y = 10
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to

# 3. Logical operators and, or, not
a = 10
b = 20
c = 5
print("a > b and a > c:", a > b and a > c)  
# Logical AND # true and true = true, true and false = false, false and false = false
print("a > b or a > c:", a > b or a > c)   # Logical OR # true or true = true, true or false = true, false or false = false
print("not (a > b):", not (a > b))         # Logical NOT # not true = false, not false = true

marks = 85
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
else:
    print("Grade: D")



# 4. Assignment operators =, +=, -=, *=, /=, %=
x = 5
x += 3  # x = x + 3
print("x after += 3:", x)  # x is now 8
x -= 2  # x = x - 2
print("x after -= 2:", x)  # x is now 6
x *= 4  # x = x * 4
print("x after *= 4:", x)  # x is now 24
x /= 6  # x = x / 6
print("x after /= 6:", x)  # x is now 4.0
x %= 3  # x = x % 3
print("x after %= 3:", x)  # x is now 1.0   

# 5. Identity operators is, is not
a = [1, 2, 3]
b = a  # b references the same list as a
c = [1, 3]  # c is a different list with the same content
print("a, 2, is b:", a is b)  # True, because a and b reference
print("a is c:", a is c)  # False, because a and c reference different lists
print("a == c:", a == c)  # True, because a and c have the same content
# 6. Membership operators in, not in
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)  # True, because 3 is in the list
print("6 in my_list:", 6 in my_list)  # False, because 6 is not in the list
print("3 not in my_list:", 3 not in my_list)  # False, because 3 is in the list
print("6 not in my_list:", 6 not in my_list)  # True, because 6 is not in the list


# 6. Membership operators in, not in\
my_string = "Hello, World!"
print("'Hello' in my_string:", 'Hello' in my_string)  # True,
print("'Python' in my_string:", 'Python' in my_string)  # False
print("'Hello' not in my_string:", 'Hello' not in my_string)  # False
print("'Python' not in my_string:", 'Python' not in my_string)  # True
