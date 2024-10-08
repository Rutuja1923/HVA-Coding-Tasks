def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
isPerfect = False
i = 0

while i<l :
    sqrt = int(L[i]**0.5)
    if (sqrt**2 == L[i]):
        isPerfect = True
        break
    i+=1
if isPerfect:
    print(L[i])
else :
    print("No")
    

