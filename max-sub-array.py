def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count

#using recursion

def longest_increasing_subarray(arr, n, prev_val=None, length=1, max_length=1):
    if n == 0:                          #base case
        return max_length
    
    if prev_val is None:                #previous value - first element of subarray
        prev_val = arr[n-1]

    if arr[n-1] > prev_val:             #check if previous element is smaller than current element
        length += 1
        if length > max_length:
            max_length = length         # update value of max-length
    else:                               # Reset length since it's not increasing
        length = 1  

    prev_val = arr[n-1]
    
    return longest_increasing_subarray(arr, n-1, prev_val, length, max_length)

print("Enter array elements :")
L=list(map(int,input().split()))
n = find_len(L)
longest_length = longest_increasing_subarray(L, n)
print(longest_length)