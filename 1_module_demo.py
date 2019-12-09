#Day01
#import modules, using someone's well return code.
import random #syntax
#tut6
print("Dear S!!!!")
#ctrl+shft+f10  to run program

#comments ,print statement & escape sequence
"""comments = single line #
            multiple line <""" """> """
print("print statement by  default includes new line ")
print("We will try to add next print statement output to this line using 'end='. ", end="")
print("This is second line.")

#using COMMA between two different strings in print statement. In output we get SPACE between two strings
print("First string","Second string")

#escape characters -- \ (backward slash).   \n, \t, \'', \"", etc
print("c:\\narrayfolder")

#computers just do mathematical calculation gives output




#tut 7
"""
Variables -- container holding a value (data type). Name given to a memory address. Adv - 
Variable - can hold different type of data type value. We can use type() to check the variable data type.
Different types of variables have different type of operations.
"""
var1 = "String1"
var2 = 4
var3 = 5.1

print(var2+var3)  #output 9.1
#print(var3 + var1) #TypeError: unsupported operand type(s) for +: 'float' and 'str'
var4 = "4"
print(type(var4))
print(var1+var4) #Output : String14    "Concatenation of two strings"
print(5*var1) #output: String1String1String1String1String1  "Strings prints multiple times"



"""Type casting : change data type 

str(), int(), float()
"""
print(int(var4)+var2) #Output : 8
print(100*str(int(var4)+var2)) #Output : 8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888




"""INput from User(keyword)
in_Num = input() --- in_Num will be assigned with user enter value as STRING

"""
print("Enter a integer")
in_Num = input()
"""print("Total contribution:  ", 100 + in_Num)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'.
 You need to do type convertion as the input from keyboard is taken as string"""
print("Total   chants:  ", 100 + int(in_Num))


#summation calc for adding two numbers
print("Enter two numbers (press enter after each number)")
in_Num1 = input()
in_Num2 = input()
print("Sum of two number is  :  ", int(in_Num1)+int(in_Num2))
