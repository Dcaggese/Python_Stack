#Print all integers 0 - 150

for x in range(0,151):
    print(x)

#Print all multiples of 5 from 5-1000

for x in range(0,1001):
    if x%5 == 0:
        print(x)

#Print integers 1-100. If divisible by 5 print "coding" instead. If divisible by 10, print "Coding Dojo"

for x in range(0,101):
    if x%5 == 0 and x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)

#Add all odd integers from 0 to 500,000 and print the sum

sum = 0;

for x in range(0,500001):
    if not x%2 == 0:
        sum += x

print(sum)

#Print positive numbers starting at 2018, counting down by fours

for x in range(2018,-1,-4):
    print(x)

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult

lowNum = 2
highNum = 250
mult = 3

for x in range(lowNum,highNum):
    if x%mult == 0:
        print(x)