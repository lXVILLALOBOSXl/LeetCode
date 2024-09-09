class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s or len(s) < 1:
            return None
        
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            if not self.is_vowel(s_list[left]):
                left += 1
            elif not self.is_vowel(s_list[right]):
                right -= 1
            else:
                self.swap(s_list, left, right)
                left += 1
                right -= 1
        
        return ''.join(s_list)

    def swap(self, s_list: list, i: int, j: int) -> None:
        aux = s_list[i]
        s_list[i] = s_list[j]
        s_list[j] = aux

    def is_vowel(self, letter: str) -> bool:
        return letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


# Test cases
s = Solution()
print(s.reverseVowels("hello")) # Expected "holle"
print(s.reverseVowels("leetcode")) # Expected "leotcede"
print(s.reverseVowels("aA")) # Expected "Aa"
print(s.reverseVowels(None))
print(s.reverseVowels(""))