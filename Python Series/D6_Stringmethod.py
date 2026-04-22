# Day 6 - String Methods 
# In this file we will learn about string methods in Python. String methods are built-in functions that can be used to perform various operations on strings. Some common string methods include upper(), lower(), strip(), replace(), and split(). The upper() method converts all characters in a string to uppercase, while the lower() method converts all characters to lowercase. The strip() method removes any leading or trailing whitespace from a string, and the replace() method replaces a specified substring with another substring. The split() method splits a string into a list of substrings based on a specified delimiter. Let's explore these string methods in more detail!


#Remove spaces

text1 = "   Hello, World!   "
# Using the strip() method to remove leading and trailing whitespace
print("Original text:", text1)  # Using repr() to show the original text with whitespace
print("removed spaces:",text1.strip())  # This will print 'Hello, World!' without the leading and trailing spaces. The strip() method removes any whitespace characters from the beginning and end of the string, but it does not remove whitespace from the middle of the string.


#convert to capital letters
text2 = "hello, world!"
# Using the upper() method to convert all characters to uppercase
print("Original text:", text2)
print("Uppercase text:", text2.upper())  # This will print 'HELLO, WORLD!' with all characters converted to uppercase. The upper() method does not modify the original string; it returns a new string with the changes applied.

#we can also add .strip() for removing spaces. example: text2.upper().strip() will first convert the string to uppercase and then remove any leading or trailing whitespace from the resulting string.
#convert to proper case letters
text3 = "hello, world!"
print("Original text:", text3)
print("Proper case text:", text3.title())  # This will print 'Hello, World!' with the first letter of each word capitalized. The title() method converts the first character of each word to uppercase and the remaining characters to lowercase. Like other string methods, it returns a new string and does not modify the original string.


#Replace text

text4 = "Hello, World!"
# Using the replace() method to replace 'World' with 'Gaurav'

print("Replaced text:", text4.replace("World","Gaurav"))  # This will print 'Hello, Gaurav!' by replacing the substring 'World' with 'Gaurav'. The replace() method takes two arguments: the substring to be replaced and the substring to replace it with. It returns a new string with the replacements made, and does not modify the original string.


#count occurences of a character in a string

text5 = "Hello, World!"
# Using the count() method to count the occurrences of 'o'  

print("Count of 'o':", text5.count('o'))  # This will print the number of times the character 'o' appears in the string, which is 2. The count() method takes a single argument, which is the substring to be counted, and returns the number of occurrences of that substring in the string.


#check if text starts with something

text6 = "Hello, World!"
# Using the startswith() method to check if the string starts with 'Hello'
print("Starts with 'Hello':", text6.startswith('Hello'))  # This will print True if the string starts with 'Hello', and False otherwise. The startswith() method takes a single argument, which is the substring to check for at the beginning of the string, and returns a boolean value indicating whether the string starts with that substring or not.


#check if only numbers are present in the string

text7 = "12345"
# Using the isdigit() method to check if the string contains only digits
print("Contains only numeric:", text7.isnumeric())  # This will print True if the string contains only digits, and False otherwise. The isdigit() method returns a boolean value indicating whether all characters in the string are digits (0-9) and there is at least one character in the string. If the string contains any non-digit characters or is empty, it will return False.



