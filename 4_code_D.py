#You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array. 

#Input:
#An integer array arr of size n.
#Example : 
#arr = [16, 17, 4, 3, 5, 2]

def find_leaders(arr):
    n = len(arr)
    leaders = []
    
    # Start from the last element, it's always a leader
    current_leader = arr[-1]
    leaders.append(current_leader)
    
    # Traverse the array from right to left
    for i in range(n-2, -1, -1):
        if arr[i] > current_leader:
            current_leader = arr[i]
            leaders.append(current_leader)
    
    # Since we collected leaders from right to left, reverse the list before returning
    return leaders[::-1]

# Test cases
print(find_leaders([16, 17, 4, 3, 5, 2])) 
print(find_leaders([1, 2, 3, 4, 0])) 
print(find_leaders([7, 10, 4, 10, 6, 5, 2])) 
print(find_leaders([5])) 
print(find_leaders([100, 50, 20, 10])) 
print(find_leaders(list(range(1, 1000001)))) 
