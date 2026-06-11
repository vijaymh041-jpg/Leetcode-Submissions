# Last updated: 6/12/2026, 12:45:13 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ' '.join(s.split())
        list1=split(s)
        return len(list1[-1])

        