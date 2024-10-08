def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
isPalindrome = True
i = 0
j = l-1

while i<j :
    if not L[i]==L[j]:
        isPalindrome = False
        break
    i+=1
    j-=1

if isPalindrome:
    print("Yes")
else :
    print("No")
    

