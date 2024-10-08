def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
found = False
i = 0

while i<l :
    if L[i]<0:
        found = True
        break
    i+=1
if found:
    print("Yes")
else :
    print("No")
    

