class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * (n + 1)
        invfact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def dfs(arr):
            m = len(arr)
            if m < 3:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            a, b = len(left), len(right)
            ways = fact[a + b] * invfact[a] % MOD * invfact[b] % MOD
            return ways * dfs(left) % MOD * dfs(right) % MOD

        return (dfs(nums) - 1) % MOD
