class Solution:

    delim = 'Ы'

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + self.delim + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != self.delim:
                j += 1 
            count = int(s[i:j])
            res.append(s[j+1:j+1+count])
            i = j+1+count
        return res