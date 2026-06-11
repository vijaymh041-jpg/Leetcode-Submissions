# Last updated: 6/12/2026, 12:45:17 AM
class Solution(object):
    def isPalindrome(self, x):
        y =str(x)
        n=len(y)
        
        if x < 0:
            return False
        else:
            for i in range(0,n):
                case = True
                if i==n/2:
                    return True

                if y[i]==y[n-i-1]:
                    case = True
                else:
                    return False


p=121
sol=Solution()
print(sol.isPalindrome(p))
