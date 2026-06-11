# Last updated: 6/12/2026, 12:44:58 AM
class Solution(object):
    def countOdds(self, low, high):
        count=(high+1)//2 - low//2
        return count