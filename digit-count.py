N=int(input("Enter a number : "))
count=0
num=N
while (num>0):
    r = num%10
    count+=1
    num//=10
print(count)