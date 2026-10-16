class Solution {
    static constexpr long long MOD = 1'000'000'007;
    int n;
    vector<long long> b1, b2;

    void add(vector<long long>& bit, int i, long long v) {
        for (; i <= n; i += i & -i)
            bit[i] += v;
    }

    long long query(const vector<long long>& bit, int i) {
        long long s = 0;
        for (; i > 0; i -= i & -i)
            s += bit[i];
        return s;
    }

    void rangeAdd(int l, int r) {
        ++l;
        ++r;
        add(b1, l, 1);
        add(b1, r + 1, -1);
        add(b2, l, l - 1);
        add(b2, r + 1, -r);
    }

    long long prefixSum(int i) {
        return query(b1, i) * i - query(b2, i);
    }

public:
    int sumCounts(vector<int>& nums) {
        n = nums.size();
        b1.assign(n + 2, 0);
        b2.assign(n + 2, 0);

        vector<int> last(100001, -1);
        long long curSq = 0, ans = 0;

        for (int i = 0; i < n; ++i) {
            int l = last[nums[i]] + 1;
            long long s = prefixSum(i + 1) - prefixSum(l);
            long long len = i - l + 1LL;

            curSq = (curSq + 2 * s + len) % MOD;

            rangeAdd(l, i);
            last[nums[i]] = i;

            ans = (ans + curSq) % MOD;
        }

        return (int)ans;
    }
};