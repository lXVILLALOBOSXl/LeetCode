from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index
                
        return index
    
# Test
s = Solution()
print(s.twoSum([3, 2, 4], 6)) # [1, 2]

