def get_all_pair_with_sum(arr, s):
    i = 0
    while i < len(arr) :
        j = i+1
        while j < len(arr) :
            cSum = arr[i] + arr[j]
            if cSum == s :
                print(arr[i],arr[j])
            j += 1
        i += 1

L = list(map(int, input().split()))
s = int(input())  
get_all_pair_with_sum(L,s)

