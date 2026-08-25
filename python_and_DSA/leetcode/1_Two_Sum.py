# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for idx, num in enumerate(nums):
            
            remain = target-num
            if remain in dict.keys():
                num_2 = dict[remain]
                num_1=idx
                return num_1, num_2
            dict[num]=idx
