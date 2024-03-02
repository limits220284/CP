class Solution {
public:
    bool canChange(string start, string target) {
        //太勾八优雅了
        auto s = start, t = target;
        s.erase(remove(s.begin(), s.end(), '_'), s.end());
        t.erase(remove(t.begin(), t.end(), '_'), t.end());
        if (s != t) return false;
        for (int i = 0, j = 0; i < start.length(); ++i) {
            if (start[i] == '_') continue;
            while (target[j] == '_') ++j;
            if (i != j && (start[i] == 'L') != (i > j)) return false;
            ++j;
        }
        return true;
    }
};