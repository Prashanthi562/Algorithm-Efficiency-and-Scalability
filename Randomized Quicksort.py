## Description:Randomized Quicksort algorithm is one of the powerful approaches towards sorting data in arrays through a randomized selection of a single element that comes to be known as the pivot element. Such randomization process supports a great variety of input situations the empty array, the sorted array, the reverse-sorted array, and also the array whose elements are the duplicated elements.
    
import random

# Choosing a random pivot index between low and high
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    
    # Swapping the randomly chosen pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Storing the pivot value
    pivot = arr[high]
    
    # Initializing the pointer for smaller elements
    i = low - 1

    # Iterating through the array from low to high - 1
    for j in range(low, high):
        # Comparing current element with pivot
        if arr[j] <= pivot:
            i += 1
            # Swapping current element to the correct position
            arr[i], arr[j] = arr[j], arr[i]

    # Placing the pivot in its correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    # Returning the final position of the pivot
    return i + 1

# Sorting the array using randomized quicksort method
def randomized_quicksort(arr, low, high):
    # Checking if the current segment has more than one element
    if low < high:
        # Getting the pivot index after partitioning
        pi = randomized_partition(arr, low, high)
        
        # Recursively sorting the left part
        randomized_quicksort(arr, low, pi - 1)
        
        # Recursively sorting the right part
        randomized_quicksort(arr, pi + 1, high)

# Running test cases to check sorting on different types of arrays
if __name__ == "__main__":
    test_cases = [
        [],              # Handling an empty array
        [1],             # Handling a single element array
        [5, 3, 8, 4, 2, 7, 6, 1],  # Sorting a random array
        [1, 2, 3, 4, 5],          # Sorting an already sorted array
        [5, 4, 3, 2, 1],          # Sorting a reverse-sorted array
        [2, 3, 2, 3, 2]           # Sorting an array with repeated elements
    ]

    for case in test_cases:
        # Making a copy of the original array
        arr_copy = case.copy()
        
        # Sorting the copied array
        randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
        
        # Printing the original and sorted arrays
        print("Original:", case)
        print("Sorted  :", arr_copy)
        print()
