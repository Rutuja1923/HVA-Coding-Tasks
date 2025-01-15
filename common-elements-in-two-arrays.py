def get_common_elements(n,arr1,arr2) :

    common = []

    for i in range(0,n) :
        if arr1[i] in arr2 and arr1[i] not in common :
            common.append(arr1[i])
            
    return common

n = int(input())
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))

result = get_common_elements(n,L1,L2)
if result :
    for e in result :
        print(e, end = ' ')
else :
    print("No")
