def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count
print("Enter array elements :")
L=list(map(int,input().split()))
l = find_len(L)
maxSum=L[0] + L[1]
i=2
while i<l-1:
    currSum = L[i] + L[i-1]
    if currSum >=maxSum :
        maxSum=currSum
    i+=1
print(maxSum)
