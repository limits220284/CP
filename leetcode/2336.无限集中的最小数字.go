type SmallestInfiniteSet struct {
    thres int
    s *treeset.Set
}


func Constructor() SmallestInfiniteSet {
    return SmallestInfiniteSet {
        thres: 1, 
        s: treeset.NewWithIntComparator(),
    }    
}


func (this *SmallestInfiniteSet) PopSmallest() int {
    if this.s.Empty() {
        ans := this.thres
        this.thres += 1
        return ans
    }
    it := this.s.Iterator()
    it.Next()
    ans := it.Value().(int)
    this.s.Remove(ans)
    return ans
}


func (this *SmallestInfiniteSet) AddBack(num int) {
    if num < this.thres {
        this.s.Add(num)
    }
}


/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */