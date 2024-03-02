class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in range(len(s)-1):
            value = romans_to_int[s[i]]
            next_value = romans_to_int[s[i+1]]
            if value<next_value:
                sum-=value
            else:
                sum +=value
        sum +=romans_to_int[s[-1]]
        return sum
