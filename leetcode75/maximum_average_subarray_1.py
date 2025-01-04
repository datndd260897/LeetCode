# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
from typing import List

class Solution:
    def __init__(self):
        pass

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """_summary_

        Args:
            nums (List[int]): _description_
            k (int): _description_

        Returns:
            float: _description_
        """
        max_average: float = 0
        index = 0
        while index + k <= len(nums):
            current_total = 0
            for j_index in range(k):
                current_total += nums[index + j_index]
            current_average = current_total / k
            if index == 0:
                max_average = current_average
            max_average = float(current_average if current_average > max_average else max_average)
            index += 1
            
        return max_average
    
    def findMaxAverage_slide_window(self, nums: List[int], k: int) -> float:
        """_summary_

        Args:
            nums (List[int]): _description_
            k (int): _description_

        Returns:
            float: _description_
        """
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_sum = max(current_sum, max_sum)

        return max_sum/k

if __name__ == "__main__":
    solution = Solution()
    nums, k = [1,12,-5,-6,50,3], 4
    print(solution.findMaxAverage(nums, k))
    print(solution.findMaxAverage_slide_window(nums, k))