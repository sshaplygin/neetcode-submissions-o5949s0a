import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        l, r = 0, 0
        max_l, max_c = 0, 0

        while r < len(s):
            ch = s[r]
            chars[ord(ch) - ord('A')] += 1
            max_c = max(max_c, chars[ord(ch) - ord('A')])

            while r - l + 1 - max_c > k:
                chars[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_l = max(max_l, r - l + 1)
            r +=1 

        return max_l
