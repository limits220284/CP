class Solution {
public:
    int longestValidSubstring(string word, vector<string>& forbidden) {
        //动态规划解法
        //f[i]代表以i结尾的最长合法字符串的长度，枚举到i的时候，回溯判断10以内的是否出现在ban中
        //如果不在f[i] = f[i] + 1, 否则f[i] = 最长的字符串-1
        int n = word.size();
        unordered_set<string> st(forbidden.begin(), forbidden.end());
        vector<int> f(n+1, 0);
        f[0] = 0;
        int pre = 1;
        for(int i = 1; i <= n; i++){
            bool flag = true;
            int j = 1;
            for(; j <= pre; j++){
                if(i - j < 0) break;
                string s = word.substr(i-j, j);
                if(st.count(s)){
                    flag = false;
                    break;
                }
            }
            if(flag){
                pre += 1;
                pre = min(pre, 10);
                f[i] = f[i-1] + 1;
            }
            else{
                f[i] = j-1;
                pre = j;
            }
        }
        //for(auto& x: f) cout << x << " ";
        return *max_element(f.begin(), f.end());
    }
};




