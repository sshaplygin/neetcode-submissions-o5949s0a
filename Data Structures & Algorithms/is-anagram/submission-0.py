class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        nums = [0 for i in range(26)]

        for ch in s:
            nums[ord(ch) - ord('a')] += 1
    
        for ch in t:
            nums[ord(ch) - ord('a')] -= 1

        for num in nums:
            if num != 0:
                return False

        return True