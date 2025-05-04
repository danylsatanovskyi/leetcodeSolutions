class Solution(object):
    def twoSum(self, nums, target):
        rests = {}
        for idx, num in enumerate(nums):
            needed = target - num
            if needed in rests:
                return [idx, rests[needed][1]]
            rests[num] = (needed, idx)
