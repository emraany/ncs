class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        List = {}
        freq = [[] for i in range (len(nums) + 1)]

        for num in nums:
            List[num] = List.get(num, 0) + 1

        for num, cnt in List.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res