# Day 4: Operators in Python
# In this file we will learn about operators in Python.
# Operators are special symbols that perform specific operations on operands (variables and values). They are used to manipulate data and perform various calculations. In Python, there are several types of operators, including:
# 1. Arithmetic Operators: These operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
# 2. Comparison Operators: These operators are used to compare two values and return a boolean  
#    result (True or False). They include operators like equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).
# 3. Logical Operators: These operators are used to combine conditional statements and return a boolean
#    result. They include operators like and, or, and not.
# 4. Assignment Operators: These operators are used to assign values to variables. They include operators like =, +=, -=, *=, /=, %=, **=, and //=.
# 5. Bitwise Operators: These operators are used to perform bitwise operations on binary numbers. They include operators like &, |, ^, ~, <<, and >>.
# 6. Identity Operators: These operators are used to compare the memory locations of two objects. They include operators like is and is not.
# 7. Membership Operators: These operators are used to test whether a value is present in a sequence (like a list, tuple, or string). They include operators like in and not in.    


#let's try example one by one for each type of operator.
#1. Arithmetic Operators

num1 = 10
num2 = 5

print("num1 + num2 =", num1 + num2)  # Addition
print("num1 - num2 =", num1 - num2)  # Subtraction
print("num1 * num2 =", num1 * num2)  # Multiplication


# Assignment Operators                                                                  
value = 10  # This is an assignment operator. It assigns the value 10 to the variable x.

print("value =", value)  # This will print the value of the variable x, which is 10.
value += 5  # This is an augmented assignment operator. It adds 5 to the current value of x and assigns the result back to x.
print("value =", value)  # This will print the updated value of the variable x, which is 15.
value-= 3  # This is another augmented assignment operator. It subtracts 3 from the current value of x and assigns the result back to x.
print("value =", value)  # This will print the updated value of the variable x, which is 12.


# 3. Comparison Operators
p1 = 18
p2 = 18
print(p1 == p2)  # less than or equal to operator. It checks if p1 is equal to p2 and returns True if they are equal, otherwise it returns False. In this case, it will return True because both p1 and p2 have the same value of 18.

p3 = 20
p4 = 15
print(p3 > p4)  # greater than operator. It checks if p3 is greater than p4 and returns True if it is, otherwise it returns False. In this case, it will return True because 20 is greater than 15.


# 4. Logical Operators
x1 = 5
x2 = 15
x3 = 25
x4 = 40

print("And result :", x1 < x2 and x3 < x4)  # A nd operator. It checks if both conditions are True and returns True if they are, otherwise it returns False. In this case, it will return True because 5 is less than 15 and 25 is less than 40.
print("Or result :", x1 < x2 or x3 > x4)  # Or operator. It checks if at least one of the conditions is True and returns True if it is, otherwise it returns False. In this case, it will return True because 5 is less than 15, even though 25 is not greater than 40.
print("Not result :", not(x1 < x2))  # Not operator. It negates the condition and returns True if the condition is False, and False if the condition is True. In this case, it will return False because 5 is less than 15, so the condition is True, and the not operator negates it to False.



#5. Identity Operators

m1 = 100
m2 = 100
print(m1 is m2)  # Is operator. It checks if m1 and m2 refer to the same object in memory and returns True if they do, otherwise it returns False. In this case, it may return True because small integers are cached by Python, but it is not guaranteed for larger integers or other data types.  



#6. Membership Operators

print("check 'P' in 'Python' :", 'P' in 'Python')  # In operator. It checks if the value 'P' is present in the string 'Python' and returns True if it is, otherwise it returns False. In this case, it will return True because 'P' is present in 'Python'.
print("check 'z' in 'Python' :", 'z' in 'Python')  # This will return False because 'z' is not present in 'Python'.
print("check 'a' not in 'Python' :", 'a' not in 'Python')  # Not in operator. It checks if the value 'a' is not present in the string 'Python' and returns True if it is not, otherwise it returns False. In this case, it will return True because 'a' is not present in 'Python'.