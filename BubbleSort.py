"""
Takes a list as input from user
Sorts the list.
display list before and after sorting
"""
list =[]
l = int(input("How many elements will there be in your list? : "))
print("Enter your elements one by one.")
for i in range(l):
    temp = int(input("Enter element "+str(i+1)+" : "))
    list.append(temp)
print("Original list :",list)
list.sort()
print("Sorted List :",list)
