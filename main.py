"""

Q: What is a Python ?
Ans:
    Python is a Programming Language use in multiple domains like Machine Learning,
    Deep learning, Data Science, Web Development, Web Scrapping etc.

Q: What is a Programming Langugae ?
Ans:
    Human can interact with a System by using a Programming Languages.
    There are multiple langugages. Python, Java, C, C++, JavaScript,PHP etc.

    We write a code that actually a programe. A program is a set of instructions.

    basics example
    we want to add 2 values from system.
    instructions and statements are same.

    a = 10
    b = 20
    add = a+b
    print("Add is: ",add)


What is Syntax in programming Langugaes?
Ans:
    In simple words, A syntax is a set of rules to write a specific program
"""

# a = 10
# b = 25
# sum = a+b
# print("Sum is ==",sum)

# x = 5
"""
x is a variable.
In Programming variable is use to contain or hold some data or value. 
"""
#
# y = 15
# print(x,y)

# Q: How to dsiplay data on screen
# print("Here your data")
"""
In programming there are different datatypes of variable. 
example.
    Integer, FLoat, String, List, Tuple, Dictionary, Set, Boolean
"""

# nam = "Ali Khan"
# a = 10 # without points or decimal number
# PI = 3.14 # Float Value.
#
# print(type(a))
# print(type(PI))
# print((type(nam)))

"""
Variables are used to store some data or value. It is just like a container to contain some results
OR it is a holder that holds some data.


"""
# a = 10 # Integer
# name = "Ali" # String
# w = 3.14
# print(w)
# print(type(w))
# print(type(a))
# print(type(name))
# Statements OR Instructions and collection of instructions is called a Program.
# Syntax A set of rules to write a Program
# DataTypes
# - = 50
# print(-)

# print("Hello EveryOne Today is Our First Class of Python")

# Concatenation.... In simple words we will combine variable's value with Text Message
# name = "Omer"
# print("My Name is:",name) # Concatenation.


# Variable's Writing Style
# lowercase
# name = "Ali"
# #uppercase
# NAME = "Omer"
# # CapitalizeCase
# Name = "Asad"
# # CamelCase
# fullName = "Ali Khan"
# # SnakeCase
# my_full_name = "Omer Khan"
# myfullname = "Haris Khan"
"""
Integer
String
Float
Boolean
List 
Tuple
Set
Dictionary
"""

"""
IMPORTANT POINT:
                Python is a Case Sensensitive Langugage
                Example:
                    a = 10
                    A = 12
                    Here, a and A both are different not same.
"""
# a = 10
# A = 20
# print(A)

# # Text Formatting
# firstName = "Haris"
# lastName = "Khan"
# fulName = firstName+" "+lastName
# # print("My Full Name is",fulName)
# print(f"My First Name is {firstName} and My Last Name is {lastName}")


"""
How to Display message on screen
print()
"""
# print("Hello Everyone")
# name = "Asad"
"""
How to take value from User?
Ans:
    We will use input() function to take user-define value
    IMPORTANT POINT is input function always gives String data
"""
# hintMessage = "Please Enter your Name"
# name = input(hintMessage)
"""
How to check DataType of any specific variable?
Ans:
    We will use type()
"""
# print(type(name))
# print("My Name is {}".format(name))
# print(f"My Name is {name}")

"""
Q: Write a Program to add 3 values ?
"""
# num1 = 10
# num2 = 15
# num3 = 5
# addValues = num1+num2+num3
# print("Total Sum is:",addValues)


"""
ctrl+? is use for multi-line comments after selecting multiple lines.
"""

# num1 = 10
# num2 = 15
# num3 = 5
# addValues = num1+num2+num3
# # print(f"Value of Num1 is {num1} and Value of Num2 is {num2} and Value of Num3 is {num3} and Value of Total is {addValues}")
# print("Value of Num1 is {} and Value of Num2 is {} and Value of Num3 is {} and Value of Total is {}".format(num1,num2,num3,addValues))

"""
Strings 
Strings Builtin functions
User define
"""
# name = "ali khan"
# NAME = "BILAL KHAN"
# # print(name.upper())
# print(NAME.lower())

# brand = "kfc"
# # print(brand.capitalize())
# print(brand.islower())

"""
Slicing 
        We can get a substring from a string
        Syntax:
            string[start:end] end point is not included
        
        Convert one type to another is called a Type Casting
        
"""
# text = "My name is Bilal"
# print(text[3:8])
# weight = str(44.5)
# print(type(weight))

"""
List Data Type 
Lists are use for the collection data.
a = 10
b= 15
10,15,12,11

    Syntax:
        listData = [ 1,2,3,4,5,6 ]
"""
# a = 1
# b = 23
# c = 66
# numbers = [ 1,23,66,44,33 ]
# print(type(numbers))
"""
How we can access data from List
Ans:
    We can assess data from list using Index Numbers. Index NUmbers are actually position number
    and in Programmn=ing Languages Index Number is always start from Zero 0.
"""


# names = ["Ali","Omer","Khan","Haris","Butt"]
# print(names)
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
"""
We want to get Data from List and we need data except 1st and Last data element.
We will apply slicing on list 
Why we are using Negative Index 
If we are using Negative it will gices the last element of the list.
"""
# names = ["Ali","Omer","Khan","Haris","Butt"]
# print(names[1:-2])
"""
How we can display reverse List
"""
# print(names[::-1])

"""
Technical we can prove that python is a case sensitive language by using a builtin function name 
id()
"""
# name = "Ali"
# name = "Omer"
# print(id(name))
# print(id(name))

"""
What is Variable Declaration and Initialization ?
VD:
    In simple words VD is just create a new variable is called a Variable Declaration.
    example:
            a = 10

VI:
    In simple words, VI is just to assign a value or Data to a newly create variable.
    OR to pass a value to a variable is called VI
"""

"""
What are rules to create a Variable ?
1.  the variWe cannot use number atable of the variable.
2. We cannot use a keywords for a Variable
3. We can use underscore at the start of a variable 
4. We canot use a Special characters at the start.
"""

# a# = 10
# print(a)

"""
Keywords are reserve words use in programming langugae for the specific purpose we cannot use them for creating 
a variable
"""
# a = 10
# if a>10:
#     print("A")
# else:
#     print("Nothing")
# if1 = 10
# print(if1)

"""
You should give 2 Hours to Python Practice lecture time is excluded. It means you should give atleast 3 Hours to
Python Programming.
"""




