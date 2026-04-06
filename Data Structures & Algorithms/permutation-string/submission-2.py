from string import ascii_lowercase

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        ds1 = dict()
        ds2 = dict()
        for ch in s1:
            ds1[ch] = ds1.get(ch, 0) + 1
        for ch in s2[:len(s1)]:
            ds2[ch] = ds2.get(ch, 0) + 1

        matches = 0
        for ch in ascii_lowercase:
            matches += (1 if ds1.get(ch, 0) == ds2.get(ch, 0) else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            ch = s2[r]
            ds2[ch] = ds2.get(ch, 0) + 1 
            if ds1.get(ch, 0) == ds2.get(ch, 0):
                matches +=1 
            elif ds1.get(ch, 0) + 1 == ds2.get(ch, 0):
                matches -= 1

            ch = s2[l]
            ds2[ch] -= 1
            if ds1.get(ch, 0) == ds2.get(ch, 0):
                matches +=1 
            elif ds1.get(ch, 0) - 1 == ds2.get(ch, 0):
                matches -= 1
            l += 1
        return matches == 26