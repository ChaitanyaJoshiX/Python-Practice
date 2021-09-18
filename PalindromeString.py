"""
Create a Palindrome Program for string.
Take string as user input.
Check if the the reversed string is same as the original.
Display appropriate output.
Author : @ChaitanyaJoshiX
"""

def checkResult(result):

    if result == True:
        print(orig_string,"is a palindrome string.")
        print("~"*25)

    else:
        print(orig_string,"is not a palindrome string.")
        print("~"*25)

def isPalindromeString(l,orig_string):
    conv_string = ""
    while l != 0:
        conv_string +=  orig_string[l-1]
        l -= 1
    print("The reversed string is : ",conv_string)
    if orig_string.lower() == conv_string.lower():
        return True
    else:
        return False


print("~"*35)
print("Welcome to the Palindrome String Checker!")
print("~"*35)
orig_string = input("Enter your string : ")
l = len(orig_string)

result = isPalindromeString(l,orig_string)

checkResult(result)

"""
Author : @ChaitanyaJoshiX
"""
