class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVals = {}
        for i, curr in enumerate(nums):
            val = target - curr 
            if val in prevVals:
                return [prevVals[val], i]
            prevVals[curr] = i
        return []