class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = i
        
        for i, n in enumerate(nums):
            c = target - n 
            if c in d and i != d[c]:
                return [i, d[c]]
        return []