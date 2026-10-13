
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        vector<long long> squares;
        squares.reserve(nums.size());

        for (int x : nums) {
            squares.push_back(1LL * x * x);
        }

        sort(squares.begin(), squares.end());

        int k = squares.size() / 2;
        long long ans = 0;

        for (int i = k; i < squares.size(); ++i) {
            ans += squares[i];
        }

        for (int i = 0; i < k; ++i) {
            ans -= squares[i];
        }

        return ans;
    }
};
