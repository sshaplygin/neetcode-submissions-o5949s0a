class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        count = 0
        zeroIdx = -1
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
                zeroIdx = i
                if count > 1:
                    return [0] * len(nums)
                continue
            p *= num
        if zeroIdx != -1:
            res = [0] * len(nums)
            res[zeroIdx] = p
            return res

        res = []
        for num in nums:
            res.append(p//num)
        return res
