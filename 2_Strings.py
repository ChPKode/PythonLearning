
#tut8 -- Strings
"""String --

"""
my_Str = "The Future Kids"
print(my_Str)
print(my_Str[8]) #output : r ..... index starts with 0
print(my_Str[0:6]) #output : The Fu .....  index 6 is excluded
print(len(my_Str))  #len() length function

#IndexError : string out of range
""" print(my_Str[50])  # IndexError: string index out of range """

print(my_Str[0:50])  #Output :  The Future Kids. Here it prints the available index values and ignores other indexes

#slicing
print(my_Str[0:8:2]) #slicing with skiping every 2 element
print(my_Str[0::500]) #Extended slicing... solves which is available

#Reverse indexing or negative indexing
print(my_Str[-5:-1])

#String (functions) methods
print(my_Str.isalnum()) #Boolean output : False  as it is not alpha nueric
print(my_Str.isalpha()) #output : False as it is not alpha.. u can see spaces in string
print(my_Str.endswith("ids")) #True
print(my_Str.count("i"))  #Output 1
print(my_Str.capitalize())
print(my_Str.find("id"))
print(my_Str.lower())
print(my_Str.upper())  #THE FUTURE KIDS
print(my_Str.replace("Future", "Current"))   #The Current Kids

"""www.w3schools.com for more python methods
www.realpython.com INSERESTING learning path 
"""