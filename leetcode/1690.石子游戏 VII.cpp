class Solution {
public:
    int stoneGameVII(vector<int>& stones) {
        int n = stones.size();
        vector<int> pre(1, 0);
        for(auto& x: stones) pre.push_back(x + pre.back());
        vector<vector<int>> f(n, vector<int>(n, 0));
        for(int i = n-2; i >= 0; i--){
            for(int j = i+1; j < n; j++){
                f[i][j] = max(pre[j] - pre[i] - f[i][j-1], pre[j+1] - pre[i+1] - f[i+1][j]);
            }
        }
        return f[0][n-1];
    }
};