#Day 3 - Data Types in Python
#In this file we will learn about data types in Python.
#Data types are the classification of data items. They represent the kind of value that tells what
#operations can be performed on the data. In Python, there are several built-in data types, including:

# learn about 7 data types in Python
#1. text data types - str (string)

customer_name = "Gaurav"  #This is a string data type. It is used to represent text data. Strings are enclosed in either single quotes (' ') or double quotes (" ").
print ("customer name is : ", customer_name)
print("customer Datatype is : ", type( customer_name))  #The type() function is used to determine the data type of a variable. In this case, it will return <class 'str'>, indicating that customer_name is a string data type.





# 2. numeric data types - int (integer), float (floating-point number), complex (complex number)
 
rating = 5
order_quantity = 3

print("rating data type is :", type (rating))  #This will return <class 'int'>, indicating that rating is an integer data type.
print("order quantity data type is :", type (order_quantity))  #This will return <class 'int'>, indicating that order_quantity is an integer data type.



#3. float data type ; decimal numbers
 

order_amount = 1250.0

print("order amount data type is :", type (order_amount))  #This will return <class 'float'>, indicating that order_amount is a float data type.




#4. complex data type ; used to represent complex numbers, which have a real part and an imaginary part.
a=3+4j

print( type (a))  #This will return <class 'complex'>, indicating that a is a complex data type. The real part of the complex number is 3, and the imaginary part is 4j.



#5. boolean data type - bool (boolean)
is_paid = True

print("is paid",type(is_paid))  #This will return <class 'bool'>, indicating that is_paid is a boolean data type. The value True represents a true condition, while False represents a false condition.



#6. sequence data types - list, tuple, range
#Lists are ordered, mutable collections of items. They are defined using square brackets [] and can contain elements of different data types.
cities = ["pune", "Delhi", "Mumbai"]  # This is a list data type. Lists are ordered, mutable collections of items.
print(cities)

print(type (cities))  #This will return <class 'list'>, indicating that cities is a list data type.



#Tuples are ordered, immutable collections of items. They are defined using parentheses () and can also contain elements of different data types.
dimension = (10, 20, 30)  # This is a tuple data type. Tuples are ordered, immutable collections of items.
print(dimension)
print(type (dimension))  #This will return <class 'tuple'>, indicating that dimension is a tuple data type.




#Ranges are used to represent a sequence of numbers. They are defined using the range() function and can be used in loops or to generate a sequence of numbers.
num = range(1,11)  # This will create a range object representing numbers from 0 to 4.

print(list(num))  #This will convert the range object to a list and print it, resulting in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
print(type (num))  #This will return <class 'range'>, indicating that num


#dictionary data type - dict (dictionary)
#Dictionaries are unordered, mutable collections of key-value pairs. They are defined using curly braces
# {} and consist of keys and values. Each key is separated from its value by a colon (:), and items are separated by commas.
student = {"name": "Gaurav", "age": 21, "grade": "A"}  # This is a dictionary data type. Dictionaries are unordered, mutable collections of key-value pairs.
print(student)
print(type (student))  #This will return <class 'dict'>, indicating that student is a dictionary data type. The keys in the dictionary are "name", "age", and "grade", and their corresponding values are "Gaurav", 21, and "A".




#set data type - set (set)
#Sets are unordered, mutable collections of unique items. They are defined using curly braces {} or
#the set() function. Sets do not allow duplicate values and are commonly used for operations like union, intersection, and difference.
numbers = {1, 2, 2, 3, 4, 5}  # This will create a set with the unique values {1, 2, 3, 4, 5}, as sets do not allow duplicate values.

print(numbers)
print(type (numbers))  #This will return <class 'set'>, indicating that value is a set data type.




#None data type - NoneType
#The None data type represents the absence of a value or a null value. It is often used to indicate that a variable has no value or to represent the absence of a return value from a function.

remark = None  # This is a None data type. It represents the absence of a value.
print(remark,type(remark))  #This will print None and <class 'NoneType'>, indicating that remark is a None data type. The value None indicates that remark has no value assigned to it.