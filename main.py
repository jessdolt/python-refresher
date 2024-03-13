
#### Typing of variables
# x = 3 
# y = '3'
# z = 3.0

# print((str(x)))
# print((int(y)))
# print((float(z)))

#### Assign Multiple Values
# x, m = ["Orange", "Banana", "Cherry"]
# print(x)
# print(y)
# print(z)

#### Global Variables
# x = 'jess'
# def myfunc():
#     x = 'fantastic'
#     print(x)
# myfunc()
# print(x)

# x = 'jess'

# def myfunc():
#     global x
#     x = "fantastic"
#     print(x)
    
# myfunc()
# print(x)


#### Data types
# x = range(5)
# print(x)

# x = list(('asd', 'asdzxc'))
# y = tuple(('asd', 'asdzxc'))
# print(x)
# print(y)


#### Strings

### Multiple line and single line quotes
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''

# print(a)
# a="Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
# print(a)


# a = 'Hello world'
# print(a[1])

# for x in 'akosijessangelroque':
#     print(x)

# txt = "The best things in life are free and jess!"
# print("Jess" in txt.lower())

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# b = " Hello, World! "
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# print(b[-5:-2])

# print(b.upper())
# print(b.lower())
# print(b.strip())
# print(b.replace('o', 'a'))
# print(b.strip().split(','))

# concat_word = 'years old'
# age = 36
# txt = "My name is John, I am {age} {concat_word}" 
# print(txt.format(age=age, concat_word=concat_word))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {2} pieces of item {0} for {1} dollars."
# print(myorder.format(quantity, itemno, price))

# a = "We are the so-called \"Jess\"  from the north."
# print(txt)
# print(a.count('the'))

# are_index = a.find('are')

# print(a[are_index:])
# txt = "For only {price:.2f} dolls!"
# print(txt.format(price = 490_000))
# txt = "plpl"

# x = txt.zfill(10)

# print(x)


#### List
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[2:] = ["blackcurrant", "watermelon", 'newfruit']
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# cherryIndex = thislist.index('cherry')
# thislist.insert(cherryIndex, 'new fruit banana')

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in range(len(thislist))]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

#### LIST COMPERHENSION
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a"]
# newlist = [x for x in fruits if x != "apple"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)



#### SORTING
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.upper )
# print(thislist)


#### LIST JOIN
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


###### TUPLES
# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

#### MUTABLE OBJECTS BY MAKING IT TO LIST AND CHANGE IT BACK TO TUPLE
# x = ('apple', 'banna', 'cherry')
# print(x)
# y = list(x)
# print(y)
# y[1] = 'mango'
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

#### UNPACKING TUPLES
# fruits = tuple(("apple", "banana", "cherry", "mango", 'adobo'))
# fruits2 = list(('apple', 'mango', 'apple'))
# (green, yellow,  *red )= fruits
# c,z,b = red

# print(c,z,b)
# print(green)
# print(yellow)
# print(red)

# print(fruits.count('mango'))
# print(fruits2.count('apple'))


#### SETS
# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset) 

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)

# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)

# x = {"apple", "banana", "cherry", True}
# y = {"google", 1, "apple", 2}

# z = x.symmetric_difference(y)

# print(z)


#### DICTIONARIES
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# x = thisdict.get("model")
# print(x)
# x = thisdict.keys()
# print([i for i in x])

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# # x = car.values()

# # print(x) #before the change

# # car["year"] = 2020

# # print(x) #after the change

# x = car.items()
# for (i,x) in x: 
#     print(i,x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)

# thisdict = {
#   "year": 1964,
    
#   "brand": "Ford",
#   "model": "Mustang",
# }
# # thisdict.popitem()
# # print(thisdict)
# # for x in thisdict:
# #   print(x)
  
# # for x in thisdict:
# #   print(thisdict[x])

# for x in thisdict.values():
#   print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily['child2']['year'])



# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(x, /):
#   print(x)

# my_function('po')

# def my_function(*, x, y, z):
#   print(x,y)

# my_function(x=32, y='we', z='3')

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# fruits = [{
#     "name": "mango"
# }]

# testtt = {
#     x: v
#     for x,v in fruits[0]
# }

# print(testtt)

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))


#### CLASS
# class MyClass:
#   x = 5
  
# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()