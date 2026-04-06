class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        counter = [0 for _ in range(26)]
        for st in strs:
            for ch in st:
                counter[ord(ch) - ord('a')] += 1
            words[tuple(counter)].append(st)
            for i in range(len(counter)):
                counter[i] = 0
        return list(words.values())