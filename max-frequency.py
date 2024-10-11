def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count
    
print("Enter array elements :")
L=list(map(int,input().split()))
l = find_len(L)

i=0
maxCount = 0
ind=0

while i<l:
    j=0
    currCount=0
    while j<l:
        if L[i]==L[j]:
            currCount+=1
        j+=1
    if currCount>maxCount:
        maxCount=currCount
        ind=i
    i+=1

print(L[ind],maxCount)
