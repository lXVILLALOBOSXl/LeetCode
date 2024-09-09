from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        
        duplicates = []
        n = len(nums)

        for i in range(n):
            index  = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicates.append(abs(nums[i]))
                continue
            nums[index] *= -1

        return duplicates

# Test cases
s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1])) # Expected [2,3]
print(s.findDuplicates([1,1,2])) # Expected [1]
print(s.findDuplicates([1])) # Expected []
print(s.findDuplicates([])) # Expected None
print(s.findDuplicates([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100])) # Expected []