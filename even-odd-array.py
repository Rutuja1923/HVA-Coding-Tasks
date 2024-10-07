def find_len(lst):
    count=0
    while lst:
        count+=1
        lst = lst[1:]
    return count

print("Enter List Elements :")
L = list(map(int,input().split()))
i = 0
length = find_len(L)
while i<length:
    if L[i]%2 == 0:
        print("Even")
    else:
        print("Odd")
    i+=1