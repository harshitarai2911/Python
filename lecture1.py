print("Hello everyone")
print('Hello world')
print("I'm Harshita Rai ")
# print is a function in Python that outputs text to the console.
print("I am a student of B.Tech CSE" , " and currently in 2nd year")
# , is used to separate multiple items in the print function, and it adds a space between them by default.
print(23+35)
print("The product of 23 and 35 is:", 23*35)
num1=14
#num1 is a variable that stores the value 14.
num2=12
print("The perimeter of rectangle is:", 2*(num1+num2))
name="tanu"
# name is a variable that stores the string "tanu".
age=19
# age is a variable that stores the integer 19.
price=19.66
# price is a variable that stores the float 19.66.
age=age+1
# age is incremented by 1, so it becomes 20.
print(name)
print(age)
print(price)
age2=age # age2 is assigned the value of age, which is 20 after incrementing by 1.
print(age2)
# name of variable should be meaningful and should not start with a number or special character. It can contain letters, numbers, and underscores.
print(type(name))
print(type(age))
print(type(price))
# primary datatypes are integers , string , float , boolean , none
# boolean values are True and False 
age = 23
old = False
a = None
print (type(old))
print (type(a))
# keywords are reserved words in python
# python is case sensitive
a = 2;
b = 5;
sum = a + b;
print("The sum of a and b is:", sum)

'''
This is a multiline comment in Python.
It can be used to comment out multiple lines of code.
'''
# arithmetic operators
c = 10
d = 6
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c%d)
print(c**d)

# relational operators
e = 50
f = 20
print(e == f)
print(e != f)
print(e > f)
print(e < f)
print(e >= f)
print(e <= f)

# asssignment operators
g = 10
g += 5
print(g)
h = 10
h -= 5  
print(h)
i = 10
i **= 5 # ** is the exponentiation operator, so i **= 5 means i = i ** 5, which raises i to the power of 5.
print(i)
# logical operators
j = True
k = False
print(j and k)
l = True
m = False
print(l or m)
n = True    
print(not n)

''' 
type conversion
it automatically converts one data type to another when performing operations between different types.
'''
o = 2
p = 4.25
sum1 = o + p
print(sum1) # automatically converts into superior data type, which is float in this case.

'''
type casting
it is the process of converting one data type to another explicitly using built-in functions.
'''
q = int("10")
r = 20
sum2 = q + r
print(sum2) # converts string "10" to integer 10 and adds it to 20, resulting in 30.
print(type(q)) # prints the type of q, which is <class 'int'> after conversion.

s = str(3.14)
t = "Hello"
u = s + t
print(u) # converts float 3.14 to string "3.14" and concatenates it with "Hello", resulting in "3.14Hello".

''' 
input function
it is used to take input from the user. The input is always taken as a string.
int () function is used to convert the input string to an integer.
int (input()) is used to take integer input from the user.
float (input()) is used to take float input from the user.
'''

'''
name = input("Enter your name: ")
print("Welcome", name)

if we'll take any integer or float as input, it will be taken as a string. 
this is why we need to use int() or float() to convert the input string to the desired data type.
basically we are doing type casting here.

age = int(input("Enter your age:"))
print("Your age is:", age)
'''

first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
Total=first+second
print("the sum of",first,"and",second,"is:",Total)
