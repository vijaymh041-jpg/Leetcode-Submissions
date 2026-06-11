# Last updated: 6/12/2026, 12:45:19 AM
class Solution(object):
    def twoSum(self, nums, target):
        list1=[]
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    list1.append([i,j])
                    return list1[0]

        