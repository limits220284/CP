class FoodRatings {
public:
    unordered_map<string,set<pair<int,string>> > memu;
    unordered_map<string,pair<string,int>> f_c_r;
    //通过第一个unordered_map可以找到不同的方式对应的
    //找到不同的方式之后，不同的方式里面通过map找到对应的不同的食物的的分数
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n=foods.size();     
        for(int i=0;i<n;i++){
            memu[cuisines[i]].insert(make_pair(-ratings[i],foods[i]));
            f_c_r[foods[i]]=make_pair(cuisines[i],ratings[i]);
        }
    }
    
    void changeRating(string food, int newRating) {
        string cui=f_c_r[food].first;
        int grade=f_c_r[food].second;
        memu[cui].erase(make_pair(-grade,food));
        memu[cui].insert(make_pair(-newRating,food));
        f_c_r[food].second=newRating;
    }
    
    string highestRated(string cuisine) {
        return memu[cuisine].begin()->second;
    }
};