class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        rm, lm = 0, 0
        res = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > lm:
                    lm = height[l]
                else:
                    res += lm - height[l]
                l += 1
                continue
            if height[r] > rm:
                rm = height[r]
            else:
                res += rm - height[r]
            r -= 1

        return res
