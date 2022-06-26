# Data Structure -> Collection of Data Types

"""
Tuples and Lists Differenciation
1. Parantheses and Square Brackets
2. Immutable and Mutable
"""

"""
Data Types : 
Strings
Integers
Floats
Booleans

Data Structures : 
Lists
Tuples
Dictionaries
Sets
"""

t1 = (1,2,3,4,5,"kaustubh","kodi")
# print(t1)
# print(type(t1))

# print(len(t1))
# print(t1[5][0:4])

# Tuple with Loops
for i in t1:
    print(i)

# Tuple with 1 element
name=("kodi",)
print(type(name))

# Tuple Unpacking
cars = ("Rolls Royce", "Ferrari", "BMW x5", "Audi", "Marauder")
car1, car2, car3, car4, car5 = cars
print(car1)
print(car5)

# TUple without Parantheses
bikes = "ktm", "hardly davidson", "royal enfield", "hayabusa", "apache"
print(type(bikes))

