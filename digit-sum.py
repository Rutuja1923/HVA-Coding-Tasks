N=int(input("Enter a number : "))
sum=0
num=N
while (num>0):
    r = num%10
    sum+=r
    num//=10
print(sum)