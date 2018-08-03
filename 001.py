# Two Sum - Medium - Accepted
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # version-1, 5860ms, beats 7.15% python submissions
#        for i in range(len(nums)):
#            for j in range(i+1,len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i+1,j+1]
                
        # version-2, 5256ms, beats 13.38% python submissions        
#        for i in range(len(nums)):
#            a = nums[i]
#            for j in range(i+1,len(nums)):
#                if a + nums[j] == target:
#                    return [i+1,j+1]

        # version-3, 5188ms, beats 13.52% python submissions
#        l = len(nums)
#        for i in range(l):
#            a = nums[i]
#            for j in range(i+1,l):
#                if a + nums[j] == target:
#                    return [i+1,j+1]

        l = len(nums)
        for i in range(l):
            a = target - nums[i]
            if a in nums:
                j = nums.index(a)
                if i < j:
                    return [i+1,j+1] 
                elif i > j:
                    return [j+1,i+1]
