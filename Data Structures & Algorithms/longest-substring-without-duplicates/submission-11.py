class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        Max = 0
        Set = set()

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l += 1
            Set.add(s[r])
            Max = max(Max, r - l + 1)
        
        return Max