# Last updated: 6/12/2026, 12:45:00 AM
class Solution(object):
    def doesAliceWin(self, s):
        v=['a','e','i','o','u']
        x=sum(1 for i in s if i in v)
        if x==0:
            return False
        elif x%2==0:
            return True
        else:
            return True
        
        