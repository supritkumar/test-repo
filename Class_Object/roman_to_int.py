from typing import SupportsInt

class Solution:
    def romanToInt(self, s: str) -> int:
       roman_dict = { "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} 
       self.s=s
       int_value = 0
       if "IV" in self.s : self.s= self.s.replace("IV","IIII")
       if "IX" in self.s : self.s= self.s.replace("IX","VIIII")
       if "XL" in self.s : self.s= self.s.replace("XL","XXXX")
       if "XC" in self.s : self.s= self.s.replace("XC","LXXXX")
       if "CD" in self.s : self.s= self.s.replace("CD","CCCC")
       if "CM" in self.s : self.s= self.s.replace("CM","DCCCC")

       for i in self.s:
           int_value = int_value + roman_dict[i]

       return int_value
    
roman_number = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(roman_number))