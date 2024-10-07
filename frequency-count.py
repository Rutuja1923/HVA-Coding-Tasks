def find_len(lst):
    count=0
    while lst:
        count+=1
        lst = lst[1:]
    return count


print("Enter List Elements :")
lst = list(map(int,input().split()))
x = int(input("Enter the number : "))
length = find_len(lst)

i = 0
freq = 0
while i<length:
    if lst[i] == x:
        freq+=1
    i+=1
print(freq)