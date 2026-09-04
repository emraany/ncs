class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        res = []

        while l < r:
            Sum = numbers[l] + numbers[r]

            if Sum == target:
                return [l + 1, r + 1]
            if Sum < target:
                l += 1
            else:
                r -= 1