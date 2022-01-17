"""
Write a program that inputs a student’s marks in n subjects (out of 100) and
Print the percentage marks.
"""
inp = input("")
inp = inp.split()
s, c = 0, 0
for i in inp:
    s += int(i)
    c += 1
s /= (c * 100)
s *= 100
print(s,"%")
