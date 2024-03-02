type FreqStack struct {
    cnt map[int]int
    stacks [][]int
}


func Constructor() FreqStack {
    return FreqStack{cnt: map[int]int{}}
}


func (f *FreqStack) Push(val int)  {
    c := f.cnt[val]
    if c == len(f.stacks){
        f.stacks = append(f.stacks, []int{val})
    }else{
        f.stacks[c] = append(f.stacks[c], val)
    }
    f.cnt[val]++
}


func (f *FreqStack) Pop() int {
    back := len(f.stacks) - 1
    st := f.stacks[back]
    bk := len(st) - 1
    val := st[bk]
    if bk == 0{
        f.stacks = f.stacks[:back]
    }else{
        f.stacks[back] = st[:bk]
    }
    f.cnt[val]--
    return val
}


/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * param_2 := obj.Pop();
 */