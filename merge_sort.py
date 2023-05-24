# Implement a merge sort for a list of integers. Your solution must run in O(n*logn) time for a list of length n.

# Input: unsorted list of integer values, e.g., [1, 9, -32, 4]
# Output: sorted list of integer values, e.g., [-32, 1, 4, 9]

# The starter code contains the scaffolding for a working merge sort algorithm. 
# It recursively divides the list then puts it back together, but all of the 
# sorting-specific logic is missing.


def mergeSort(inputList):
    # Calculate length of input list
    length = len(inputList)
    # Base case for recursion (infinite loop without this!) stop when length of list is 1
    if length <= 1:
        return inputList

    print(f'mergeSort called with a list of length {length}: {inputList}')

    # When the length of input list is greater than 1, the function divides the list

    # Get the middle index
    middleIndex = length // 2 # floor division
    # Divide input list into two sublists left and right
    left = inputList[:middleIndex] # left : elements from index 0 to mid index
    right = inputList[middleIndex:] # right : elements from mi index to end of list

    # Recursively call the function for left and right sublists until base case is raeched
    left = mergeSort(left) # repeat process for left sublist
    right = mergeSort(right) # repeat process for right sublist
    # Merge the sorted sublists
    return list(merge(left, right))


def merge(left, right): # lists
    # Initialize an empty sorted list to store the sorted elements
    sorted_list = []
    # define pointers for each list
    i = 0 # pointer to keep track of index in left list
    j = 0 # pointer to keep track of index in right list

    # The while loop iterates as long as both pointers are within the bounds of
    # their respective sublists
    while i < len(left) and j < len(right):
        # at each step, compare the next values from left & right
        # Choose the lowest of the two values to append to the result list 
        if left [i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # If the lists are different length, we may need to also transfer over 
    # the additional elements from the longer list.
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Test cases:
unsortedList = [1, 97, 36, -4, 0, 124, 3000]
print(mergeSort(unsortedList)) # -4, 0, 1, 36, 97, 124, 3000