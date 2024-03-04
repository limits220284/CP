class NumberContainers {
private:
unordered_map<int,int> inx_num;
unordered_map<int,set<int>> num_inx;
public:
    NumberContainers() {
        unordered_map<int,int> inx_num;
        unordered_map<int,set<int>> num_inx;
    }
    void change(int index, int number) {
        if(inx_num.find(index)==inx_num.end()){
            inx_num[index]=number;
            num_inx[number].insert(index);
        }
        int x=inx_num[index];
        inx_num[index]=number;
        num_inx[x].erase(index);
        if(num_inx[x].size()==0){
            num_inx.erase(x);
        }
        num_inx[number].insert(index);
    }
    
    int find(int number) {
        if(num_inx.find(number)==num_inx.end()){
            return -1;
        }
        cout<<number;
        return *num_inx[number].begin();
    }
};
/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */