class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        Set = set()
        best = 0

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
            Set.add(s[r])
            best = max(best, r - l + 1)

        return best