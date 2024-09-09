#Problem: Sort an Array of 0s, 1s, and 2s
#You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space. This means you need to rearrange the array in-place.

#Input :
#An integer array arr of size n where each element is either 0, 1, or 2.
#Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

#Output :
#The sorted array, arranged in increasing order of 0s, 1s, and 2s.
#Example: [0, 0, 0, 1, 1, 1, 2, 2] 

def sort_arrays(arr):
    """
    low represents the position for 0's
    mid is used to traverse through the elements
    high represents the position for 2's
    """
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:  # Traversing through the array
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    sorted_arr = sort_arrays(arr)
    print("Sorted Array:", sorted_arr)
