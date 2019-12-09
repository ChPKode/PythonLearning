#tut09
#List Data Structure"Python List
list = [] #create a empty list
print(type(list))

""""Lists are just like the arrays, declared in other languages. 
Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.

List in Python are ordered and have a definite count.
The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index. Each element in the list has its definite place in the list, which allows duplicating of elements in the list, with each element having its own distinct place and credibility.

Note- Lists are a useful tool for preserving a sequence of data and further iterating over it."""

grocery = ["banana", "orange", "apple"]
print(grocery[0])
print(grocery[0:10])

num_list1 = [1,10,210,930,430,509]
print(num_list1)
print(num_list1.sort())   #Output : None.
num_list1.sort()  #Sorts the num_list1 a creates a new list ans assigns it tot num_list1(changes the original list)
print(num_list1)   #[1, 10, 210, 430, 509, 930]
num_list1.reverse()  #new(num_list1) reverse list is created from num_list1
print(num_list1)  #[930, 509, 430, 210, 10, 1]

#Slicing
print(num_list1[1:4])
"""Note  : Slicing return the list"""
#extended list
print(num_list1[::-1])   #print(num_list1[::-2])  print(num_list1[::-3])  may cause problem.


#list methods
#append
num_list1.append(100)   #Add at the end of the list
num_list1.append(100)
num_list1.append(100)
num_list1.append(100)
num_list1.append(100)
num_list1.append(100)
num_list1.append(100)
print(num_list1)

num_list1.insert(2,50)  #adds at specific index
print(num_list1)
num_list1.remove(50) #remove element from list
print(num_list1)
num_list1.pop()
print(num_list1) #deletes the last element from list


#Tuple
#immutable list
t = (1,2,3,4,6,8,7,10,41,23,31)
print(type(t))


#swap two numbers
s1 = 7
s2 = 4
print(s1,s2)
s1, s2 = s2, s1
print(s1,s2)

"""Dictionary -- data structure
key : value pair
"""
dic1 = {}
print(type(dic1))
nestDic = {1: [1, 2, 3, 4], 'Name': 'Geeks'}
nestDic["Country"] = "India"
print(nestDic)
del nestDic["Country"]
print(nestDic)

nestDic2 = nestDic
nestDic3 = nestDic.copy()   #Shallow copy
print(nestDic2.get("Name"))

nestDic2.update({"City":"New Delhi"})   # equivalent to nestDic["Country"] = "India"
print(nestDic)


print(nestDic.keys())
print(nestDic.items())

#My own dictionary
ownDict = {"abate":"become less in amount or intensity","abhor":"find repugnant","abortive":"failing to accomplish an intended result","absolve":"grant remission of a sin to","abstruse":"difficult to understand","accolade":"a tangible symbol signifying approval or distinction","accost":"approach and speak to someone aggressively or insistently","acquiesce":"agree or express agreement"}
print("List of words in my dictionary : " , ownDict.keys())
print("Enter word to find the meaning")
wordIn = input()
print("Entered word ", wordIn, " meaning is : ", ownDict[wordIn])
