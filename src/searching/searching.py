# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return -1
    else:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            # recurse 
            return binary_search(arr, target, start, mid - 1)
        
        elif target > arr[mid]:
            return  binary_search(arr, target, mid + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

