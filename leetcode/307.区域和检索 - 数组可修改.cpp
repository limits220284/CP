
const int N = 100010;
typedef long long LL;
int n;
int tr[N];
int a[N];

class NumArray {
public:

    int lowbit(int x){
        return x & -x;
    }
    int query(int x){
        LL res = 0;
        for(int i = x; i; i -= lowbit(i)){
            res += tr[i];
        }
        return res;
    }
    
    void update_tr(int x, int c){
        for(int i = x; i <= n; i += lowbit(i)){
            tr[i] += c;
        }
    }

    NumArray(vector<int>& nums) {
        //构造函数
        memset(tr, 0, sizeof tr);
        n = nums.size();
        for(int i = 0; i < n; i++){
            a[i+1] = nums[i];
        }
        for(int i = 0; i < n; i++){
            update_tr(i+1, nums[i]);
        }
    }
    
    void update(int index, int val) {
        update_tr(index+1, val-a[index+1]);
        a[index+1] = val;
    }
    
    int sumRange(int left, int right) {
        return query(right+1) - query(left);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */