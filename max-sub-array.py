def longist_increasing_subarray(arr) :
    if not arr :
        return 0
    
    curr_len = 1
    max_len = 1

    for i in range(1, len(arr)) :
        if arr[i] > arr[i-1] :
            curr_len += 1
            max_len = max(max_len, curr_len)
        
        else :
            curr_len = 1
        
    return max_len

L = list(map(int, input().split()))

print(longist_increasing_subarray(L))