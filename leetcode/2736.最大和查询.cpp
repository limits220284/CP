class BIT {
// 注意树状数组维护区间后缀最大值的写法
public:
    vector<int>tree;
    int n;
    static int lowbit(int x){
        return x & (-x);
    }
    BIT(int _n){
        n = _n;
        tree.assign(_n+1, -1);
    }
    int query(int x){
        int ans = -1;
        while(x <= n){
            ans = max(ans, tree[x]);
            x += lowbit(x);
        }
        return ans;
    }
    void update(int x, int val){
        while(x){
            tree[x] = max(tree[x], val);
            x -= lowbit(x);
        }
    }
};

class Solution {
public:
    typedef pair<int, int> pii;
    vector<int> maximumSumQueries(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        int n = nums1.size(), m = queries.size();
        vector<pii> nums;
        for(int i = 0; i < n; i++) nums.push_back({nums1[i], nums2[i]});
        //1、把所有的y进行离散化
        map<int, int> mp;
        vector<int> alls;
        for(auto& x: nums) alls.push_back(x.second);
        for(auto& x: queries) alls.push_back(x[1]);
        sort(alls.begin(), alls.end());
        alls.erase(unique(alls.begin(), alls.end()), alls.end());
        for(int i = 0; i < alls.size(); i++) mp[alls[i]] = i+1;

        //2、将nums, queries关于x进行排序
        sort(nums.begin(), nums.end(), [&](auto& a, auto& b){
            return a.first > b.first;
        });
        vector<int> ids(m);
        iota(ids.begin(), ids.end(), 0);
        sort(ids.begin(), ids.end(), [&](auto& a, auto& b){
            return queries[a][0] > queries[b][0];
        });
        // for(auto&x: ids) cout << x << " ";
        BIT bt(alls.size() + 1);
        int ptr = 0;
        vector<int> ans(m, -1);
        for(int id: ids){
            while(ptr < n && nums[ptr].first >= queries[id][0]){
                bt.update(mp[nums[ptr].second], nums[ptr].first + nums[ptr].second);
                ptr += 1;
            }
            ans[id] = bt.query(mp[queries[id][1]]);
        }
        return ans;
        // int n = nums1.size(), m = queries.size();
        // vector<vector<int>> keys;
        // for(int i = 0;i < n;++i) keys.push_back({nums1[i], nums2[i]});
        
        // // 对y离散化后，规模是m+n，树状数组不会爆内存
        // vector<int> copy(m+n);
        // int p = 0;
        // for(auto& k: keys)
        //     copy[p++] = k[1];
        // for(auto& q: queries)
        //     copy[p++] = q[1];
        // sort(copy.begin(), copy.end());
        // for(auto& x: copy) cout << x << " ";
        // for(auto& k: keys){
        //     k[1] = lower_bound(copy.begin(), copy.end(), k[1]) - copy.begin() + 1;
        // }
        // for(auto& q: queries){
        //     q[1] = lower_bound(copy.begin(), copy.end(), q[1]) - copy.begin() + 1;
        // }
        
        // // 对x降序排序，为了保证输出的顺序，queries数组要对下标进行排序
        // vector<int> ids(m);
        // iota(ids.begin(), ids.end(), 0);
        
        // sort(ids.begin(), ids.end(), [&](int& a, int& b){
        //     return queries[a][0] > queries[b][0];
        // });
        // cout << endl;
        // for(auto&x: ids) cout << x << " ";
        // sort(keys.begin(), keys.end(), [&](vector<int>& a, vector<int>& b){return a[0] > b[0];});
        
        // BIT* bit = new BIT(m + n);
        // int ptr = 0;
        // vector<int> ans(m, -1);
        
        // for(auto& id:ids){
        //     // 保证keys的第一维大于等于queries的第一维
        //     while(ptr < n && keys[ptr][0] >= queries[id][0]){
        //         // 在树状数组中更新，值为x_k + y_k，下标为y_k
        //         bit->update(keys[ptr][1], keys[ptr][0] + copy[keys[ptr][1]-1]);
        //         ++ptr;
        //     }
        //     // 第一维已经得到保证了，现在需要从大于等于y_q的所有y_k中，找到x_k + y_k最大的，也就是利用树状数组求后缀最大值
        //     ans[id] = bit->query(queries[id][1]);
        // }
        // return ans;
        return {};
    }
};