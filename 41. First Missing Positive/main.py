from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 1
        
        n = len(nums)
        contains_one = 0
        # From 1 to n + 1 are the numbers are the minum possible positive integers
        
        for i in range(n):
        #1) Change not important values (values > n) or (values < 1) to 1's
            if nums[i] == 1:
                contains_one = 1
            elif nums[i] > n or nums[i] < 1:
                nums[i] = 1

        if contains_one == 0:
            return 1

        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0: 
                nums[index] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1
            
        return n + 1

        


# Test cases
s = Solution()
print(s.firstMissingPositive([3,4,-1,1]))
