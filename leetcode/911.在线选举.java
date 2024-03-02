class TopVotedCandidate {
    Map<Integer, Integer> cnt;
    List<Integer> tops;
    int[] times;
    public TopVotedCandidate(int[] persons, int[] times) {
        tops = new ArrayList<Integer>();
        cnt = new HashMap<Integer, Integer>();
        int top = -1;
        int mx = -1;
        for(int i = 0; i < persons.length; i++){
            int p = persons[i];
            cnt.put(p, cnt.getOrDefault(p, 0) + 1);
            if(cnt.get(p) >= mx){
                top = p;
                mx = cnt.get(p);
            }
            tops.add(top);
        }
        this.times = times;
    }
    public int q(int t) {
        int l = 0, r = times.length - 1;
        while(l < r){
            int mid = (r + l + 1) / 2;
            if(times[mid] <= t){
                l = mid;
            }
            else{
                r = mid - 1;
            }
        }
        return tops.get(l);
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */