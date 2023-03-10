# Strings
name = "Lakshay,Rahul"
print(len(name)) # This is used to determine the length of a string
print(name[0:7]) # This is used to slice a string
print(name[:7]) # This is used to slice a string

print(name[:-4])
print(name[:len(name)-4]) # Both of them are same

print(name[-1:len(name)-14])
print(name[len(name)-1:len(name)-14]) # Both of them are same

# This will make a new string and make it upper/lower case but it don't change the existing string
print(name.upper()) # This will make all the alphabet in upper case
print(name.lower()) # This will make all the alphabet in lower case

a = "Laksahay !!!!!!!!!!!!! Laksahay"
print(a.rstrip("!")) # This will remove the ! from the right end only not from the begning
print(a.replace("Laksahay","Nikhil")) # This will replace all the occurance

print(a.split(" ")) # This will create new list with three elements
capitalise = "lakshay is my namE"
print(capitalise.capitalize()) # This will capitalise the first letter of the string and make other capital letter to lower case

str = "Hello,Myself Lakshay"
print(len(str))
print(str.center(50))
print(len(str.center(50)))

str2 = "This is an example!!!!"
print(str2.endswith("!!!"))

str2 = "This is an example!!!!"
print(str2.endswith("an",6,10))

st3 = "This is a python tutorial"
print(st3.find("is"))
print(st3.find("an")) # This will not throw any error
# print(st3.index("an")) # This will throw an error as it will check the index of the an word

str3 = "This is tutorial 5 of python"
print(str.isalnum()) # This will check if the string only contains letter(both upper and lower case) and the number from 0-9
print(str.isalpha()) # This will check if the string only contains letter(both upper and lower case)
print(str.islower())

str4 = "This is an string example because there is no lorem in the python"
print(str4.isprintable()) #This will check if all the character in the string are printable or not that means it will return false if there is \n or \t in the string

str5 = "  "
print(str5.isspace()) # If string only contains whitespaces it will return true otherwise false

str6 = "Why there is no lorem in python"
print(str6.istitle()) # This will check if every word in the string has capital letter in the begining
print(str6.startswith("Why"))

print(str6.swapcase()) # This will swap the uppercase to lowercase and vice-versa
print(str6.title())
