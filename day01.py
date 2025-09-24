# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

#import datetime
#current_year = datetime.datetime.now().year

from datetime import datetime

now = datetime.now()

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))



#age = int(input("Enter your age: "))
#age = current_year - birth_year
age = now.year - birth_year

# print(type(name))
# print(type(age))

#print(f"Hello, {name}! You are { current_year - birth_year } years old.")
#print(f"Hello, {name}! Today is { datetime.datetime.now().strftime("%d.%m.%y") }!" +
#      " You are { age } years old.")
print(f"Hello, {name}! Today is { now.strftime("%d.%m.%y") }! You are { age } years old.")
