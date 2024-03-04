class Solution {
public:
    vector<long long> distance(vector<int>& arr) {
        
        vector<long long> result(arr.size(), 0);
        unordered_map<int, vector<long long>> preSum; /* 前缀和分组 */
        unordered_map<int, vector<long long>> nxtSum; /* 后缀和分组 */
        unordered_map<int, int> times;                /* 辅助记录到第几个数字 */
        /* 求和过程 */
        for (int i = 0; i < arr.size(); ++i) {
            preSum[arr[i]].push_back(i);
            nxtSum[arr[i]].push_back(i);
        }
        for (auto &it : preSum) {
            auto &g = it.second;
            for (int i = 1; i < g.size(); ++i) {
                g[i] += g[i - 1];
            }
        }
        for (auto &it : nxtSum) {
            auto &g = it.second;
            for (int i = g.size() - 2; i >= 0; --i) {
                g[i] += g[i + 1];
            }
        }

        /* 计算每个数字的左右端距离 */
        for (long long i = 0; i < arr.size(); ++i) {
            long long index = times[arr[i]]++;
            auto &preVec = preSum[arr[i]];
            auto &nxtVec = nxtSum[arr[i]];
            result[i] += i * (index + 1) - preVec[index];
            result[i] += nxtVec[index] - (nxtVec.size() - index) * i;
        }
        return result;
        
    }
};