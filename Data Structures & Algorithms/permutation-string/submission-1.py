class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # target freq
        perm = {}
        for c in s1:
            perm[c] = perm.get(c, 0) + 1

        # first window freq
        count = {}
        for i in range(n):
            count[s2[i]] = count.get(s2[i], 0) + 1

        if count == perm:
            return True

        l, r = 0, n  # r points to the NEXT char after the current window [l, r)
        while r < m:
            # add right char
            rc = s2[r]
            count[rc] = count.get(rc, 0) + 1

            # remove left char
            lc = s2[l]
            count[lc] -= 1
            if count[lc] == 0:
                del count[lc]

            # move window
            l += 1
            r += 1

            if count == perm:
                return True

        return False
