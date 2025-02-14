# Find Kth Largest Element in an Array 

def find_kth_largest(nums: list, k: int) -> int:
    if k > len(nums):
        print("Value of k is greater than array length")
        exit()
    else:
        nums.sort()
        return nums[-k]

nums = [3, 2, 1, 5, 6, 4] 
k = 2
print(find_kth_largest(nums, k)) # Output: 5