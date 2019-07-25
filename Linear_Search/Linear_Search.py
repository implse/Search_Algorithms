# Linear Search or Sequential Search : Time Complexity O(n)

# Unordered Linear Search
def unordered_linear_search(arr, target_value):
    for i in range(len(arr)):
        if arr[i] == target_value:
            return i
    return -1

# Sorted Linear Search
def ordered_linear_search(arr, target_value):
    for i in range(len(arr)):
        if arr[i] == target_value:
            return i
        elif arr[i] > target_value:
            return -1
    return -1
