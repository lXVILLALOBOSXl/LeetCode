class Solution:
     def firstUniqChar(self, s: str) -> int:
          unique_chars = {}

          for letter in s:
               unique_chars[letter] = 0

          for letter in s:
               unique_chars[letter] += 1

          for i in range(len(s)):
                if unique_chars[s[i]] == 1:
                      return i
            
          return -1

     

# Test cases
s = Solution()
print(s.firstUniqChar("leetcode")) # Expected 0
print(s.firstUniqChar("loveleetcode")) # Expected 2
print(s.firstUniqChar("aabb")) # Expected -1
print(s.firstUniqChar("z")) # Expected 0
print(s.firstUniqChar("aadadaad")) # Expected -1
print(s.firstUniqChar("dddccdbba")) # Expected 8
print(s.firstUniqChar("dddccdbba")) # Expected 8
