from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass

# Test cases
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(s.topKFrequent([1], 1)) # [1]
print(s.topKFrequent([1,2], 2)) # [1,2]