class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = sorted(x * x for x in nums)
        k = len(nums) // 2
        return sum(nums[k:]) - sum(nums[:k])