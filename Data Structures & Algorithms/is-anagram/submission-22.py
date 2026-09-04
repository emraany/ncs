class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = {}
        tSet = {}

        for i in range(len(s)):
            sSet[s[i]] = sSet.get(s[i], 0) + 1

        for i in range(len(t)):
            tSet[t[i]] = tSet.get(t[i], 0) + 1

        return tSet == sSet
        