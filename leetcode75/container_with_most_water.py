# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) 
# and (i, height[i]).

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

from typing import List


class Solution:
    def __init__(self):
        pass

    def maxArea_bruteforce(self, height: List[int]) -> int:
        """_summary_

        Args:
            height (List[int]): _description_

        Returns:
            int: maxArea
        """
        max_area : int = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if not i == j:
                    area = abs(i - j) * min(height[i], height[j])
                    max_area = max_area if max_area > area else area
        return max_area


if __name__ == "__main__":
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    expected_result = 49
    print(solution.maxArea_bruteforce(height) == expected_result)