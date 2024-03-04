class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        map<int,int> mp;
        vector<vector<int>> res;
        for(auto a:items1){
            mp[a[0]]+=a[1];
        }
        for(auto a:items2){
            mp[a[0]]+=a[1];
        }
        for(auto [x,y] :mp){
            res.push_back({x,y});
        }
        return res;
    }
};