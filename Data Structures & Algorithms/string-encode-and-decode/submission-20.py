class Solution:

    def encode(self, strs: List[str]) -> str:
        sb = []
        for s in strs:
            sb.append(str(len(s)))
            sb.append('#')
            sb.append(s)
        s = "".join(sb)
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
#. 3#cat4#bird

