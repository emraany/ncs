class Solution:
#. 3#cat4#bird
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        res = "".join(res)
        return res
    
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            Len = int(s[i:j])
            i = j + 1
            j = i + Len
            res.append(s[i:j])
            i = j
        return res
    