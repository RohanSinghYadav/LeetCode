class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
                if ans == 0:
                    return 0
        return max(ans, 0)