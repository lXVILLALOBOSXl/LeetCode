class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) < 1: 
            return 0
        
        i, j, max = 0, 0, 0
        sub_string = set()
        
        while i < len(s):
            char = s[i]
            while char in sub_string:
                sub_string.remove(s[j])
                j+=1
            sub_string.add(char)
            max = max if max > (i - j + 1) else (i - j + 1)
            i+=1


        return max
        

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew")) # expected 3
print(s.lengthOfLongestSubstring("aab")) # Expected 2
print(s.lengthOfLongestSubstring("abcabcbb")) # expected 3
print(s.lengthOfLongestSubstring("bbbbb")) # expected 1
print(s.lengthOfLongestSubstring("")) # expected 0
print(s.lengthOfLongestSubstring("dvdf")) # Expected 3
print(s.lengthOfLongestSubstring(None)) # Expected 0
