#Problem: Find the missing number
#You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

#Input :
#An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
#Example : arr = [1, 2, 4, 5]

#Output :
#Return the missing integer from the array.
#Example: Missing Number : 3

def find_missing_number(arr):
   
    n = len(arr) + 1
    
    expected_sum = n * (n + 1) // 2
    
    actual_sum = sum(arr)
    
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usages
arr = [1, 2, 4, 5]
print(find_missing_number(arr))  

arr = [2, 3, 4, 5]
print(find_missing_number(arr))  

arr = [1, 2, 3, 4]
print(find_missing_number(arr))  