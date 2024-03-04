class Solution {
public:
    int maximumSum(vector<int>& nums) {
    int n = nums.size();
    unordered_map<int, vector<int>> mp;
    for (int x : nums) {
        int sum = 0;
        int y = x;
        while (x > 0) {
            int a = x % 10;
            sum += a;
            x = x / 10;
        }
        mp[sum].push_back(y);
    }
    int mx = -1;
    for (auto x : mp) {
        vector<int> y = x.second;
        if (y.size() >= 2) {
            sort(y.begin(), y.end(), greater<int>());
            mx = max(mx, y[0] + y[1]);
        }
    }
    return mx;
}
};