def get_all_pair_diff_sum(arr):
    i = 0
    dSum = 0
    while i < len(arr) :
        j = i+1
        while j < len(arr) :
            dSum += abs(arr[i] - arr[j])
            j += 1
        i += 1
    return dSum

L=list(map(int, input().split()))
print(get_all_pair_diff_sum(L))

