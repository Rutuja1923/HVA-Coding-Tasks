n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

maxNum = 0
if n1>n2 :
    maxNum=n1
else:
    maxNum=n2

while True:
    if maxNum%n1==0 and maxNum%n2==0 : 
        print(maxNum)
        break
    maxNum+=1