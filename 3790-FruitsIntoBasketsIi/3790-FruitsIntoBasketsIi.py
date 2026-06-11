# Last updated: 6/12/2026, 12:44:55 AM
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        used = [False] * n  
        unplaced_count = 0
        
        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True  
                    placed = True
                    break
            if not placed:
                unplaced_count += 1
        
        return unplaced_count

fru = [4, 2, 5]
bas = [3, 5, 4]
sol = Solution()
print(sol.numOfUnplacedFruits(fru, bas))