"""
WAP to enter a list.
Reverse the list 
return the resulting list.
Author : @ChaitanyaJoshiX
"""
inplist = input("Enter list elements separated by space : ")
inplist = inplist.split()
outlist = []
l = len(inplist)
j = l-1
for i in range(l):
    outlist.append(inplist[j])
    j -= 1
print(outlist)
"""
Later, I realised that the reverse() function is already present in a py lib.
So, I remade the program in C++
"""
