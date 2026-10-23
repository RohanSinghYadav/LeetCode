class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            x = nums[i]
            if x != i:
                ans &= x
                if ans == 0:
                    return 0
        return max(ans, 0)