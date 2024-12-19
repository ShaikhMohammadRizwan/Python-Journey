Data Types in Python:-

1. Numerica
    int
    float
    complex type

2. Sequence:-
    List
    String
    Tuple

3. Dictonary
4. Set

o Mutable Object can change it state or contents and immutable objects cannot.

Mutable Data Types :-

    1. List
    2. Dictonary
    3. byte array

Immutable Data types :-

    1. int
    2. Float
    3. Complex
    4. String
    5. Tuple
    6. set

********* Data Types **********

1. Number
    intergers
    float
    complex numbers



a = 5
print(a, "is type of ", type(a))
# 5 is type of  <class 'int'>

b = 3.12
print(b, 'is type of', type(b))
# 3.12 is type of <class 'float'>

c = 2+3j
print(c, 'is type of', type(c))
# 3.12 is type of <class 'float'>


2. String

* A String is a collection of one or more character put in a single, double or tripple Quote
* Multi-Line String can be denoted using triple quotes, ''', or """ ///////(/""" ''')


s1 = 'Rizwan Shaikh'
print(s1)
# Rizwan Shaikh

s2 = "Rizwan Shaikh"
print(s2)
# Rizwan Shaikh

s3 = '''
    Rizwan Shaikh 
        Back-end Developer
            Using Python, Django

    '''
print(s3)
#     Rizwan Shaikh
#         Back-end Developer
#             Using Python, Django


3. List

* List is an Ordered Sequence of items.
* It is one of the most used data types in python and is very flexible.
* it is Dentoed by [ ]

a = [1, 2, 3, 'A', 1j]

a [4] = 5
# [1, 2, 3, 'A', 5]

print(a, type(a))
# [1, 2, 3, 'A', 1j]
# <class 'list'>

4. Tuple

* Tuple is an Orderd Sequence of items same as list.
* It is defined within a parameters ( ) where items are seprated by commas.
* Tuple is fast and other side List.
* Tuple ke ander ek se zyada value hone cahiye agar usme ek value hui to wo tuple count nai hoga.
* Tuple is Immutable

t = (5, 'Hello', 10)
print(t)
# (5, 'Hello', 10)

print(type(t))
# <class 'tuple'>

5. Dictoionary

* Dictionary is an unorderd Collection of key-vaues pair.
* In Python, dictonaries are defined within { } with each item beign a pair in the form key-value pair.
* Dictonary is Unique not defined same key in dictionary
* Dictionary is Mutable

d = {
    1: 'value',
    'key': 2
}

d = {
    'course_name': 'Python',
    'course_fees': 'Free',
    'Duration': 90,
    'Timing': 'Any'
}

print(d)
# {'course_name': 'Python', 'course_fees': 'Free', 'Duration': 90, 'Timing': 'Any'}

print(type(d))
# <class 'dict'>

print(d['course_fees'])
# Free

6. Set

* A Set is an Unordered Collection of items.
* Every-Set element is unique (No Duplicates) and must be immutable (cannot be changed)
* denoted by { }

my_set = {1, 2, 3}
print(my_set)
#{1, 2, 3}

print(type(my_set))
# <class 'set'>

set = { }