# take input

# a = input('Enter a number: ')
# print(a)

"""
    Eventhough the input are numbers, input() function only take it as String.
    'single quotes' and "Double quotes" are same in pyton


"""
# Example

# a = input('Enter a number : ')  # "10"
# b = input('Enter a number : ')  # "20"
# c = a + b
# print(c)  # "1020" not 30
#
# # Resolving the problem
# a = int(input('Enter a number : '))  # "10" -> 10
# b = int(input('Enter a number : '))  # "20" -> 10
# c = a + b
# print(c)  # 30

# name = input()  # "EMC"
# age = input()   # "1"
# print('My Name is :', name)
# print('My Age is :', age)


# name = input()  # "EMC"
# age = input()   # "1"
# address = input()   # Keeranur, Pudukkotai
# print('My Name is :', name)
# print('My Age is :', age)
# print('My Address is :', address)

# name = input('Enter your name : ')   # "10" -> 10
# score = int(input('Enter your score (out of 100) : '))   # "20" -> 20
# department = input('Enter your department : ')   # "30" -> 30
# outOfTen = score/10
# print('My Name is', name)
# print('My Score is', outOfTen,'/10')
# print('My Department is', department)

# score = int(input('Enter your score (out of 100) : '))
# if score <= 35:
#   print('Poor Student')
# elif 35 < score < 70:
#   print('Average Student')
# else:
#   print('Good Student')
#
# a = int(input('A : '))
# b = int(input('B : '))
# operation = input('Operation : ')

# if operation == 'add':
#   print('Addition of A and B is', a+b)
# elif operation == 'sub':
#   print('Subtraction of A and B is', a-b)
# elif operation == 'multi':
#   print('Multiplication of A and B is', a*b)
# elif operation == 'div':
#   print('Division of A and B is', a/b)
# else :
#   print('Invalid Operation')

# score = int(input('Enter the score : '))
#
# if score > 70:
#     name = input('Enter the name : ')
#     department = input('Enter the department : ')
#     location = input('Enter the location : ')
#     print('Eligible')
# else:
#     print('Not Eligible')

# salary = int(input('Enter your Salary : '))
# age = int(input('Enter your age : '))
#
# if salary >= 20000 or age <= 25:
#     loanAmount = int(input('Enter your loan amount : '))
#     if loanAmount <= 50000:
#       print('You are eligible for load')
#     else:
#       print('Maximum loan amount is 50,000')
# else:
#     print('You are not eligible for loan')

# for i in 'apple':
#   print(i)

# for i in range(5):
#   print(i)

# for j in range(1,11):
#   for i in range(1,11):
#     print(i, 'x', j ,'=', i*j)

#
# a = int(input('Enter the starting number :'))
# b = int(input('Enter the ending number :'))
#
# for i in range(a,b):
#   print(i)

# n = int(input('Enter the number : '))
# count = 0
# for i in range(1,n+1):
#   if i % 2 == 0 :
#     count += 1
# print(count)

# sum = 0
# for i in range(1,11):
#     # a = 'Enter the number', i, ':'
#     n = int(input(f'Enter the number {i}: '))
#     sum += n
# print('sum is',sum)
# print('avg is', sum/10)

# n = int(input('Enter the number : '))
# for i in range(n):
#   print(f'Number is : {i+1} and cube of the {i+1} is : {(i+1)*(i+1)*(i+1)}')

# n = int(input('Enter the number : '))
# for i in range(1,n+1):
#   print(f'Number is : {i} and cube of the {i} is : {i*i*i}')

n = 5

# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(j, end=' ')
#   print()


# n = int(input('Enter the number : '))
#
# for i in range(n+1):
#   list = ''
#   for j in range(i):
#     list += '*'
#   print(list)

# n = int(input('Enter the number : '))
#
# for i in range(n+1):
#   for j in range(i):
#     print('*', end=' ')
#   print()

# a = []
# a.append(1)
# print(a)
# a.append(2)
# print(a)
# a.append(True)
# print(a)
# a.append('emc')
# print(a)
# # print length of list
# print(len(a))
# # add value at specific index
# a.insert(1,80)
# print(a)
# # modify value at specific index
# a[2] = 35
# print(a)
# # access element at specific index
# print(a[3])
# # remove element as per index (0 based indexing) -> 0 till len(a)-1
# a.pop(1)
# print(a)
# # remove element at the end
# a.pop()
# print(a)
# # merge two list
# b = [1,'bcs', False]
# a.extend(b)
# print(a)
#
# a = (1,2,3,4)
# b = list(a)
# print(a)
# print(b)

# a = [10,11,23,32,42,43,31,43]
# print(a[2:5])
#
# print(a[:4])
# print(a[2:])
# print(a[-4:-1])

# Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# a = [1,2,3,4,5,67]
# a.remove(5)
# del a[3]
#
# print(a)

# a = [223,4,5,6,7,8,8,8]
# [print(x) for x in a]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
#
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x != 'apple']
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# thislist = [100, 50, 65, 82, 23, 213]
# thislist.sort()
# print(thislist)

# def myfunc(n):
#   return abs(70-n)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

#
# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)

# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, *yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)

# thisset = {"apple", "banana", "cherry", True, "1", 2}
# ajaiSet = {'name', 'apple', 'Parthiban', 'Velmurugan'}
# thisset.extend(ajaiSet)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange", "apple"]
#
# thisset.update(mylist)
#
# print(thisset)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.intersection_update(set2)
# print('DEBUG')
# print(set1)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.items()
#
# print(x) #before the change
#
# car["colour"] = 2020
#
# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# list = "Ford"
#
# if list in car.values():
#     print('I am the greatest of all time')
# else :
#     print('Please put some mustard oil in your eyes')

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# for x in thisdict:
#   print(x)

# for x in thisdict:
#   print(thisdict[x])
#
# for x in thisdict.values():
#   print(x)
#
# for x in thisdict.keys():
#   print(x)
#
# for x, y in thisdict.items():
#   print(x, y)

# def add(x, y):
#   return x + y
#
#
# def sub(x, y):
#   return x - y
#
#
# def multi(x, y):
#   return x * y
#
#
# def div(x, y):
#   return x / y
#
#
# a = int(input('Enter the value for x : '))
# b = int(input('Enter the value for y : '))
#
# print('x + y =', add(a, b))
# print('x - y =', sub(a, b))
# print('x * y =', multi(a, b))
# print('x / y =', div(a, b))


# def findPassOrFail(x):
#   if x >= 35:
#     print('PASS')
#   else:
#     print('FAIL')
#
# n = int(input('Enter the number : '))
# findPassOrFail(n)

# def printRange(a,b):
#   for i in range(a, b+1):
#     print(i)
#
# x,y = int(input('Enter the Starting number : ')), int(input('Enter the ending number : '))
#
# printRange(x,y)

# def validate(x,y):
#   s_userName = 'EMC'
#   s_password = '123'
#
#   if x == s_userName and y == s_password:
#     return 'Both username and password are valid'
#   elif x != s_userName and y == s_password:
#     return 'Invalid username'
#   elif x != s_userName and y == s_password:
#     return 'Invalid password'
#   else:
#     return 'Both username and password are invalid'
#
#
# a = input('Enter your username : ')
# b = input('Enter your password : ')
#
# print(validate(a,b))

# def add(x, y):
#     return x + y
#
#
# def mulit(x, y):
#     return x * y
#
#
# a = int(input('Enter the value of a : '))
# b = int(input('Enter the value of b : '))
# c = int(input('Enter the value of c : '))
#
# print(mulit(add(a, b), c))

# multi = lambda x,y : x*y
# print(multi(5,6))

# def multi(n):
#   return lambda a : a*n
#
# myTriple = multi(3)
#
# print(myTriple(11))


# class Laptop:
#     price = 0
#     processor = ""
#     ram = 0
#
#
# HP = Laptop()
# HP.price = 10000
# HP.processor = "intel i5"
# HP.ram = 16
# DELL = Laptop()
# DELL.price = 12345
# DELL.processor = 'intel i3'
# DELL.ram = 8
# LENOVO = Laptop()
#
# print(HP.price, DELL.price, LENOVO.price)

# class Student:
#     def __init__(self):
#         self.name = ""
#         self.registerNumber = 0
#
#     def display(self):
#         print('Student Name :', self.name)
#         print('Student Register Number :', self.registerNumber)
#
#
# ajai = Student()
# sharan = Student()
# ajai.name = "Ajai"
# ajai.registerNumber = 420
#
# ajai.display()
# sharan.display()

# class Fruit:
#     def __init__(self, color):
#         self.color = color
#     def display(self):
#         print('The color is', self.color)
#
#
# apple = Fruit('Red')
# apple.display()

# class Teacher:
#     def __init__(self, name, regNo):
#         self.name = name
#         self.regNo = regNo
#
#     def display(self):
#         print('Teacher name', self.name)
#         print('Teacher register Number', self.regNo)
#
#
# t1 = Teacher('Velmurugan', 12345)
# t2 = Teacher('Ajai', 54321)
#
# t1.display()
# t2.display()

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def multi(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
#     def display(self):
#         print('a + b =', self.add())
#         print('a - b =', self.sub())
#         print('a * b =', self.multi())
#         print('a / b =', self.div())
#
#
# sample = Calculator(1, 5)
#
# sample.display()


# class Laptop:
#     # class variable
#     chargerType = "C-Type"
#
#     def __init__(self, name, processor, ram):
#         # instantaneous variable
#         self.name = name
#         self.processor = processor
#         self.ram = ram
#
#     def display(self):
#         print('Laptop name :', self.name)
#         print('Laptop processor :', self.processor)
#         print('Laptop ram :', self.ram)
#         # we can access the class variable using object reference as well
#         print('Laptop charger type :', self.chargerType)
#
#
#
# hp = Laptop('hp', 'intel i5', '16GB')
# dell = Laptop('dell', 'intel i3', '8GB')
# lenovo = Laptop('lenovo', 'intel i7', '32GB')
#
# print('before changing the value in class variable')
# hp.display()
# dell.display()
# lenovo.display()
#
# Laptop.chargerType = "B-Type"
#
# print('after changing the value in class variable')
# hp.display()
# dell.display()
# lenovo.display()


# class Laptop:
#
#     chargerType = 'C Type'
#
#     def __init__(self):
#         self.brand = ""
#         self.price = 0
#
# # instantaneous method -> accessing both class and instantaneous variable.
#     def setPrice(self, price):
#         self.price = price
#     def getPrice(self):
#         print(self.price)
#
# # class method  ->  accessing only class variable.
#     @classmethod
#     def changeCargerType(cls, chargerType):
#         cls.chargerType = chargerType
#         print(chargerType)
#
# # static method -> we can not access neither class variable nor instantaneous variable
#
#     @staticmethod
#     def info():
#         print("Buy pc not laptop")
#
#
#
#
#
#
# hp = Laptop()
# # accessing instantaneous method
# hp.setPrice(720)
# hp.getPrice()
#
#
# # accessing class method
# Laptop.changeCargerType('B-Type')
#
# # accessing static method
#
# Laptop.info()
# # (or)
# hp.info()


# class Shape:
#     def area(self):
#         return 0
#
#
# class Rectangle(Shape):
#     def area(self, length, width):
#         return length * width
#
#
# obj = Rectangle()
# print(obj.area(10, 15))

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)
#         self.grade = grade
#
#     def display(self):
#         print('Student name :', self.name)
#         print('Student grade :', self.grade)
#
#
# obj = Student('ajai', "A")
# obj.display()

# class Vehicle:
#
#     def start(self):
#         print('Vehicle started')
#
#
# class Car(Vehicle):
#
#     def start(self):
#         print('Car started')
#
#
# obj = Car()
# obj.start()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#
#     def display(self):
#         print('Manager Name :', self.name)
#         print('Manager salary :', self.salary)
#         print('Manager department :', self.department)
#
#
# obj = Manager('Ajai', '12345', 'Computer')
# obj.display()

# a = '     Hello, world!    '
# print(a.split(' '))

# import pyautogui as pg
# import time
#
# time.sleep(8)
#
# for i in range(11):
#     pg.write('Hi, ')
#     pg.write('I am BAT man')
#     pg.press('enter')

# price = 5.34353
# txt = f'The price of the phone is {price:.2f}'
# print(txt)

# x = "0"
# y = 0
#
# print(bool(x))
# print(bool(y))
# x = 'kumar'
# y = 'kumar'
# print(x is y)

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# class Student:
#
#     def __init__(self, name, std):
#         self.name = name
#         self.std = std
#
#
#
# ajai = Student('ajai', 4)
#
# print(ajai)

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()


# def myfunc1():
#     x = "Jane"
#
#     def myfunc2():
#         nonlocal x
#         x = "hello"
#
#     myfunc2()
#     return x
#
#
# print(myfunc1())

import random
import string


# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password
#
#
# password_length = int(input("Enter the length of the password: "))
# generated_password = generate_password(password_length)
# print("Your random password is:", generated_password)


# import platform
#
# x = dir(platform)
# print(x)

import datetime

x = datetime.datetime.now()

# print(x.year)
date = x.strftime("%x")

if '15' in date:
    print (True)
else :
    print (False)
