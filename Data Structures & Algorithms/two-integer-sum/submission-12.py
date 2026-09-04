class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            s[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in s and s[diff] != i:
                return [i, s[diff]]
