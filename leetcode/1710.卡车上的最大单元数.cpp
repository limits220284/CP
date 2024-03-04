class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        const int n = boxTypes.size();
        int sum = 0;
        int l = 0, r = n;
        const auto ptr = boxTypes.data();
        const auto cmp = [&] (const vector<int>& box1, const vector<int>& box2) {
            return box1[1] > box2[1];
        };
        while (l < r) {
            const int mid = (l + r) / 2;
            nth_element(ptr + l, ptr + mid, ptr + r, cmp);
            int nsum = sum;
            for (int i = l;i < mid;++i)
                nsum += ptr[i][0];
            if (truckSize <= nsum)
                r = mid;
            else {
                sum = nsum + ptr[mid][0];
                l = mid + 1;
            }
        }
        int ans = 0;
        for (int i = 0;i < l;++i)
            ans += ptr[i][0] * ptr[i][1];
        if (sum > truckSize) ans -= (sum - truckSize) * ptr[l - 1][1];
        return ans;
    }
};