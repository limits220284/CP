class Solution {
public:
    int addMinimum(string word) {
        int n = word.size();
        int cnt = 1;
        for(int i = 0; i < n-1; i++){
            if(word[i] >= word[i+1]){
                cnt += 1;
            }
        }
        return 3 * cnt - n;
    }
};