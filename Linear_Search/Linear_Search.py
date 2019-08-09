# Linear Search or Sequential Search : Time Complexity O(n)

# Linear Search - Unordered Input list
def linear_search_unordered(search_list, target_value):
    for i in range(len(search_list)):
        if search_list[i] == target_value:
            return i
    return -1

# Linear Search - Sorted Input list
def linear_search_ordered(search_list, target_value):
    for i in range(len(search_list)):
        if search_list[i] == target_value:
            return i
        elif search_list[i] > target_value:
            return -1
    return -1

# Linear Search - Find Duplicates
def find_duplicates(search_list, target_value):
    matches = list()
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
    if len(matches) > 0:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))

# Linear Search - Find Maximum Value
def find_maximum(search_list):
    maximum_value_index = None
    for idx in range(len(search_list)):
        if maximum_value_index is None:
            maximum_value_index = idx
        elif search_list[idx] > search_list[maximum_value_index]:
            maximum_value_index = idx
    return maximum_value_index
