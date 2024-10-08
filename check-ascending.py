def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
isAscending = True 
i = 0

while i<l-1 :
    if not L[i]<L[i+1]:
        isAscending = False
        break
    i+=1
if isAscending:
    print("Yes")
else :
    print("No")
    

