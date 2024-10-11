def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count
    
print("Enter array elements :")
L=list(map(int,input().split()))
l = find_len(L)

minDiff=L[0]
maxDiff=L[0]
i=1 

while i<l:
    if L[i]<minEle:
        minEle = L[i]
    if L[i]>maxEle:
        maxEle = L[i]
    i+=1

print(maxEle-minEle)