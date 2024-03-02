const int N = 20010;
class Solution {
public:
    unordered_map<int, int> mp;
    typedef long long LL;
    struct Node{
        int l, r;
        int h; // h维护的是每一个区间的最大高度
    }tr[N * 4];

    void build(int p, int l, int r){
        tr[p].l = l, tr[p].r = r;
        if (l == r) return;
        int mid = (l + r) >> 1;
        build(p * 2, l, mid);
        build(p * 2 + 1, mid + 1, r);
    }
    void spread(int p){ //懒标记, 如果存在则向下更新儿子节点的最大高度
        if (tr[p].h){
            tr[p * 2].h = max(tr[p * 2].h, tr[p].h);
            tr[p * 2 + 1].h = max(tr[p * 2 + 1].h, tr[p].h);
            tr[p].h = 0;
        }
    }
    void modfiy(int p, int l, int r, int d){
        if (l <= tr[p].l && r >= tr[p].r){
            tr[p].h = max(tr[p].h, d);
            return;
        }
        spread(p);
        int mid = (tr[p].l + tr[p].r) >> 1;
        if (l <= mid) modfiy(p * 2, l, r, d);
        if (r >= mid + 1) modfiy(p * 2 + 1, l, r, d);
    }

    int query(int p, int x){ // 单点查询离散化的每一个点
        if (tr[p].l == tr[p].r){
            return tr[p].h;
        }
        spread(p);
        int mid = (tr[p].l + tr[p].r) >> 1;
        if (x <= mid) return query(p * 2, x);
        else return query(p * 2 + 1, x);
    }
    vector<vector<int>> getSkyline(vector<vector<int>>& bs) {
        vector<int> ans;
        vector<vector<int>> res;
        for (int i = 0; i < bs.size(); i ++){
            ans.push_back(bs[i][0]);
            ans.push_back(bs[i][1]);
        }
        //排序去重+离散化处理；
        sort(ans.begin(), ans.end());
        ans.erase(unique(ans.begin(), ans.end()), ans.end());
        int n = ans.size();
        for (int i = 0; i < n; i ++) {
            mp[ans[i]] = i + 1;
        }
        build(1, 1, n);
        for (int i = 0; i < bs.size(); i ++){
            int l = mp[bs[i][0]], r = mp[bs[i][1]] - 1;
            modfiy(1, l, r, bs[i][2]);
        }
        int maxv = 0;
        for (int i = 0; i < n; i ++){
            int x = query(1, mp[ans[i]]); 
            if (x != maxv) { // 判断与上一个节点是否相同。
                res.push_back({ans[i], x});
                maxv = x;
            }
        }   
        return res;
    }
};
