class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        charsS = set()
        while r < len(s):
            ch = s[r]
            while ch in charsS:
                charsS.remove(s[l])
                l += 1
            
            charsS.add(ch)

            res = max(res, len(charsS))
            r += 1
            
        return res