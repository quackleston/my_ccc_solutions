"""
TELEMARKETER OR NOT??

telemarketers like to use seven-digit phone numbers
where last four digits have three properties:
- first of these four digits in 8 or 9
- last digit is 8 or 9
- second and third digits are same
- examples: 8229, 8338, 9008


you must:
write a program to decide if telephone is telemarketer or not
(if yes, ignore, if no, answer)
"""


alist = []

for i in range(4):
    numbers = input()
    alist.append(numbers)

if alist[0] == "8" or alist[0] == "9":
    if alist[1] == alist[2]:
        if alist[3] == "8" or alist[3] == "9":
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")


#print(alist[1:3]) #middle numbers

