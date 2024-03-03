#26
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        num = []
        for i in range(0,len(nums)):
            if nums[i] not in num:
                num.append(nums[i])
                k+=1

        return len(num)

soln = Solution()
duplicates = [0,0,1,1,1,2,2,3,3,4]
print(soln.removeDuplicates(duplicates))
