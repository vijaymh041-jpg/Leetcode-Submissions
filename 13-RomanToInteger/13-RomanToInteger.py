# Last updated: 6/12/2026, 12:45:16 AM
class Solution(object):
    
    def romanToInt(self,s):
        rom = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        sum= 0
        n=len(s)
        for i in range(n):
            cvalue=rom[s[i]]
            if i+1 < n and rom[s[i+1]] > cvalue:
                sum -= cvalue
            else:
                sum += cvalue
        return sum


sol=Solution()
inp="III"
print(sol.romanToInt(inp))      