class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()
        ans = ""
        i = 0
        first,last = strs[0],strs[-1]
        while i<min(len(first),len(last)):
            if first[i] ==last[i]:
                ans +=first[i]
            else:
                return ans
            i+=1

        return ans


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""