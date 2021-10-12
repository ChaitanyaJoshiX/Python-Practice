"""
Check if number is a Krishnamurthy number.
A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself.
Example : 145.
"""
n = input("Enter the number you want to check : ")
print(n)
n = int(n)
toCheck = n
digit = 0
fact = 1
sum = 0
while n!= 0:
    digit = n % 10
    count = digit
    while count >= 1:
        fact *= count
        count -= 1
    sum += fact
    fact = 1
    n = int(n/10)
if toCheck == sum:
    print(toCheck,"is a Krishnamurthy Number")
else:
    print(toCheck,"is not a Krishnamurthy Number")
