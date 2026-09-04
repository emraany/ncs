class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        
        tdict = {}
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        
        return tdict == sdict