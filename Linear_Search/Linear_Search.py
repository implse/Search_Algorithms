# Linear Search or Sequential Search : Time Complexity O(n)

# Unordered Linear Search
def unordered_linear_search(arr, value_to_search):
    for i in range(len(arr)):
        if arr[i] == value_to_search:
            return i
    return -1

# Test1
a = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(unordered_linear_search(a, 277))

# Sorted Linear Search
def ordered_linear_search(arr, value_to_search):
    for i in range(len(arr)):
        if arr[i] == value_to_search:
            return i
        elif arr[i] > value_to_search:
            return -1
    return -1
