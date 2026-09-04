class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = dict()
        tSet = dict()

        for c in s:
            sSet[c] = sSet.get(c, 0) + 1

        for c in t:
            tSet[c] = tSet.get(c, 0) + 1

        return sSet == tSet