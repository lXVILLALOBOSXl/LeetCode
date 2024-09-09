class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while(x != 0):
            remainder = x % 10
            result = result * 10 + remainder
            if result < -2**31 or result > 2**31 - 1:
                return 0
            x = int(x / 10)

        return sign * result

# Test cases
s = Solution()
print(s.reverse(123)) # Expected 321
print(s.reverse(-123)) # Expected -321
print(s.reverse(120)) # Expected 21
print(s.reverse(0)) # Expected 0
print(s.reverse(1534236469)) # Expected 0
print(s.reverse(-1563847412)) # Expected 0
print(s.reverse(None)) # Expected 0