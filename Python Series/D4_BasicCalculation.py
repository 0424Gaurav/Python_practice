# Day 4: python input ,type Casting and Basic Calculation
# In this file we will learn about basic calculations in Python. We will also learn about type  casting, which is the process of converting one data type to another. This is useful when we want to perform operations on different types of data. For example, if we want to add a string and an integer, we need to convert the integer to a string first. We will also learn about the input function, which allows us to take user input in Python. The input function takes a string as an argument and returns the user input as a string. We can then use type casting to convert the user input to the desired data type for our calculations. Let's get started with basic calculations in Python!  

#Input and Type Casting
# The input function is used to take user input in Python. It takes a string as an argument and returns the user input as a string. We can then use type casting to convert the user input to the desired data type for our calculations. For example, if we want to take two numbers as input from the user and add them together, we can do it like this:

#name=input ("Enter the name:")
#print("Welcome", name )

#age= input("Enter your age: ")
#age=int(age)  # This will convert the age variable from a string to an integer using the int() function. Now we can perform calculations with the age variable as an integer.
#print(type(age))  # This will print the type of the variable age, which is <class 'str'> because the input function returns a string.
#age=age+5  # This will cause an error because we cannot add an integer (5) to a string (age). We need to convert the age variable to an integer first before we can perform the addition.
#print("Your age is", age)


#tempertaure =float (input ("Enter today's temperature: "))  # This will take the user input for temperature and convert it to a float using the float() function. Now we can perform calculations with the temperature variable as a float.

#print(type(tempertaure))  # This will print the type of the variable temperature, which is <class 'str'> because the input function returns a string.



#convert number to string
#sales = 5000
#text = "total sales: " + str(sales)  # This will convert the sales variable from an integer to a string using the str() function. Now we can concatenate the text variable with the sales variable as a string.
#print(text)  # This will print the text variable, which is "total sales:


#Total sales Calculator 
product = input ("product name :")
quality = int(input("Enter quality sold :"))
price_per_unit= float (input ("Enter price per unit :"))

total_sales = quality * price_per_unit  # This will calculate the total sales by multiplying the quality variable (which is an integer) with the price_per_unit variable (which is a float). The result will be stored in the total_sales variable.

print("___________________")
print("product :", product)  # This will print the product variable, which is the name of the product entered by the user.
print("total sales :", total_sales)  # This will print the total_sales variable, which is the result of the calculation for total sales. It will be a float value representing the total sales amount for the product based on the quantity sold and the price per unit.



