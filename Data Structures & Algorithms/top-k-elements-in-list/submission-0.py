class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for n in nums:
            c[n] += 1
        
        vals = []
        for key in c:
            vals.append([c[key], key])
    
        vals.sort(reverse=True)

        return [val[1] for val in vals[:k]]