# Find the Missing Number in an Array 

def find_missing_number(arr: list) -> int:
    set_arr = set(arr)
    for i in range(len(arr) + 1):
        if i not in set_arr:
            return i

arr = [3, 0, 1] 
print(find_missing_number(arr))   #Output: 2 
