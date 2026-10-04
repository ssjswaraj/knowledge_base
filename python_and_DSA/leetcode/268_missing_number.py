#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        sm_need = 0
        sm_og = 0

        for i in nums:
            sm_og += i

        for i in range(mn, mx + 1, 1):
            sm_need += i

        if sm_need == sm_og and mn == 0:
            return mx + 1

        elif sm_need == sm_og and mn != 0:
            return 0

        else:
            return sm_need - sm_og
