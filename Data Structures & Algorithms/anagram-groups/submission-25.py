class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Set = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count [ord(c) - ord('a')] += 1
            Set[tuple(count)].append(s)

        return list(Set.values())
            
