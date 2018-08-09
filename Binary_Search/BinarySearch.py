# Binary Search : Time Complexity O(log n)

# Recursive Binary Search
def binary_search_recursive(arr, value_to_search, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == value_to_search:
            return mid
            # return "Value {} found at index: {}".format(value_to_search, mid)
        elif arr[mid] > value_to_search:
            return binary_search_recursive(arr, value_to_search, low, mid - 1)
        else:
            return binary_search_recursive(arr, value_to_search, mid + 1, high)
    else:
        return -1

# Iterative Binary Search
def binary_search_iterative(arr, value_to_search, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == value_to_search:
            return mid
            # return "Value {} found at index: {}".format(value_to_search, mid)
        elif arr[mid] < value_to_search:
            low = mid + 1
        else:
            high = mid - 1
    return -1
