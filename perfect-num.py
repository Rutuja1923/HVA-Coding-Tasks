n = int(input("Enter a number : "))
i , sum = 1 , 0
while i<n:
    if n%i == 0:
        sum+=i
    i+=1
if sum==n:
    print("Yes")
else:
    print("No")