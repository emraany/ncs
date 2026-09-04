class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        Set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
            Set.add(s[r])
            Max = max(Max, r - l + 1)

        return Max
