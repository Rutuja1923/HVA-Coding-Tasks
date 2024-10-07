def find_len(lst):
    count=0
    while lst:
        count+=1
        lst = lst[1:]
    return count

print("Enter List Elements :")
L = list(map(int,input().split()))
l = find_len(L)
i = 0
odd_count = 0
while i<l:
    if not L[i]%2 == 0:
        odd_count+=1
    i+=1
print(odd_count)