class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_nums = []
        for i in range(0,len(nums)):
            if val != nums[i]:
                new_nums.append(nums[i])
        return new_nums

soln = Solution()
nums = [0,1,2,2,3,0,4,2]
print(soln.removeElement(nums,2))


# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         while val in nums:
#             nums.remove(val)
#         return len(nums)