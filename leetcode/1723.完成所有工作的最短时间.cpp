class Solution {
public:
    const int MX = 1e8;
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int n = jobs.size();
        int m = 1 << n;
        vector<int> pre(m, 0);
        for(int i = 1; i < m; i++){
            pre[i] = pre[i^i&-i] + jobs[__builtin_ctz(i)];
        }
        vector<vector<int>> f(k, vector<int>(m, 0));
        for(int i = 0; i < m; i++) f[0][i] = pre[i];
        for(int i = 1; i < k; i++){
            for(int j = 1; j < m; j++){
                int v = MX;
                for(int s = j; s; s = (s - 1) & j){
                    v = min(v, max(pre[s], f[i-1][j^s]));
                }
                f[i][j] = v;
            }
        }
        return f[k-1][m-1];
    }
};