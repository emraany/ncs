class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        count = {}
        for i in range(n):
            count[s2[i]] = count.get(s2[i], 0) + 1

        if count == need:
            return True

        l, r = 0, n
        while r < m:
            count[s2[r]] = count.get(s2[r], 0) + 1
            count[s2[l]] -= 1
            if count[s2[l]] == 0:
                del count[s2[l]]

            l += 1
            r += 1

            if count == need:
                return True
        return False

                 
