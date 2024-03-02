type RangeFreqQuery struct {
    pos [1e4 + 1]sort.IntSlice
}


func Constructor(arr []int) RangeFreqQuery {
    q := RangeFreqQuery{}
    for i, value := range arr {
        q.pos[value] = append(q.pos[value], i)
    }
    return q
}


func (q *RangeFreqQuery) Query(left int, right int, value int) int {
    p := q.pos[value]
    return p.Search(right + 1) - p.Search(left)
}


/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
 */