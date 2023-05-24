# Merge Sort Algorithm

This repository contains a Python implementation of the Merge Sort algorithm. Merge Sort is a divide-and-conquer sorting algorithm that recursively divides the input list into smaller sublists, sorts them, and then merges them to obtain the final sorted list.


## Requirements

- Python 3 installed locally.

## Implementation

The algorithm is implemented in the mergeSort function, which takes an input list as a parameter and returns the sorted list. The function uses recursion to divide the list into two sublists, performs merge sort on each sublist, and then merges the sorted sublists.

The merge function is used internally by mergeSort to merge two sorted sublists into a single sorted list. It compares the elements from both sublists and appends the smaller element to the sorted list.

## Usage

To use the Merge Sort algorithm, simply call the mergeSort function with your input list. For example:

```
input_list = [1, 97, 36, -4, 0, 124, 3000]
sorted_list = mergeSort(input_list)
print(sorted_list)
```
This will output the sorted list: [-4, 0, 1, 36, 97, 124, 3000].


## Credits

This code was created as part of a data structures and algorithms course at BloomTech.
