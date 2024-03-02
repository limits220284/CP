class Solution {
public:
    int find(vector<int>& f,int x){
        if(f[x]==x){
            return x;
        }
        int fa=find(f,f[x]);
        f[x]=fa;
        return fa;
    }
    void Union(vector<int>& f,int x,int y){
        int fa=find(f,x);
        int fb=find(f,y);
        if(fa==fb){
            return;
        }
        f[fb]=fa;
    }
    int minSwapsCouples(vector<int>& row) {
       int n=row.size();
       vector<int> f(n);
       for(int i=0;i<n;i++){
           f[i]=i;
       }
       for(int i=0;i<n;i+=2){
           int x=row[i]/2;
           int y=row[i+1]/2;
           Union(f,x,y);
       }
       unordered_map<int,int> hash;
       for(int i=0;i<n;i++){
           int fa=find(f,f[i]);
           hash[fa]++;
       }
       int cnt=0;
       for(auto& ans:hash){
          if(ans.second>=2){
              cnt+=(ans.second-1);
          }
       }
       return cnt;
    }
};