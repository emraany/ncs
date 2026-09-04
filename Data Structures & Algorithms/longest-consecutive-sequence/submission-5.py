class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set()

        for i in range(len(nums)):
            Set.add(nums[i])
        
        prevMax = 0

        for n in nums:
            m = 0
            
            if not ((n - 1) in Set):
                while(n + 1 in Set):
                    m += 1
                    n += 1
                m+= 1
                prevMax = max(prevMax, m)
            
        return prevMax
            
