#This program can print the mathematical table of any number upto n multiples
num = int(input("Which number's table do want : "))
mul = int(input("How many multiples do you wish : "))
print("~~~~~~~~~~~~~~~~~~~~~~~")
print("Table of",num)
print("No.   Multiple")
for i in range(1,(mul+1)):
    if(i > 9):
        print(i,"  ",num*i)
    else:
        print(i,"   ",num*i)
print("~~~~~~~~~~~~~~~~~~~~~~~")
