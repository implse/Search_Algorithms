# Search Algorithm

Searching is the process of finding an item with specified properties from a collection of items.

## Linear Search

Linear search sequentially checks each element of the list until it finds an element that matches the searching value.

#### Unordered Linear Search

Let us assume we are given an array where the order of the elements is not known. That means the elements of
the array are not sorted. In this case, to search for an element we have to scan the complete array and see if the
element is in the given array or not.

#### Sorted / Ordered Linear Search

If the elements of the array are already sorted, then in many cases we don't have to scan the complete array to
see if the element is there in the given array or not.

If the value arr[-1] is greater than the data to be searched, then we just return -1 without searching the remaining array.

__Time Complexity : O(n)__

Linear search is rarely used practically because other search algorithms such as the binary search and hash tables allow significantly faster searching comparison to Linear search.

## Binary Search

Search a sorted array by repeatedly dividing the search interval in half.

Begin with an interval covering the whole array.

If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.

Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

__Time Complexity :  O(log n)__
