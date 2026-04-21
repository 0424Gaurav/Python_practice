#Day-5 of learning python:- Conditional Statements in Python
# In this file we will learn about conditional statements in Python. Conditional statements are used to perform different actions based on different conditions. The most common conditional statements in Python are if, elif, and else. The if statement is used to test a condition and execute a block of code if the condition is true. The elif statement is used to test multiple conditions and execute a block of code if any of the conditions are true. The else statement is used to execute a block of code if all the conditions are false. Let's get started with conditional statements in Python!


#string Indexing 

name = "Gaurav"
#print(name )
print(name[0])  # This will print the first character of the string, which is 'G'.
print(name[5])  # This will print the second character of the string, which is 'a'.
print(name[-4])  # This will print the last character of the string, which is 'v'.


#String Slicing
# String slicing is a technique used to extract a portion of a string. It allows us to create a new string by selecting a range of characters from the original string. The syntax for string slicing is as follows: 
# syntax: string[start:end]

name = "Gaurav Yadav"
print(name[-6:-1])  # This will print the characters from index -4 to index -1, which is 'Yad'.
print(name[0:6])  # This will print the characters from index 0 to


#Extracting charcters from middle 
Text ="DataAnalysis"
print("Middle slice : ", Text[4:12])  # This will print the characters from index 4 to index 11, which is 'Analysis'. The character at index 12 is not included in the output because the end index in string slicing is exclusive.

#Extract till End 
print("till end:", Text[4:12])  # This will print the characters from index 4 to the end of the string, which is 'Analysis'.

#Extract from start
print("from start:", Text[0:4])  # This will print the characters from the start of the string to index 3, which is 'Data'.

#Extract Last 5 characters
print("last 5 characters:", Text[-5:])  

#skip text "DataAnalysis"
print("skip text:", Text[0:10:2])  # This will print every second character from index 0 to index 11, which is 'DtAslyi'. The third parameter in string slicing is the step, which determines how many characters to skip between each character in the output. In this case, it is set to 2, so every second character is included in the output.
print("Reverse:", Text[4::-1])  # This will print the characters of the string in reverse order, which is 'sisylanAataD'. The step parameter is set to -1, which means that the characters will be selected in reverse order.

