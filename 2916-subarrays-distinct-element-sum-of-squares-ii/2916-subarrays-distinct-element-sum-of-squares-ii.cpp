class Solution {
    int n;
    vector<long long> b1, b2;

    void add(vector<long long>& bit, int i, long long v) {
        for (; i <= n + 1; i += i & -i)
            bit[i] += v;
    }

    long long rangeSum(int l, int r) {
        int a = r + 1, b = l;
        int x = a, y = b;
        long long a1 = 0, a2 = 0, b1s = 0, b2s = 0;

        while (a > 0 || b > 0) {
            if (a > 0) {
                a1 += b1[a];
                a2 += b2[a];
                a -= a & -a;
            }
            if (b > 0) {
                b1s += b1[b];
                b2s += b2[b];
                b -= b & -b;
            }
        }

        return x * a1 - a2 - (y * b1s - b2s);
    }

    void rangeAdd(int l, int r) {
        int L = l + 1, R = r + 1;
        add(b1, L, 1);
        add(b1, R + 1, -1);
        add(b2, L, L - 1);
        add(b2, R + 1, -R);
    }

public:
    int sumCounts(vector<int>& nums) {
        constexpr long long MOD = 1'000'000'007;
        n = nums.size();
        b1.assign(n + 2, 0);
        b2.assign(n + 2, 0);

        vector<int> last(100001, -1);
        long long cur = 0, ans = 0;

        for (int i = 0; i < n; ++i) {
            int l = last[nums[i]] + 1;
            long long s = rangeSum(l, i);
            long long len = i - l + 1LL;

            cur = (cur + 2 * s + len) % MOD;
            rangeAdd(l, i);

            last[nums[i]] = i;
            ans = (ans + cur) % MOD;
        }

        return (int)ans;
    }
};