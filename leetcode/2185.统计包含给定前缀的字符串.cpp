class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int cnt=0;
        int n=pref.size();
        for(const auto&s :words){
            if(s.compare(0,n,pref)==0){
                cnt++;
            }
        }
        return cnt;
          
    }
};