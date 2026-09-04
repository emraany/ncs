class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = dict()

        for i, n in enumerate(nums):
            Map[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in Map and Map[diff] != i:
                return [i, Map[diff]]
        