# https://leetcode.com/problems/move-zeroes/description/

from collections import deque

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        q = deque()

        for idx, num in enumerate(nums):
            if num == 0:
                q.append(idx)

            elif num != 0 and q:
                nums[q[0]] = num
                nums[idx] = 0
                q.popleft()
                q.append(idx)
