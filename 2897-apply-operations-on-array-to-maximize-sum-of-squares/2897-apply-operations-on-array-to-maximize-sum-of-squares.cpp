class Solution {
public:
    int maxSum(vector<int>& nums, int k) {
        constexpr long long MOD = 1'000'000'007LL;
        int cnt[30] = {};

        for (int num : nums) {
            while (num) {
                int bit = __builtin_ctz((unsigned)num);
                ++cnt[bit];
                num &= num - 1;
            }
        }

        long long ans = 0;

        for (int i = 0; i < k; ++i) {
            long long x = 0;

            for (int b = 29; b >= 0; --b) {
                if (cnt[b] > 0) {
                    x |= (1LL << b);
                    --cnt[b];
                }
            }

            ans = (ans + x * x) % MOD;
        }

        return static_cast<int>(ans);
    }
};
