class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted(x * x for x in nums)
        k = len(squares) // 2
        return sum(squares[k:]) - sum(squares[:k])