class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        long long mask = 0;
        for(auto& c: jewels){
            mask |= 1LL << (c & 63);
        }
        int ans = 0;
        for(char c: stones){
            ans += mask >> (c & 63) & 1;
        }
        return ans;
    }
};