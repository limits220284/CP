class Solution {
public:
    long long maxScore(vector<int>& nums, int x) {
        // 只需要知道奇偶的信息
        int n = nums.size();
        double f[2] = {int(-1e9), int(-1e9)};
        f[nums[0] % 2] = nums[0];
        for(int i = 1; i < n; i++){
            int p = nums[i] % 2;
            double t = max(f[p] + nums[i], f[p^1] + nums[i] - x);
            f[p] = max(f[p], t);
        }
        return max(f[0], f[1]);
    }
};