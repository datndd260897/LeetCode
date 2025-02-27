# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k 
# and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
from typing import List, Dict

class Solution:
    def __init__(self):
        pass
        
    def maxOperations(self, nums: List[int], k: int) -> int:
        count: int = 0
        nums_map: Dict[int, int] = {}
        for value in nums:
            if nums_map.get(value):
                nums_map[value] += 1
            else:
                nums_map[value] = 1

        for value in nums:
            value2 = k - value
            if nums_map.get(value2):
                nums_map[value2] -= 1
                nums_map[value] -= 1
                if nums_map[value] >= 0 and nums_map[value2] >= 0:
                    count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    nums, k = [3,1,3,4,3], 6
    print(solution.maxOperations(nums, k))

    
