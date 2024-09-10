class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:
            return None
        
        roman = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        roman_number = ""

        for key in roman:
            greatest_value = int(num / roman.get(key))
            if greatest_value > 0:
                for i in range(greatest_value):
                    roman_number += key
            num %= roman.get(key)
            if num == 0:
                break


        return roman_number

# Test cases
s = Solution()
print(s.intToRoman(2944)) # "MMCMXLIV"
print(s.intToRoman(3)) # "III"
print(s.intToRoman(4)) # "IV"
print(s.intToRoman(9)) # "IX"
print(s.intToRoman(58)) # "LVIII"
print(s.intToRoman(1994)) # "MCMXCIV"
print(s.intToRoman(3999)) # "MMMCMXCIX"
print(s.intToRoman(0)) # None
print(s.intToRoman(4000)) # None
print(s.intToRoman(1)) # "I"