"""
Check if a year isa a leap year or not.
Take year in 4 digit form (eg:2015) .
Call a function and display the appropriate message.
Author : @ChaitanyaJoshiX
"""

def isLeapYear(last_digits): # Creating a small function to check.
    if last_digits % 4 == 0:
        print("is a Leap year")
        print("~"*15)
    else:
        print("is not a Leap Year.")
        print("~"*15)

print("~"*30)
print("Welcome to Check Leap Year!")
print("~"*30)
year = input("Enter the year in 4 digit format (XXXX) : ") # Taking year as input.
print("You're entered year is :",year)
print("~"*30)
l = len(year) # Finding out the length of the string. (**Not necessary but just in case.)
last_digits = int(year[l-2:l]) # Using substring to find last two digits.
print(year,end = " ")
isLeapYear(last_digits) # Calling isLeapYear function.

"""
Author : @ChaitanyaJoshiX
"""
