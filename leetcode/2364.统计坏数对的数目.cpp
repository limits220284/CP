class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size();
        long long ans = 1LL * n * (n - 1) / 2;
        unordered_map<int, int> mp;
        for (int i = 0; i < n; i++) {
            int t = nums[i] - i;
            ans -= mp[t];
            mp[t]++;
        }
        return ans;
    }
};
