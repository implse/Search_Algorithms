# Search Algorithms

Searching is the process of finding an item with specified properties from a collection of items.


## Searching Techniques

- Sequential search

- Interval seach

## Linear Search

`Linear search` or `sequential search` sequentially checks each `element` of the list until it finds an `element` that matches the `searching value`.

### Unordered Linear Search

Let us assume we are given a `list` where the order of the elements is not known. That means the `elements` of
the `list` are not sorted. In this case, to search for an element we have to scan the complete `list` and see if the
`element` is in the given `list` or not.

### Sorted / Ordered Linear Search

If the `elements` of the list are already sorted, then in many cases we don't have to scan the complete `list` to
see if the element is in the given `list` or not.

- If the `value` `arr[-1]` is greater than the `value` to be searched, then we just return `-1` without searching the remaining `list`.

- At each iteration, if the `value` `arr[-i]` is greater than the `value` to be searched, then we just return `-1` without searching the remaining `list`.

__Time Complexity:__ `O(n)`

`Linear search` is rarely used practically because other `search algorithms` such as the `binary search` and `hash tables` allow significantly faster searching comparison to `Linear search`.

## Binary Search

`Binary search` is used to search an `value` in a `sorted list` of elements by repeatedly dividing the search interval in `half`.

`Binary search` works by comparing the `value` to search for with the `middle value` of the `sorted list`.

- It begin with an `interval` covering the whole `list` of elements, getting the `middle value`. (it splits list by two halves).

- Check if the `middle value` is equal to the `value` we’re searching for.

- If the value is higher than the `middle value`, then the search proceeds in the `right half` of the `list`.

- If the value is lower than the `middle value`, then the search proceeds in the `left half` of the `list`.

- This process is repeated comparing the `searching value` and the `middle value` until the `value` is found or the `interval` is empty then in this case the `searching value` is not in the `list`.

The `binary search` pattern is based on the `divide and conquer` algorithm technique.

`binary search` reduces the search complexity to `O(log(n))`.

The algorithm may be implemented in different ways using `iterative` or `recursive` approach.

The number of possible divisions is proportional to the power of two that will give us the total
number of elements in the list.

If the `sorted list` contain 10 000 elements then number of possible divisions is `log2(10 000) = 13.28`.

__Time Complexity:__ `O(log(n))`

note : A `binary search tree` is a `binary tree` data structure that works based on the principle of `binary search`.
