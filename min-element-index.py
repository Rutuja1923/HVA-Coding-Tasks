def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count
print("Enter array elements :")
L=list(map(int,input().split()))
l = find_len(L)
minInd=0
i=1
while i<l:
    if L[i]<L[minInd]:
        minInd=i
    i+=1
print(minInd+1)