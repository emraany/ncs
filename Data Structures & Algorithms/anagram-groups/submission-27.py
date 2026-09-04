class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for s in strs:
            curr = {}
            for c in s:
                curr[c] = curr.get(c, 0) + 1
            curr = tuple(sorted(curr.items()))
            if curr not in strings:
                strings[curr] = []
            strings[curr].append(s)

        return list(strings.values())