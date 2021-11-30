"""
Check if a number is a duck number.
A number is called a duck number if,
zeroes are present in it but there should be no zero present at the beginning of the number.
Example:
3210 --> (Duck Number)
042  --> (Not Duck Number)
"""
num = input("Enter the number : ")
cond = False
if num[0] == '0':
    print(num,"is not a Duck number!")
else:
    for digit in num:
        if digit == '0':
            print(num,"is a Duck Number!")
            cond = True
            break
    if cond != True:
        print(num,"is not a Duck number!")
