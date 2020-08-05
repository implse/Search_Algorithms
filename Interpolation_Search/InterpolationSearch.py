# Interpolation Search Iterative
def interpolation_search_iterative(lst, target):
    low = 0
    high = len(lst) - 1
    while lst[low] <= target and lst[high] >= target:
        position  = low + int(((float(high - low) / ( lst[high] - lst[low])) * ( target - lst[low])))
        if lst[position] < target:
            low = position + 1
        elif lst[position] > target:
            high = position - 1
        else:
            return position
    if lst[low] == target:
        return low
    return None

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
print(interpolation_search_iterative(arr, 21))
