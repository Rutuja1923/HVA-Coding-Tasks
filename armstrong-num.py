N=int(input("Enter a number : "))

count,sum = 0 ,0
num=N

while (num>0):
    r = num%10
    count+=1
    num//=10

dig_count = count
num = N

while count>0:
    r = num%10
    sum+= r ** dig_count
    num//=10
    count-=1

if sum == N :
    print("Yes")
else:
    print("No")
    