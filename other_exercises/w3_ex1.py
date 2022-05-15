# Write a Python program to create a class and display the namespace
# of the said class.

from builtins import abs


class Student:

    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year


# for name in Student.__dict__:
    # print(name)

# Write a Python program to create an instance of a specified class and
# display the namespace of the said instance.

Alex = Student('101SV', 'Alexandru', 2015)

for name in Alex.__dict__:
    print(name)

# builtins' module provides direct access to all 'built-in' identifiers of
# Python.

# Write a python program which import the abs() function using the builtins
# module, display the documentation of abs() function and find the absolute
# value of -155.


print(abs.__doc__)

print(abs(-155))
