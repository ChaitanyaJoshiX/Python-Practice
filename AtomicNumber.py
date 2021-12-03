ElementsList = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
AtomicList = [1, 2, 3, 4, 5]
MassNumber = ["1", "4", "7", "9", "11"]
Nature = ["Non-Metal", "Noble Gas", "Metal", "Metal", "Metalloid"]
input = input("Enter the atomic number of the element : ")
print(input)
temp = input
input = int(input)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(5):
    if input == AtomicList[i]:
        print("Element\t  Atomic No.   Nature\tMass Number")
        print(ElementsList[i]+"\t   "+temp+"\t       "+Nature[i] +"\t"+ MassNumber[i])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Thank you for running my program :)")
"""
End of the program:)
"""
