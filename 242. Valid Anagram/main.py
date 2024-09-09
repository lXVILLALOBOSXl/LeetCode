class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_chars_s = {}
        unique_chars_t = {}
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
            return False

        for letter in s:
            if unique_chars_s.get(letter):
                unique_chars_s[letter] += 1
            else:
                unique_chars_s[letter] = 1

        for letter in t:
            if unique_chars_t.get(letter):
                unique_chars_t[letter] += 1
            else:
                unique_chars_t[letter] = 1

        for item in unique_chars_s:
            if item not in unique_chars_t or unique_chars_s[item] != unique_chars_t[item]:
                return False
        
        return True
        
# test cases
s = Solution()
print(s.isAnagram("anagram", "nagaram")) # Expected True
print(s.isAnagram("rat", "car")) # Expected False
print(s.isAnagram("a", "ab")) # Expected False
print(s.isAnagram("ab", "a")) # Expected False
print(s.isAnagram("ab", "ba")) # Expected True
print(s.isAnagram("a", "a")) # Expected True
print(s.isAnagram("a", "b")) # Expected False
print(s.isAnagram("a", "a")) # Expected True
