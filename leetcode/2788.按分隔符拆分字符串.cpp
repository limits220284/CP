class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> ans;
        for (auto &w : words) {
            int j = 0;
            for(int i = 0; i <= w.size(); i++){
                if(i == w.size() || w[i] == separator){
                    if(i - j > 0) ans.push_back(w.substr(j, i - j));
                    j = i + 1;
                }
            }

        }
        return ans;
    }
};