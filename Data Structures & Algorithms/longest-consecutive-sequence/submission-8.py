class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        Set = set()

        for n in nums:
            Set.add(n)

        for n in nums:
            if (n - 1) not in Set:
                cur = 1
                while (n + cur) in Set:
                    cur += 1
                best = max(best, cur)
        return best

