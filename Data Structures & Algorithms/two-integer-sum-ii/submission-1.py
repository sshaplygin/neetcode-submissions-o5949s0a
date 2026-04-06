class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            s = numbers[i] + numbers[j]
            if target == s:
                return [i + 1, j + 1]
            
            if s > target:
                j -= 1
                continue
            
            i += 1
        return []

