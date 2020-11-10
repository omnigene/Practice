# Problem:
# You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements.
# You need to find the minimum number of swaps required to sort the array in ascending order.

# Explanation:
# Given array arr:[4,3,1,2]
# After swapping (0,2) we get arr:[1,3,4,2]
# After swapping (1,2) we get arr:[1,4,3,2]
# After swapping (1,3) we get arr:[1,2,3,4]
# So, we need a minimum of 3 swaps to sort the array in ascending order.

def minimumSwaps(arr):
    arr_ref={}
    for j in range(len(arr)):
        arr_ref[arr[j]]=j
    swaps=0
    for i,n in enumerate(arr):
        if n!=i+1:
            arr[arr_ref[i+1]]=n
            arr_ref[n]=arr_ref[i+1]
            arr[i]=i+1
            swaps+=1
    return swaps

a=[3,7,6,9,1,8,10,4,2,5]
print(minimumSwaps(a))