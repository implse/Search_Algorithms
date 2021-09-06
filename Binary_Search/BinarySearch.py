# Binary Search : Time Complexity O(log n)

# Recursive Binary Search
def binary_search_recursive(sorted_list, target_value, low, high):
    if high >= low:
        # Avoid overflow for mid index
        mid = low + (high - low) // 2
        if sorted_list[mid] == target_value:
            # return the index of the target value
            return mid
            # return "Value {} found at index: {}".format(target_value, mid)
        elif sorted_list[mid] > target_value:
            return binary_search_recursive(sorted_list, target_value, low, mid - 1)
        else:
            return binary_search_recursive(sorted_list, target_value, mid + 1, high)
    else:
        return -1

# Iterative Binary Search
def binary_search_iterative(sorted_list, target_value, low, high):
    while low <= high:
        # Avoid overflow for mid index
        mid = low + (high - low) // 2
        if sorted_list[mid] == target_value:
            # return the index of the target value
            return mid
            # return "Value {} found at index: {}".format(target_value, mid)
        elif sorted_list[mid] < target_value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
