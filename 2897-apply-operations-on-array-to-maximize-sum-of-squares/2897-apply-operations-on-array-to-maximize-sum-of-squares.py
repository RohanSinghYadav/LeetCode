class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 30

        for num in nums:
            while num:
                bit = num & -num
                bits[bit.bit_length() - 1] += 1
                num &= num - 1

        ans = 0

        for _ in range(k):
            x = 0
            for b in range(29, -1, -1):
                if bits[b]:
                    x |= 1 << b
                    bits[b] -= 1
            ans = (ans + x * x) % MOD

        return ans
