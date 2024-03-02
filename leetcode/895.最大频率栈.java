class FreqStack {
    private final Map<Integer, Integer> cnt = new HashMap<>();
    private final List<Deque<Integer>> stacks = new ArrayList<>();
    public void push(int val) {
        int c = cnt.getOrDefault(val, 0);
        if(c == stacks.size()){
            stacks.add(new ArrayDeque<>());
        }
        stacks.get(c).push(val);
        cnt.put(val, c+1);
    }
    
    public int pop() {
        int back = stacks.size() - 1;
        int val = stacks.get(back).pop();
        if(stacks.get(back).isEmpty()){
            stacks.remove(back);
        }
        cnt.put(val, cnt.get(val) - 1);
        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */