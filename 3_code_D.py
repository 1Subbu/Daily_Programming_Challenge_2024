#Problem: Find the duplicate number
#You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive. There is exactly one duplicate number in the array, but it may appear more than once. Your task is to find the duplicate number without modifying the array and using constant extra space.
#Input :
#An integer array arr of size n+1, where each element is an integer in the range [1, n].
#Example : arr = [3, 1, 3, 4, 2]

#Output :
#Return the duplicate integer present in the array.
#Example: Duplicate Number : 3

def findDuplicate(arr):
   
    tortoise = arr[0]
    hare = arr[0]
    
    while True:
        tortoise = arr[tortoise]        
        hare = arr[arr[hare]]           
        if tortoise == hare:            
            break
    
    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    
   
    return tortoise


print(findDuplicate([1, 3, 4, 2, 2])) 
print(findDuplicate([3, 1, 3, 4, 2])) 
print(findDuplicate([1, 1]))           
print(findDuplicate([1, 4, 4, 2, 3]))  
