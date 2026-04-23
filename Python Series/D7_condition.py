# Day 7: Logical Conditions
# In this file, we will learn about logical conditions in Python. Logical conditions are used to make decisions in our code based on certain criteria. We can use logical operators such as and, or, and not to combine multiple conditions. The if statement is used to execute a block of code if a specified condition is true. We can also use elif (short for else if) to check multiple conditions and else to execute a block of code if none of the previous conditions are true. Let's explore how to use logical conditions in Python!    
# Example of using if, elif, and else statements

age = int(input("Enter Your Number"))

if age>=18:
    print("You are an adult.")
else:
    print("You are a minor.")


    #Discount checker
amount = 2000

if amount >= 1000:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")


    # if-elif-else example for grading system(multiple conditions)
marks = int(input("Enter Your Marks: "))  
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")



# sales performance(Data Analyst use case

sales = 65000
if sales >= 100000:
    print("High performance!")
elif sales >= 50000:
    print("Medium performance!")
else:
    print("Low performance!")



#string coparision

city = "New York" 
if city == "new York":       # The condition checks if the value of the variable city is equal to the string "new York". However, since the comparison is case-sensitive, "New York" and "new York" are considered different strings. Therefore, the condition will evaluate to False, and the else block will be executed, printing "city not matched!" to the console. If we want to make the comparison case-insensitive, we can convert both strings to lowercase (or uppercase) before comparing them, like this: if city.lower() == "new york".
    print("city matched!")
else:
    print("city not matched!")


#Password program
password = input("Enter your password: ")

if password == "admin123":
    print("login successful!")
else:
    print("Invalid password.")



# Email validation program
email = "user@example.com"
if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")


#Advanced : Missing Data check

value ="sdf"
if value is None or value == "":
    print("Data is missing.")
else:
    print("Data is available.")