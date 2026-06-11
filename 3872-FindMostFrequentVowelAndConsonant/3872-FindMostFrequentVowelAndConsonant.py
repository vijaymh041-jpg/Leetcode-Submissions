# Last updated: 6/12/2026, 12:44:53 AM
class Solution(object):
    def maxFreqSum(self, s):
        vowels='aeiou'
        d=Counter(s)
        c=0
        v=0
        for i in s:
            if i in vowels:
                v=max(v, d[i])
            else:
                c=max(c, d[i])
        return c+v
        
        
        
        
        