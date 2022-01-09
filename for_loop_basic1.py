for x in range(0,151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if(x % 10 == 0):
        print("Coding Dojo")
    elif(x % 5 == 0):
        print("Coding")
    else:
        print(x)

y = 0
for x in range(1,500000,2):
    y = y + x
print(y)

x = 2018
while x > 0:
    print(x)
    x = x - 4

lowNum = 2
highNum = 9
mult = 3
while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum += 1